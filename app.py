# ========================================================================
# FLASK AYURVEDIC FOOD GUIDANCE SYSTEM - FIXED & IMPROVED VERSION
# ========================================================================
# File: app.py (Main application file)

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.menu import MenuLink
from flask_admin.theme import Bootstrap4Theme
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ayurvedic_food.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# ========================================================================
# DATABASE MODELS - IMPROVED STRUCTURE
# ========================================================================

# Many-to-Many relationship tables
food_season = db.Table('food_season',
    db.Column('food_id', db.Integer, db.ForeignKey('food_items.id'), primary_key=True),
    db.Column('season_id', db.Integer, db.ForeignKey('seasons.id'), primary_key=True),
    db.Column('is_suitable', db.Boolean, default=True)  # Can be suitable or not suitable
)

food_disease = db.Table('food_disease',
    db.Column('food_id', db.Integer, db.ForeignKey('food_items.id'), primary_key=True),
    db.Column('disease_id', db.Integer, db.ForeignKey('diseases.id'), primary_key=True),
    db.Column('is_beneficial', db.Boolean, default=True)  # Beneficial or harmful
)

food_taste = db.Table('food_taste',
    db.Column('food_id', db.Integer, db.ForeignKey('food_items.id'), primary_key=True),
    db.Column('taste_id', db.Integer, db.ForeignKey('tastes.id'), primary_key=True)
)

class Season(db.Model):
    __tablename__ = 'seasons'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    name_hindi = db.Column(db.String(100), nullable=False)
    name_english = db.Column(db.String(100), nullable=False)
    name_marathi = db.Column(db.String(100), nullable=False)
    months = db.Column(db.String(50))  # e.g., "Nov-Dec"
    
    def __repr__(self):
        return f'<Season {self.code}>'

class Disease(db.Model):
    __tablename__ = 'diseases'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    name_hindi = db.Column(db.String(100), nullable=False)
    name_english = db.Column(db.String(100), nullable=False)
    name_marathi = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Disease {self.code}>'

class Taste(db.Model):
    __tablename__ = 'tastes'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    name_hindi = db.Column(db.String(100), nullable=False)
    name_english = db.Column(db.String(100), nullable=False)
    name_marathi = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Taste {self.code}>'

class FoodType(db.Model):
    __tablename__ = 'food_types'

    id            = db.Column(db.Integer, primary_key=True)
    code          = db.Column(db.String(50), unique=True, nullable=False)
    name_hindi    = db.Column(db.String(100), nullable=False)
    name_english  = db.Column(db.String(100), nullable=False)
    name_marathi  = db.Column(db.String(100), nullable=False)
    icon          = db.Column(db.String(10), default='🍽️')
    display_order = db.Column(db.Integer, default=0)
    is_active     = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<FoodType {self.code}>'


class FoodItem(db.Model):
    __tablename__ = 'food_items'
    
    id = db.Column(db.Integer, primary_key=True)
    name_hindi = db.Column(db.String(200), nullable=False)
    name_english = db.Column(db.String(200))
    name_marathi = db.Column(db.String(200))
    
    # Food classification
    food_type = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    
    # For Vrati (fasting) suitability
    suitable_for_vrat = db.Column(db.Boolean, default=False)
    
    # Additional classification (from Excel data)
    sub_category      = db.Column(db.String(100))   # e.g. सादा, हरी फलीदार पतली, दूध
    is_laghu          = db.Column(db.Boolean, default=False)  # लघु (Light)
    is_guru           = db.Column(db.Boolean, default=False)  # गुरु (Heavy)
    is_garm           = db.Column(db.Boolean, default=False)  # गर्म (Hot)
    is_thanda         = db.Column(db.Boolean, default=False)  # ठंडा (Cold)

    # Descriptions
    description_hindi = db.Column(db.Text)
    description_english = db.Column(db.Text)
    description_marathi = db.Column(db.Text)
    
    # Relationships
    seasons = db.relationship('Season', secondary=food_season, backref='foods')
    diseases = db.relationship('Disease', secondary=food_disease, backref='foods')
    tastes = db.relationship('Taste', secondary=food_taste, backref='foods')
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<FoodItem {self.name_hindi}>'
    
    def is_suitable_for_season(self, season_code):
        """Check if food is suitable for given season"""
        for season in self.seasons:
            if season.code == season_code:
                # Check food_season table for is_suitable flag
                stmt = food_season.select().where(
                    (food_season.c.food_id == self.id) & 
                    (food_season.c.season_id == season.id)
                )
                result = db.session.execute(stmt).first()
                return result.is_suitable if result else True
        return False
    
    def is_beneficial_for_disease(self, disease_code):
        """Check if food is beneficial for given disease"""
        for disease in self.diseases:
            if disease.code == disease_code:
                stmt = food_disease.select().where(
                    (food_disease.c.food_id == self.id) & 
                    (food_disease.c.disease_id == disease.id)
                )
                result = db.session.execute(stmt).first()
                return result.is_beneficial if result else None
        return None

class AdminUser(db.Model):
    __tablename__ = 'admin_users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<AdminUser {self.username}>'

class UserPreference(db.Model):
    __tablename__ = 'user_preferences'
    
    id = db.Column(db.Integer, primary_key=True)
    session_key = db.Column(db.String(100), nullable=False)
    for_whom = db.Column(db.String(20))
    ritu = db.Column(db.String(50))
    bimari = db.Column(db.String(50))
    rasa = db.Column(db.String(200))  # comma-separated restriction values e.g. "hari,doodh"
    max_items = db.Column(db.Integer, default=20)
    language = db.Column(db.String(10), default='hi')  # hi, en, mr
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Preference {self.session_key}>'

class SelectedFood(db.Model):
    __tablename__ = 'selected_foods'
    
    id = db.Column(db.Integer, primary_key=True)
    session_key = db.Column(db.String(100), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('food_items.id'), nullable=False)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    food = db.relationship('FoodItem', backref='selections')
    
    def __repr__(self):
        return f'<Selection {self.food_id}>'

# ========================================================================
# FLASK-ADMIN SETUP WITH AUTHENTICATION
# ========================================================================

class SecureAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return super(SecureAdminIndexView, self).index()




class SecureModelView(ModelView):
    def is_accessible(self):
        return session.get('admin_logged_in')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin_login'))



# Initialize Flask-Admin
admin = Admin(
    app,
    name='आयुर्वेदिक आहार Admin',
    index_view=SecureAdminIndexView()
)
admin.add_view(SecureModelView(FoodType, db.session, name='Food Types'))
admin.add_view(SecureModelView(FoodItem, db.session, name='Food Items'))
admin.add_view(SecureModelView(Season, db.session, name='Seasons'))
admin.add_view(SecureModelView(Disease, db.session, name='Diseases'))
admin.add_view(SecureModelView(Taste, db.session, name='Tastes'))
admin.add_view(SecureModelView(UserPreference, db.session, name='User Preferences'))
admin.add_view(SecureModelView(SelectedFood, db.session, name='Selected Foods'))
admin.add_view(SecureModelView(AdminUser, db.session, name='Admin Users'))
admin.add_link(MenuLink(name='🔓 Logout', url='/admin/logout', category=''))

# ========================================================================
# ADMIN AUTHENTICATION ROUTES
# ========================================================================

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = AdminUser.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['admin_logged_in'] = True
            session['admin_username'] = username
            return redirect('/admin/')
        else:
            error = 'Invalid username or password'
            return render_template('admin_login.html', error=error)
    
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    session.pop('admin_username', None)
    return redirect(url_for('admin_login'))

# ========================================================================
# MAIN APPLICATION ROUTES
# ========================================================================

@app.route('/')
def index():
    # Get reference data for dropdowns
    seasons = Season.query.all()
    diseases = Disease.query.all()
    tastes = Taste.query.all()
    
    return render_template('index.html', seasons=seasons, diseases=diseases, tastes=tastes)

@app.route('/submit', methods=['POST'])
def submit_form():
    if 'session_id' not in session:
        session['session_id'] = os.urandom(24).hex()
    
    session_key = session['session_id']
    
    # Save user preferences with language
    pref = UserPreference(
        session_key=session_key,
        for_whom=request.form.get('for_whom'),
        ritu=request.form.get('ritu'),
        bimari=request.form.get('bimari', ''),
        rasa=','.join(request.form.getlist('rasa')),  # multi-value from checkboxes
        max_items=int(request.form.get('max_items', 20)),
        language=request.form.get('language', 'hi')
    )
    
    db.session.add(pref)
    db.session.commit()
    
    return redirect(url_for('recommendations'))

@app.route('/recommendations')
def recommendations():
    if 'session_id' not in session:
        return redirect(url_for('index'))
    
    session_key = session['session_id']
    pref = UserPreference.query.filter_by(session_key=session_key).order_by(UserPreference.created_at.desc()).first()
    
    if not pref:
        return redirect(url_for('index'))
    
    # Get reference data for filters
    seasons = Season.query.all()
    diseases = Disease.query.all()
    tastes = Taste.query.all()
    
    return render_template('recommendations.html', preference=pref, seasons=seasons, diseases=diseases, tastes=tastes)

@app.route('/api/food-data', methods=['POST'])
def get_food_data():
    if 'session_id' not in session:
        return jsonify({'success': False, 'error': 'No session'})
    
    session_key = session['session_id']
    pref = UserPreference.query.filter_by(session_key=session_key).order_by(UserPreference.created_at.desc()).first()
    
    if not pref:
        return jsonify({'success': False, 'error': 'No preferences found'})
    
    # Build query
    query = FoodItem.query

    # Get request body overrides (sidebar live-filter on recommendations page)
    request_data = request.get_json(silent=True) or {}

    # Sync max_items if client sent an updated value
    if 'max_items' in request_data:
        new_max = int(request_data['max_items'])
        if 1 <= new_max <= 200 and new_max != pref.max_items:
            pref.max_items = new_max
            db.session.commit()

    # Filter by vrat
    if pref.for_whom == 'vrati':
        query = query.filter_by(suitable_for_vrat=True)
    
    # Filter by season (allow sidebar override)
    ritu_filter = request_data.get('ritu') or pref.ritu
    if ritu_filter and ritu_filter != '':
        season = Season.query.filter_by(code=ritu_filter).first()
        if season:
            query = query.filter(FoodItem.seasons.contains(season))
    
    # Filter by disease (allow sidebar override)
    bimari_filter = request_data.get('bimari')
    if bimari_filter is None:
        bimari_filter = pref.bimari
    if bimari_filter and bimari_filter != '':
        disease = Disease.query.filter_by(code=bimari_filter).first()
        if disease:
            query = query.filter(FoodItem.diseases.contains(disease))
    
    # ── Rasi restriction filter ─────────────────────────────────────
    # rasa = comma-separated rasi codes e.g. "hari,doodh,tel"
    # Each rasi value maps to food_type codes to EXCLUDE from results.
    # Logic: excluded food_types are removed entirely; excluded taste codes
    # remove foods that have that taste associated.
    RASI_EXCLUDE_TYPES = {
        'hari':   ['leafy_veg', 'vegetable'],   # all green veg
        'meetha': ['sweetener', 'sweet'],        # sweets, jaggery, sugar
        'ghee':   [],                            # ghee is in dairy — excluded by name filter below
        'doodh':  ['dairy', 'beverage'],         # milk, curd, buttermilk, warm milk etc
        'khatai': [],                            # sour — exclude by taste code 'amla'
        'tel':    ['oil'],                       # all oils
        'namak':  [],                            # salt — excluded by taste code 'lavana'
    }
    RASI_EXCLUDE_TASTES = {
        'khatai': ['amla'],     # sour taste
        'namak':  ['lavana'],   # salty taste
        'meetha': ['madhur'],   # sweet taste (belt-and-suspenders)
    }
    # Name fragments to exclude (case-insensitive) for ghee specifically
    RASI_EXCLUDE_NAMES = {
        'ghee':  ['ghee', 'घी', 'तूप'],
        'doodh': ['milk', 'दूध', 'दुध'],  # catches items like "Warm Milk" not in dairy type
    }

    rasa_str = request_data.get('rasa') or pref.rasa or ''
    rasi_values = [r.strip() for r in rasa_str.split(',') if r.strip()]

    if rasi_values:
        excluded_types = set()
        excluded_taste_codes = set()
        excluded_name_frags = []

        for rv in rasi_values:
            excluded_types.update(RASI_EXCLUDE_TYPES.get(rv, []))
            excluded_taste_codes.update(RASI_EXCLUDE_TASTES.get(rv, []))
            excluded_name_frags.extend(RASI_EXCLUDE_NAMES.get(rv, []))

        # Exclude by food_type
        if excluded_types:
            query = query.filter(~FoodItem.food_type.in_(list(excluded_types)))

        # Exclude by taste association
        if excluded_taste_codes:
            excluded_tastes = Taste.query.filter(
                Taste.code.in_(list(excluded_taste_codes))
            ).all()
            for et in excluded_tastes:
                query = query.filter(~FoodItem.tastes.contains(et))

        # Apply name-based exclusion after main query
        foods = query.all()
        if excluded_name_frags:
            import re
            pattern = '|'.join(re.escape(f) for f in excluded_name_frags)
            foods = [f for f in foods if not re.search(
                pattern,
                (f.name_hindi or '') + (f.name_english or '') + (f.name_marathi or ''),
                re.IGNORECASE
            )]
    else:
        foods = query.all()
    
    
    # Get language: prefer request body override, fall back to saved preference
    lang = request_data.get('language') or (pref.language if pref.language else 'hi')
    if lang not in ['hi', 'en', 'mr']:
        lang = 'hi'
    name_field = f'name_{lang}' if lang in ['hi', 'en', 'mr'] else 'name_hindi'
    if lang == 'hi':
        name_field = 'name_hindi'
    elif lang == 'en':
        name_field = 'name_english'
    elif lang == 'mr':
        name_field = 'name_marathi'
    
    # Organize by food type and category — load from DB food_types table
    result = {}
    db_food_types = FoodType.query.filter_by(is_active=True).order_by(FoodType.display_order).all()
    food_types = {
        ft.code: {'hi': ft.name_hindi, 'en': ft.name_english, 'mr': ft.name_marathi}
        for ft in db_food_types
    }
    
    for food_type_code, food_type_names in food_types.items():
        type_foods = [f for f in foods if f.food_type == food_type_code]
        
        if type_foods:
            result[food_type_code] = {
                'name': food_type_names.get(lang, food_type_names['hi']),
                'eat': [{'id': f.id, 'name': getattr(f, name_field, f.name_hindi)} for f in type_foods if f.category == 'eat'],
                'less_eat': [{'id': f.id, 'name': getattr(f, name_field, f.name_hindi)} for f in type_foods if f.category == 'less_eat'],
                'dont_eat': [{'id': f.id, 'name': getattr(f, name_field, f.name_hindi)} for f in type_foods if f.category == 'dont_eat'],
            }
    
    return jsonify({
        'success': True,
        'data': result,
        'max_items': pref.max_items,
        'language': lang
    })

@app.route('/api/toggle-selection', methods=['POST'])
def toggle_selection():
    if 'session_id' not in session:
        return jsonify({'success': False, 'error': 'No session'})
    
    data = request.get_json()
    food_id = data.get('food_id')
    action = data.get('action')
    session_key = session['session_id']
    
    pref = UserPreference.query.filter_by(session_key=session_key).order_by(UserPreference.created_at.desc()).first()
    
    if action == 'add':
        count = SelectedFood.query.filter_by(session_key=session_key).count()
        if count >= pref.max_items:
            return jsonify({
                'success': False,
                'error': f'अधिकतम {pref.max_items} व्यंजन की सीमा पूर्ण!'
            })
        
        selection = SelectedFood(session_key=session_key, food_id=food_id)
        db.session.add(selection)
    else:
        SelectedFood.query.filter_by(session_key=session_key, food_id=food_id).delete()
    
    db.session.commit()
    
    count = SelectedFood.query.filter_by(session_key=session_key).count()
    return jsonify({'success': True, 'count': count})

@app.route('/api/selected-foods')
def get_selected_foods():
    if 'session_id' not in session:
        return jsonify({'success': True, 'items': [], 'count': 0})
    
    session_key = session['session_id']
    selections = SelectedFood.query.filter_by(session_key=session_key).all()
    
    items = [{
        'id': s.id,
        'food_id': s.food_id,
        'name': s.food.name_hindi,
        'type': s.food.food_type
    } for s in selections]
    
    return jsonify({'success': True, 'items': items, 'count': len(items)})


@app.route('/api/all-foods')
def get_all_foods():
    """Return all food items as flat list with all properties, matching the screenshot table format."""
    lang = request.args.get('lang', 'hi')
    if lang not in ['hi', 'en', 'mr']:
        lang = 'hi'
    name_field = {'hi': 'name_hindi', 'en': 'name_english', 'mr': 'name_marathi'}[lang]

    # Load food types for display names
    db_food_types = {ft.code: ft for ft in FoodType.query.filter_by(is_active=True).all()}

    foods = FoodItem.query.order_by(FoodItem.food_type, FoodItem.category, FoodItem.id).all()
    items = []
    for idx, f in enumerate(foods, 1):
        ft = db_food_types.get(f.food_type)
        type_name = getattr(ft, f'name_{lang}', f.food_type) if ft else f.food_type
        type_icon = ft.icon if ft else '🍽️'
        items.append({
            'idx':         idx,
            'id':          f.id,
            'name':        getattr(f, name_field, f.name_hindi) or f.name_hindi,
            'type_code':   f.food_type,
            'type_name':   type_name,
            'type_icon':   type_icon,
            'sub_category': f.sub_category or '',
            'category':    f.category,
            'vrat':        f.suitable_for_vrat,
            'is_laghu':    f.is_laghu,
            'is_guru':     f.is_guru,
            'is_garm':     f.is_garm,
            'is_thanda':   f.is_thanda,
        })
    return jsonify({'success': True, 'items': items, 'total': len(items), 'lang': lang})


@app.route('/api/update-max-items', methods=['POST'])
def update_max_items():
    """Update max_items in UserPreference session record."""
    pref_id = session.get('preference_id')
    if not pref_id:
        return jsonify({'success': False, 'error': 'No session'})
    
    data = request.get_json(silent=True) or {}
    new_max = int(data.get('max_items', 20))
    if new_max < 1 or new_max > 200:
        return jsonify({'success': False, 'error': 'Invalid value'})
    
    pref = UserPreference.query.get(pref_id)
    if not pref:
        return jsonify({'success': False, 'error': 'Preference not found'})
    
    pref.max_items = new_max
    db.session.commit()
    return jsonify({'success': True, 'max_items': new_max})

# ========================================================================
# INITIALIZE DATABASE (tables only — no sample data)
# ========================================================================

def init_db():
    """Create all database tables. Run load_data.py separately to seed data."""
    with app.app_context():
        db.create_all()
        print("✅ Database tables created.")

# ========================================================================
# RUN APPLICATION
# ========================================================================

if __name__ == '__main__':
    init_db()
    print("\n" + "="*60)
    print("🍃 आयुर्वेदिक आहार मार्गदर्शन प्रणाली")
    print("="*60)
    print("\n📱 Application: http://127.0.0.1:5000/")
    print("🔧 Admin Panel: http://127.0.0.1:5000/admin/")
    print("\n✨ Press CTRL+C to stop the server\n")
    print("="*60 + "\n")
    
    app.run(debug=True, port=5000)