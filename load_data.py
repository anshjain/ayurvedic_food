# ========================================================================
# load_data.py — Seed the database with reference + sample food data
# ========================================================================
# Run once after setting up the database:
#   python load_data.py
#
# Safe to re-run — skips any data that already exists.
# ========================================================================

from app import app, db
from app import Season, Disease, Taste, FoodType, FoodItem, AdminUser
import sys

sys.stdout.reconfigure(encoding='utf-8')

def seed_admin():
    if AdminUser.query.filter_by(username='admin').first():
        print("⏭️  Admin user already exists, skipping.")
        return
    admin_user = AdminUser(username='admin', email='admin@example.com')
    admin_user.set_password('admin123')
    db.session.add(admin_user)
    db.session.commit()
    print("✅ Admin user created — username: admin / password: admin123")


def seed_seasons():
    if Season.query.first():
        print("⏭️  Seasons already seeded, skipping.")
        return
    seasons_data = [
        {'code': 'margshirsh', 'name_hindi': 'मार्गशीर्ष', 'name_english': 'Margshirsh', 'name_marathi': 'मार्गशीर्ष', 'months': 'Nov-Dec'},
        {'code': 'paush',      'name_hindi': 'पौष',         'name_english': 'Paush',      'name_marathi': 'पौष',         'months': 'Dec-Jan'},
        {'code': 'magh',       'name_hindi': 'माघ',          'name_english': 'Magh',       'name_marathi': 'माघ',          'months': 'Jan-Feb'},
        {'code': 'phalgun',    'name_hindi': 'फाल्गुन',      'name_english': 'Phalgun',    'name_marathi': 'फाल्गुन',      'months': 'Feb-Mar'},
        {'code': 'chaitra',    'name_hindi': 'चैत्र',         'name_english': 'Chaitra',    'name_marathi': 'चैत्र',         'months': 'Mar-Apr'},
        {'code': 'vaishakh',   'name_hindi': 'वैशाख',         'name_english': 'Vaishakh',   'name_marathi': 'वैशाख',         'months': 'Apr-May'},
        {'code': 'jyeshtha',   'name_hindi': 'ज्येष्ठ',       'name_english': 'Jyeshtha',   'name_marathi': 'ज्येष्ठ',       'months': 'May-Jun'},
        {'code': 'ashadh',     'name_hindi': 'आषाढ़',          'name_english': 'Ashadh',     'name_marathi': 'आषाढ',           'months': 'Jun-Jul'},
        {'code': 'shravan',    'name_hindi': 'श्रावण',         'name_english': 'Shravan',    'name_marathi': 'श्रावण',         'months': 'Jul-Aug'},
        {'code': 'bhadrapad',  'name_hindi': 'भाद्रपद',       'name_english': 'Bhadrapad',  'name_marathi': 'भाद्रपद',       'months': 'Aug-Sep'},
        {'code': 'ashwin',     'name_hindi': 'आश्विन',         'name_english': 'Ashwin',     'name_marathi': 'आश्विन',         'months': 'Sep-Oct'},
        {'code': 'kartik',     'name_hindi': 'कार्तिक',        'name_english': 'Kartik',     'name_marathi': 'कार्तिक',        'months': 'Oct-Nov'},
    ]
    for data in seasons_data:
        db.session.add(Season(**data))
    db.session.commit()
    print(f"✅ {len(seasons_data)} seasons seeded.")


def seed_diseases():
    if Disease.query.first():
        print("⏭️  Diseases already seeded, skipping.")
        return
    diseases_data = [
        {'code': 'fever',    'name_hindi': 'बुखार',        'name_english': 'Fever',   'name_marathi': 'ताप'},
        {'code': 'cold',     'name_hindi': 'सर्दी-जुकाम', 'name_english': 'Cold',    'name_marathi': 'सर्दी'},
        {'code': 'cough',    'name_hindi': 'खांसी',         'name_english': 'Cough',   'name_marathi': 'खोकला'},
        {'code': 'diabetes', 'name_hindi': 'मधुमेह',        'name_english': 'Diabetes','name_marathi': 'मधुमेह'},
        {'code': 'bp',       'name_hindi': 'उच्च रक्तचाप', 'name_english': 'High BP', 'name_marathi': 'उच्च रक्तदाब'},
        {'code': 'acidity',  'name_hindi': 'एसिडिटी',       'name_english': 'Acidity', 'name_marathi': 'आम्लपित्त'},
    ]
    for data in diseases_data:
        db.session.add(Disease(**data))
    db.session.commit()
    print(f"✅ {len(diseases_data)} diseases seeded.")


def seed_tastes():
    if Taste.query.first():
        print("⏭️  Tastes already seeded, skipping.")
        return
    tastes_data = [
        {'code': 'madhur',  'name_hindi': 'मधुर',  'name_english': 'Sweet',      'name_marathi': 'गोड'},
        {'code': 'amla',    'name_hindi': 'अम्ल',   'name_english': 'Sour',       'name_marathi': 'आंबट'},
        {'code': 'lavana',  'name_hindi': 'लवण',    'name_english': 'Salty',      'name_marathi': 'खारट'},
        {'code': 'katu',    'name_hindi': 'कटु',    'name_english': 'Pungent',    'name_marathi': 'तिखट'},
        {'code': 'tikta',   'name_hindi': 'तिक्त',  'name_english': 'Bitter',     'name_marathi': 'कडू'},
        {'code': 'kashaya', 'name_hindi': 'कषाय',   'name_english': 'Astringent', 'name_marathi': 'आकड'},
    ]
    for data in tastes_data:
        db.session.add(Taste(**data))
    db.session.commit()
    print(f"✅ {len(tastes_data)} tastes seeded.")


def seed_food_types():
    if FoodType.query.first():
        print("⏭️  Food types already seeded, skipping.")
        return
    food_types_data = [
        {'code': 'fruit',       'name_hindi': 'फल',              'name_english': 'Fruit',           'name_marathi': 'फळ',           'icon': '🍎', 'display_order': 1},
        {'code': 'fruit_juice', 'name_hindi': 'फलों का रस',      'name_english': 'Fruit Juice',     'name_marathi': 'फळांचा रस',   'icon': '🥤', 'display_order': 2},
        {'code': 'vegetable',   'name_hindi': 'सब्जी',            'name_english': 'Vegetable',       'name_marathi': 'भाजी',         'icon': '🥦', 'display_order': 3},
        {'code': 'leafy_veg',   'name_hindi': 'पत्तेदार सब्जी',  'name_english': 'Leafy Vegetable', 'name_marathi': 'पालेभाजी',    'icon': '🥬', 'display_order': 4},
        {'code': 'grain',       'name_hindi': 'अन्न',             'name_english': 'Grain',           'name_marathi': 'धान्य',        'icon': '🌾', 'display_order': 5},
        {'code': 'pulse',       'name_hindi': 'दाल',              'name_english': 'Pulse',           'name_marathi': 'डाळ',          'icon': '🫘', 'display_order': 6},
        {'code': 'spice',       'name_hindi': 'मसाला',            'name_english': 'Spice',           'name_marathi': 'मसाला',        'icon': '🌿', 'display_order': 7},
        {'code': 'dry_fruit',   'name_hindi': 'सूखे मेवे',        'name_english': 'Dry Fruit',       'name_marathi': 'सुके मेवे',   'icon': '🥜', 'display_order': 8},
        {'code': 'dairy',       'name_hindi': 'दूध उत्पाद',       'name_english': 'Dairy Products',  'name_marathi': 'दुग्धजन्य',   'icon': '🥛', 'display_order': 9},
        {'code': 'oil',         'name_hindi': 'तेल / चिकनाई',    'name_english': 'Oil / Fat',       'name_marathi': 'तेल',          'icon': '🫙', 'display_order': 10},
        {'code': 'sweetener',   'name_hindi': 'मीठा',             'name_english': 'Sweetener',       'name_marathi': 'गोड पदार्थ',  'icon': '🍯', 'display_order': 11},
        {'code': 'beverage',    'name_hindi': 'पेय',              'name_english': 'Beverage',        'name_marathi': 'पेय',          'icon': '☕', 'display_order': 12},
        {'code': 'soup',        'name_hindi': 'सूप',              'name_english': 'Soup',            'name_marathi': 'सूप',          'icon': '🍲', 'display_order': 13},
        {'code': 'roti',        'name_hindi': 'रोटी',             'name_english': 'Roti / Bread',    'name_marathi': 'रोटी / भाकरी','icon': '🫓', 'display_order': 14},
        {'code': 'nashta',      'name_hindi': 'नाश्ता',           'name_english': 'Snacks / Nashta', 'name_marathi': 'नाश्ता',      'icon': '🍘', 'display_order': 15},
        {'code': 'sweet',       'name_hindi': 'मीठे व्यंजन',     'name_english': 'Sweet Dishes',    'name_marathi': 'गोड पदार्थ',  'icon': '🍮', 'display_order': 16},
    ]
    for data in food_types_data:
        db.session.add(FoodType(**data))
    db.session.commit()
    print(f"✅ {len(food_types_data)} food types seeded.")


def seed_foods():
    if FoodItem.query.first():
        print("⏭️  Food items already seeded, skipping.")
        return

    def s(*codes): return Season.query.filter(Season.code.in_(codes)).all()
    def d(*codes): return Disease.query.filter(Disease.code.in_(codes)).all()
    def t(*codes): return Taste.query.filter(Taste.code.in_(codes)).all()

    ALL = 'all'
    all_seasons = Season.query.all()

    # Property defaults per food type (sub_category, laghu, guru, garm, thanda)
    FOOD_TYPE_PROPS = {
        'fruit':       ('ताजा फल',          True,  False, False, True),
        'fruit_juice': ('ठंडे जल',           True,  False, False, True),
        'vegetable':   ('हरी फलीदार पतली',   True,  False, False, True),
        'leafy_veg':   ('पत्तेदार पतली',     True,  False, False, True),
        'grain':       ('सादा',              True,  False, False, True),
        'pulse':       ('सादी पतली',         True,  False, False, True),
        'spice':       ('मसाला',             False, False, True,  False),
        'dry_fruit':   ('मेवे',              False, True,  False, False),
        'dairy':       ('दूध',               False, True,  True,  False),
        'oil':         ('तेल',               False, True,  True,  False),
        'sweetener':   ('मीठा',              False, True,  True,  False),
        'beverage':    ('ठंडे जल',           True,  False, False, True),
        'soup':        ('सादी पतली',         True,  False, True,  False),
        'roti':        ('सादा',              True,  False, False, True),
        'nashta':      ('सादा',              True,  False, False, False),
        'sweet':       ('दूध',               False, True,  True,  False),
    }

    def make_food(name_hi, name_en, name_mr, food_type, category, vrat,
                  season_codes, disease_codes, taste_codes,
                  sub_cat=None, laghu=None, guru=None, garm=None, thanda=None):
        props = FOOD_TYPE_PROPS.get(food_type, ('', False, False, False, False))
        f = FoodItem(
            name_hindi=name_hi, name_english=name_en, name_marathi=name_mr,
            food_type=food_type, category=category, suitable_for_vrat=vrat,
            sub_category = sub_cat  if sub_cat  is not None else props[0],
            is_laghu     = laghu    if laghu     is not None else props[1],
            is_guru      = guru     if guru      is not None else props[2],
            is_garm      = garm     if garm      is not None else props[3],
            is_thanda    = thanda   if thanda    is not None else props[4],
        )
        f.seasons  = s(*season_codes) if season_codes != ALL else all_seasons
        f.diseases = d(*disease_codes) if disease_codes else []
        f.tastes   = t(*taste_codes)   if taste_codes   else []
        return f

    sample_foods = [

        # ================================================================
        # FRUITS (फल) — Image 6
        # ================================================================
        make_food('केला','Banana','केळं','fruit','eat',True,
            ['margshirsh','paush','magh','phalgun'],['fever','acidity'],['madhur']),
        make_food('सेब (लाल)','Apple (Red)','सफरचंद (लाल)','fruit','eat',True,
            ['ashwin','kartik','margshirsh'],['diabetes','bp'],['madhur','amla']),
        make_food('सेब (सफेद)','Apple (White)','सफरचंद (पांढरे)','fruit','eat',True,
            ['ashwin','kartik','margshirsh'],['diabetes','bp'],['madhur','amla']),
        make_food('आम','Mango','आंबा','fruit','less_eat',True,
            ['vaishakh','jyeshtha','chaitra'],['diabetes'],['madhur','amla']),
        make_food('पपीता','Papaya','पपई','fruit','eat',False,
            ['chaitra','vaishakh','ashwin'],['acidity','fever'],['madhur']),
        make_food('अनार','Pomegranate','डाळिंब','fruit','eat',True,
            ['ashwin','kartik','shravan'],['fever','bp','diabetes'],['madhur','amla']),
        make_food('तरबूज','Watermelon','टरबूज','fruit','eat',True,
            ['vaishakh','jyeshtha','ashadh'],['bp','fever'],['madhur']),
        make_food('अंगूर (काला)','Grapes (Black)','द्राक्ष (काळे)','fruit','less_eat',True,
            ['phalgun','chaitra'],['acidity'],['madhur','amla']),
        make_food('अंगूर (सफेद)','Grapes (White)','द्राक्ष (पांढरे)','fruit','less_eat',True,
            ['phalgun','chaitra'],['acidity'],['madhur','amla']),
        make_food('संतरा / मुसंबी','Orange / Sweet Lime','संत्रा / मोसंबी','fruit','eat',True,
            ['phalgun','chaitra','vaishakh'],['fever','acidity'],['amla','madhur']),
        make_food('नींबू','Lemon','लिंबू','fruit','eat',True,
            ALL,['acidity','fever'],['amla']),
        make_food('आंवला','Indian Gooseberry','आवळा','fruit','eat',True,
            ['ashwin','kartik','margshirsh'],['acidity','diabetes','bp'],['amla','tikta','kashaya']),
        make_food('अमरूद','Guava','पेरू','fruit','eat',False,
            ['ashwin','kartik','margshirsh'],['diabetes','bp'],['madhur','kashaya']),
        make_food('सीताफल','Custard Apple','सीताफळ','fruit','eat',True,
            ['ashwin','kartik'],['acidity'],['madhur']),
        make_food('खीरा','Cucumber','काकडी','fruit','eat',True,
            ['vaishakh','jyeshtha','ashadh'],['bp','diabetes','acidity'],['madhur']),
        make_food('आडू / आलूबुखारा','Peach / Plum','पीच / आलूबुखारा','fruit','eat',False,
            ['chaitra','vaishakh'],['acidity'],['madhur','amla']),
        make_food('लीची','Lychee','लिची','fruit','less_eat',False,
            ['vaishakh','jyeshtha'],['diabetes'],['madhur']),
        make_food('स्ट्रॉबेरी','Strawberry','स्ट्रॉबेरी','fruit','less_eat',False,
            ['phalgun','chaitra'],['diabetes'],['amla','madhur']),
        make_food('अंजीर (काला/पका)','Fig (Black/Ripe)','अंजीर','fruit','eat',True,
            ['margshirsh','paush','magh'],['acidity','diabetes'],['madhur']),
        make_food('ड्रैगन फ्रूट','Dragon Fruit','ड्रॅगन फ्रूट','fruit','eat',False,
            ['ashadh','shravan','bhadrapad'],['diabetes','bp'],['madhur']),
        make_food('खरबूज','Muskmelon','खरबूज','fruit','eat',True,
            ['vaishakh','jyeshtha','ashadh'],['bp','fever'],['madhur']),
        make_food('सफेद फूट / पेठा','Ash Gourd','कोहळा','fruit','eat',False,
            ALL,['acidity','diabetes'],['madhur']),
        make_food('कमरख','Star Fruit','कमरख','fruit','eat',False,
            ['ashwin','kartik'],['acidity'],['amla']),
        make_food('शेवफल / सागरगोटा','Wood Apple','कवठ','fruit','eat',False,
            ['ashwin','kartik'],['acidity'],['amla','kashaya']),
        make_food('केला (हरा/कच्चा)','Raw / Green Banana','कच्चा केळा','fruit','eat',True,
            ALL,['acidity','diabetes'],['kashaya','madhur']),
        make_food('बेर','Indian Jujube','बोर','fruit','eat',True,
            ['margshirsh','paush','magh'],['acidity','fever'],['madhur','amla']),

        # ================================================================
        # VEGETABLES (सब्जी) — Image 6
        # ================================================================
        make_food('लौकी','Bottle Gourd','दुधी भोपळा','vegetable','eat',False,
            ['ashadh','shravan','bhadrapad'],['bp','diabetes','acidity'],['madhur']),
        make_food('करेला','Bitter Gourd','कारलं','vegetable','eat',False,
            ['ashadh','shravan'],['diabetes','fever'],['tikta']),
        make_food('आलू','Potato','बटाटा','vegetable','less_eat',True,
            ALL,['diabetes'],['madhur']),
        make_food('टमाटर','Tomato','टोमॅटो','vegetable','less_eat',False,
            ['phalgun','chaitra','vaishakh'],['acidity'],['amla']),
        make_food('गाजर','Carrot','गाजर','vegetable','eat',True,
            ['margshirsh','paush','magh'],['diabetes','bp'],['madhur']),
        make_food('कद्दू','Pumpkin','भोपळा','vegetable','eat',True,
            ['shravan','bhadrapad','ashwin'],['diabetes','acidity'],['madhur']),
        make_food('बैंगन','Brinjal','वांगं','vegetable','dont_eat',False,
            ['shravan'],['acidity','bp'],['tikta','katu']),
        make_food('टिंडा','Round Gourd','टिंडा','vegetable','eat',False,
            ['ashadh','shravan','bhadrapad'],['bp','diabetes'],['madhur']),
        make_food('परवल','Pointed Gourd','परवल','vegetable','eat',False,
            ['ashadh','shravan'],['diabetes','acidity'],['madhur','tikta']),
        make_food('कुंदरू','Ivy Gourd','तोंडली','vegetable','eat',False,
            ['ashadh','shravan','bhadrapad'],['diabetes'],['madhur']),
        make_food('अरबी / कचालू','Taro Root','अरबी','vegetable','less_eat',False,
            ['shravan','bhadrapad'],['acidity'],['kashaya','madhur']),
        make_food('सेम फली','Flat Beans','वाल पापडी','vegetable','eat',False,
            ['margshirsh','paush','magh'],['diabetes'],['madhur','kashaya']),
        make_food('गवार फली','Cluster Beans','गवार शेंग','vegetable','eat',False,
            ['ashadh','shravan','bhadrapad'],['diabetes','bp'],['tikta','kashaya']),
        make_food('बींस / फ्रेंच बींस','French Beans','फ्रेंच बीन्स','vegetable','eat',False,
            ['margshirsh','paush','magh'],['diabetes','bp'],['madhur']),
        make_food('मूली','Radish','मुळा','vegetable','less_eat',False,
            ['margshirsh','paush','magh','phalgun'],['acidity'],['katu','tikta']),
        make_food('चुकंदर','Beetroot','बीट','vegetable','eat',False,
            ['margshirsh','paush','magh'],['bp','diabetes'],['madhur']),
        make_food('शकरकंद','Sweet Potato','रताळे','vegetable','eat',True,
            ['ashwin','kartik','margshirsh'],['diabetes','acidity'],['madhur']),
        make_food('कच्चा केला (सब्जी)','Raw Banana (Vegetable)','कच्चा केळा (भाजी)','vegetable','eat',True,
            ALL,['acidity','diabetes'],['kashaya','madhur']),
        make_food('कच्चा आम (सब्जी)','Raw Mango (Vegetable)','कच्चा आंबा (भाजी)','vegetable','less_eat',False,
            ['chaitra','vaishakh'],['acidity'],['amla','katu']),
        make_food('फूल गोभी','Cauliflower','फ्लॉवर','vegetable','less_eat',False,
            ['margshirsh','paush','magh','phalgun'],['acidity'],['madhur']),
        make_food('पत्ता गोभी','Cabbage','कोबी','vegetable','less_eat',False,
            ['margshirsh','paush','magh','phalgun'],['acidity'],['madhur']),
        make_food('हरी मिर्च','Green Chilli','हिरवी मिरची','vegetable','less_eat',False,
            ALL,['acidity'],['katu']),
        make_food('शिमला मिर्च','Capsicum','सिमला मिरची','vegetable','eat',False,
            ['phalgun','chaitra','vaishakh'],['diabetes','bp'],['madhur','katu']),
        make_food('भिंडी','Okra / Lady Finger','भेंडी','vegetable','eat',False,
            ['ashadh','shravan','bhadrapad'],['diabetes','acidity'],['madhur','kashaya']),
        make_food('कटहल','Jackfruit','फणस','vegetable','less_eat',False,
            ['chaitra','vaishakh','jyeshtha'],['diabetes'],['madhur']),
        make_food('सहजन (ड्रमस्टिक)','Drumstick','शेवगा','vegetable','eat',False,
            ['chaitra','vaishakh'],['diabetes','bp'],['tikta','katu']),

        # ================================================================
        # LEAFY VEGETABLES (पत्तेदार सब्जी) — Image 6
        # ================================================================
        make_food('पालक','Spinach','पालक','leafy_veg','eat',False,
            ['margshirsh','paush','magh','phalgun'],['bp','diabetes'],['tikta']),
        make_food('मेथी','Fenugreek Leaves','मेथी','leafy_veg','eat',False,
            ['margshirsh','paush','magh'],['diabetes','bp'],['tikta']),
        make_food('पुदीना','Mint','पुदिना','leafy_veg','eat',True,
            ['vaishakh','jyeshtha','ashadh'],['acidity','fever','cold'],['tikta','katu']),
        make_food('चौलाई','Amaranth Leaves','चवळई','leafy_veg','eat',False,
            ['ashadh','shravan','bhadrapad'],['bp','diabetes'],['madhur','tikta']),
        make_food('कड़ी पत्ता','Curry Leaves','कढीपत्ता','leafy_veg','eat',False,
            ALL,['diabetes','acidity'],['tikta','katu']),
        make_food('धनिया पत्ती','Coriander Leaves','कोथिंबीर','leafy_veg','eat',True,
            ALL,['acidity','fever'],['tikta','katu']),
        make_food('सहजन पत्ती','Drumstick Leaves','शेवग्याची पाने','leafy_veg','eat',False,
            ['vaishakh','jyeshtha','ashadh'],['diabetes','bp'],['tikta','katu']),
        make_food('कुल्थी पत्ता','Horse Gram Leaves','कुळीथ पान','leafy_veg','eat',False,
            ['margshirsh','paush','magh'],['bp','diabetes'],['tikta','kashaya']),
        make_food('तुलसी पत्ती','Tulsi Leaves','तुळस पान','leafy_veg','eat',True,
            ALL,['fever','cold','cough'],['tikta','katu']),

        # ================================================================
        # GRAINS (अन्न)
        # ================================================================
        make_food('चावल','Rice','तांदूळ','grain','eat',False,
            ALL,['fever','acidity'],['madhur']),
        make_food('गेहूँ','Wheat','गहू','grain','eat',False,
            ['margshirsh','paush','magh','phalgun'],['diabetes'],['madhur']),
        make_food('साबूदाना','Sabudana','साबुदाणा','grain','eat',True,
            ALL,['acidity'],['madhur']),
        make_food('कुट्टू','Buckwheat','कुट्टू','grain','eat',True,
            ['ashwin','kartik','shravan'],['diabetes','bp'],['tikta','kashaya']),
        make_food('जौ','Barley','जव','grain','eat',False,
            ['phalgun','chaitra'],['diabetes','bp','acidity'],['madhur','kashaya']),
        make_food('मक्का / भुट्टा','Corn / Maize','मका','grain','eat',False,
            ['ashadh','shravan','bhadrapad'],['diabetes'],['madhur']),
        make_food('ज्वार','Sorghum','जोंधळा','grain','eat',False,
            ['vaishakh','jyeshtha','ashadh'],['diabetes','bp'],['madhur','kashaya']),
        make_food('बाजरा','Pearl Millet','बाजरी','grain','eat',False,
            ['margshirsh','paush','magh'],['bp','diabetes'],['madhur','kashaya']),
        make_food('रागी','Finger Millet','नाचणी','grain','eat',False,
            ALL,['diabetes','bp'],['kashaya','madhur']),
        make_food('सिंघाड़ा आटा','Water Chestnut Flour','शिंगाडा पीठ','grain','eat',True,
            ['ashwin','kartik','shravan'],['acidity','diabetes'],['madhur']),
        make_food('राजगिरा','Amaranth Seeds','राजगिरा','grain','eat',True,
            ALL,['acidity','diabetes'],['madhur','kashaya']),

        # ================================================================
        # PULSES (दाल)
        # ================================================================
        make_food('मूंग दाल','Moong Dal','मूग डाळ','pulse','eat',False,
            ALL,['fever','acidity','diabetes'],['madhur']),
        make_food('चना दाल','Chana Dal','चना डाळ','pulse','less_eat',False,
            ['margshirsh','paush','magh'],['diabetes'],['madhur','kashaya']),
        make_food('उड़द दाल','Urad Dal','उडीद डाळ','pulse','dont_eat',False,
            ['ashadh','shravan','bhadrapad'],['bp','acidity'],['madhur']),
        make_food('राजमा','Kidney Beans','राजमा','pulse','less_eat',False,
            ['margshirsh','paush','magh','phalgun'],['bp','diabetes'],['madhur','kashaya']),
        make_food('तुअर / अरहर दाल','Toor Dal','तुरडाळ','pulse','eat',False,
            ALL,['acidity','fever'],['madhur']),
        make_food('मसूर दाल','Masoor Dal','मसूर डाळ','pulse','eat',False,
            ALL,['acidity','fever'],['madhur','amla']),
        make_food('छोले / काबुली चना','Chickpeas','छोले','pulse','less_eat',False,
            ['margshirsh','paush','magh','phalgun'],['diabetes'],['madhur','kashaya']),
        make_food('मूंग (साबुत)','Whole Moong','मूग (साबूत)','pulse','eat',False,
            ALL,['diabetes','acidity'],['madhur','kashaya']),
        make_food('कुल्थी दाल','Horse Gram','कुळीथ','pulse','eat',False,
            ['margshirsh','paush','magh'],['bp','diabetes'],['kashaya','tikta']),
        make_food('मोठ / मटकी','Moth Beans','मटकी','pulse','eat',False,
            ['margshirsh','paush','magh'],['diabetes','acidity'],['madhur','kashaya']),

        # ================================================================
        # DAIRY (डेयरी / दूध उत्पाद) — Image 5 item 11
        # ================================================================
        make_food('दूध','Milk','दूध','dairy','eat',True,
            ALL,['acidity','fever'],['madhur']),
        make_food('दही','Curd / Yogurt','दही','dairy','eat',True,
            ['vaishakh','jyeshtha','ashadh','shravan'],['acidity','diabetes'],['amla','madhur']),
        make_food('घी','Ghee','तूप','dairy','eat',True,
            ['margshirsh','paush','magh'],['acidity'],['madhur']),
        make_food('पनीर','Paneer','पनीर','dairy','less_eat',True,
            ['margshirsh','paush','magh','phalgun'],['diabetes','bp'],['madhur']),
        make_food('छाछ / ताक','Buttermilk','ताक','dairy','eat',True,
            ['vaishakh','jyeshtha','ashadh','chaitra'],['acidity','fever'],['amla','madhur']),
        make_food('मलाई','Cream','साय','dairy','less_eat',False,
            ['margshirsh','paush','magh'],['diabetes','bp'],['madhur']),
        make_food('खोया / मावा','Khoya / Mawa','खवा','dairy','less_eat',False,
            ['margshirsh','paush','magh','phalgun'],['diabetes'],['madhur']),
        make_food('श्रीखंड','Shrikhand','श्रीखंड','dairy','less_eat',False,
            ['vaishakh','jyeshtha'],['diabetes','acidity'],['madhur','amla']),
        make_food('टोन्ड दूध','Toned Milk','टोन्ड दूध','dairy','eat',False,
            ALL,['diabetes','bp'],['madhur']),
        make_food('लस्सी (मीठी)','Sweet Lassi','गोड लस्सी','dairy','less_eat',False,
            ['vaishakh','jyeshtha','ashadh'],['acidity'],['madhur','amla']),
        make_food('लस्सी (नमकीन)','Salty Lassi','खारट लस्सी','dairy','eat',False,
            ['vaishakh','jyeshtha','ashadh'],['acidity','bp'],['lavana','amla']),

        # ================================================================
        # SPICES (मसाला) — Image 5 item 8: लौकतीक, कालीमिर्च, इलायची
        # ================================================================
        make_food('अदरक','Ginger','आलं','spice','eat',True,
            ['margshirsh','paush','magh','phalgun'],['cold','cough','acidity'],['katu']),
        make_food('हल्दी','Turmeric','हळद','spice','eat',True,
            ALL,['fever','cold','cough'],['tikta','katu']),
        make_food('काली मिर्च','Black Pepper','काळी मिरी','spice','eat',True,
            ['margshirsh','paush','magh'],['cold','cough','fever'],['katu']),
        make_food('जीरा','Cumin','जिरे','spice','eat',True,
            ALL,['acidity','diabetes'],['katu','tikta']),
        make_food('सेंधा नमक','Rock Salt','सेंधव मीठ','spice','eat',True,
            ALL,['bp','acidity'],['lavana']),
        make_food('लौंग','Clove','लवंग','spice','eat',True,
            ['margshirsh','paush','magh'],['cold','cough','fever'],['katu','tikta']),
        make_food('इलायची','Cardamom','वेलची','spice','eat',True,
            ALL,['acidity','fever'],['madhur','katu']),
        make_food('दालचीनी','Cinnamon','दालचिनी','spice','eat',False,
            ['margshirsh','paush','magh'],['diabetes','cold'],['madhur','katu']),
        make_food('धनिया (बीज)','Coriander Seeds','धणे','spice','eat',False,
            ALL,['acidity','diabetes'],['tikta','katu']),
        make_food('सौंफ','Fennel Seeds','बडीशेप','spice','eat',True,
            ALL,['acidity','fever'],['madhur']),
        make_food('अजवाइन','Carom Seeds','ओवा','spice','eat',True,
            ALL,['acidity','cold','cough'],['katu','tikta']),
        make_food('राई / सरसों (बीज)','Mustard Seeds','मोहरी','spice','eat',False,
            ALL,['cold','cough'],['katu','tikta']),
        make_food('मेथी दाना','Fenugreek Seeds','मेथ्याचे दाणे','spice','eat',False,
            ALL,['diabetes','bp'],['tikta','kashaya']),
        make_food('हींग','Asafoetida','हिंग','spice','eat',False,
            ALL,['acidity'],['katu']),
        make_food('तेज पत्ता','Bay Leaf','तमालपत्र','spice','eat',False,
            ALL,['acidity','diabetes'],['katu','tikta']),
        make_food('जायफल','Nutmeg','जायफळ','spice','eat',False,
            ['margshirsh','paush','magh'],['cold','cough'],['katu','madhur']),
        make_food('केसर','Saffron','केशर','spice','eat',True,
            ['margshirsh','paush','magh'],['fever','acidity'],['madhur']),
        make_food('सामान्य नमक','Common Salt','सामान्य मीठ','spice','less_eat',False,
            ALL,['bp','acidity'],['lavana']),
        make_food('लाल मिर्च','Red Chilli','लाल मिरची','spice','dont_eat',False,
            ALL,['acidity'],['katu']),
        make_food('गर्म मसाला','Garam Masala','गरम मसाला','spice','less_eat',False,
            ALL,['acidity'],['katu','tikta']),

        # ================================================================
        # DRY FRUITS (सूखे मेवे) — Image 6 (comprehensive list)
        # ================================================================
        make_food('बादाम','Almonds','बदाम','dry_fruit','eat',True,
            ['margshirsh','paush','magh','phalgun'],['diabetes','bp'],['madhur','tikta']),
        make_food('अखरोट','Walnuts','अक्रोड','dry_fruit','eat',True,
            ['margshirsh','paush','magh'],['bp','diabetes'],['tikta','madhur']),
        make_food('किशमिश','Raisins','मनुका','dry_fruit','less_eat',True,
            ['margshirsh','paush','magh','phalgun'],['acidity','diabetes'],['madhur']),
        make_food('खजूर','Dates','खजूर','dry_fruit','less_eat',True,
            ['margshirsh','paush','magh'],['acidity'],['madhur']),
        make_food('काजू','Cashews','काजू','dry_fruit','less_eat',True,
            ['margshirsh','paush','magh','phalgun'],['diabetes','bp'],['madhur']),
        make_food('पिस्ता','Pistachios','पिस्ता','dry_fruit','less_eat',True,
            ['margshirsh','paush','magh'],['diabetes','bp'],['madhur','tikta']),
        make_food('मुनक्का','Large Raisins','मोठे मनुके','dry_fruit','eat',True,
            ['margshirsh','paush','magh','phalgun'],['acidity','fever'],['madhur']),
        make_food('छुहारा','Dried Dates','सुके खजूर','dry_fruit','eat',True,
            ['margshirsh','paush','magh'],['acidity','fever'],['madhur']),
        make_food('अंजीर (सूखा)','Dried Fig','सुके अंजीर','dry_fruit','eat',True,
            ['margshirsh','paush','magh','phalgun'],['acidity','diabetes'],['madhur']),
        make_food('चिरोंजी','Chironji','चारोळी','dry_fruit','eat',True,
            ['margshirsh','paush','magh'],['acidity'],['madhur']),
        make_food('मखाना','Fox Nuts / Lotus Seeds','मखाना','dry_fruit','eat',True,
            ALL,['acidity','diabetes'],['madhur','kashaya']),
        make_food('नारियल (कच्चा)','Fresh Coconut','ओले खोबरे','dry_fruit','eat',True,
            ['vaishakh','jyeshtha','ashadh'],['acidity','bp'],['madhur']),
        make_food('नारियल (सूखा)','Dry Coconut','सुके खोबरे','dry_fruit','less_eat',False,
            ['margshirsh','paush','magh'],['bp'],['madhur','tikta']),
        make_food('खुबानी (एप्रीकॉट)','Apricot','जर्दाळू','dry_fruit','eat',True,
            ['margshirsh','paush','magh'],['acidity','fever'],['madhur','amla']),
        make_food('तिल (सफेद)','White Sesame Seeds','पांढरे तीळ','dry_fruit','eat',True,
            ['margshirsh','paush','magh'],['bp'],['madhur','tikta']),
        make_food('तिल (काला)','Black Sesame Seeds','काळे तीळ','dry_fruit','eat',False,
            ['margshirsh','paush','magh'],['bp','diabetes'],['tikta','madhur']),
        make_food('खरबूज बीज','Muskmelon Seeds','खरबूज बी','dry_fruit','eat',False,
            ['vaishakh','jyeshtha','ashadh'],['bp'],['madhur']),
        make_food('सूरजमुखी बीज','Sunflower Seeds','सूर्यफूल बी','dry_fruit','eat',False,
            ALL,['bp','diabetes'],['madhur']),
        make_food('खसखस','Poppy Seeds','खसखस','dry_fruit','eat',False,
            ['margshirsh','paush','magh'],['acidity'],['madhur']),
        make_food('गुंडा / लसोड़ा','Cordia / Gunda','गोंडा','dry_fruit','eat',False,
            ['margshirsh','paush','magh'],['acidity'],['madhur','kashaya']),

        # ================================================================
        # OILS (तेल / चिकनाई) — Image 5 item 10
        # ================================================================
        make_food('नारियल तेल','Coconut Oil','नारळ तेल','oil','eat',True,
            ['vaishakh','jyeshtha','ashadh'],['acidity','diabetes'],['madhur']),
        make_food('तिल का तेल','Sesame Oil','तिळाचे तेल','oil','eat',False,
            ['margshirsh','paush','magh'],['bp'],['madhur','tikta']),
        make_food('सरसों का तेल','Mustard Oil','मोहरीचे तेल','oil','less_eat',False,
            ['margshirsh','paush','magh'],['cold','cough'],['katu']),
        make_food('मूंगफली तेल','Groundnut Oil','शेंगदाण्याचे तेल','oil','less_eat',False,
            ALL,['diabetes','bp'],['madhur']),
        make_food('गाय का घी','Cow Ghee (Pure)','गाईचे तूप','oil','eat',True,
            ALL,['acidity'],['madhur']),

        # ================================================================
        # SWEETENERS (मीठा) — Image 5 item 14
        # ================================================================
        make_food('गुड़','Jaggery','गूळ','sweetener','eat',True,
            ['margshirsh','paush','magh','phalgun'],['acidity','fever'],['madhur']),
        make_food('शहद','Honey','मध','sweetener','eat',True,
            ALL,['cold','cough','fever'],['madhur']),
        make_food('चीनी','Sugar','साखर','sweetener','less_eat',True,
            ALL,['diabetes','bp','acidity'],['madhur']),
        make_food('मिश्री','Rock Sugar / Mishri','खडीसाखर','sweetener','eat',True,
            ALL,['acidity','fever'],['madhur']),
        make_food('नारियल शक्कर','Coconut Sugar','नारळ साखर','sweetener','less_eat',False,
            ALL,['diabetes'],['madhur']),

        # ================================================================
        # BEVERAGES (पेय)
        # ================================================================
        make_food('हरी चाय','Green Tea','हिरवा चहा','beverage','eat',False,
            ['margshirsh','paush','magh','phalgun'],['diabetes','bp'],['tikta','kashaya']),
        make_food('नारियल पानी','Coconut Water','नारळ पाणी','beverage','eat',True,
            ['vaishakh','jyeshtha','ashadh','chaitra'],['bp','fever','acidity'],['madhur']),
        make_food('नींबू पानी','Lemon Water','लिंबू पाणी','beverage','eat',True,
            ['vaishakh','jyeshtha','ashadh'],['fever','acidity'],['amla','madhur']),
        make_food('आम का पना','Raw Mango Drink','कैरीचे पन्हे','beverage','eat',True,
            ['vaishakh','jyeshtha'],['fever','acidity'],['amla','madhur']),
        make_food('गर्म दूध','Warm Milk','गरम दूध','beverage','eat',True,
            ALL,['acidity','fever'],['madhur']),
        make_food('हर्बल काढ़ा','Herbal Kadha','हर्बल काढा','beverage','eat',True,
            ALL,['fever','cold','cough'],['tikta','katu']),
        make_food('जौ का पानी','Barley Water','जवाचे पाणी','beverage','eat',False,
            ['phalgun','chaitra','vaishakh'],['bp','diabetes','fever'],['madhur','kashaya']),

        # ================================================================
        # FRUIT JUICE (फलों का रस)
        # ================================================================
        make_food('आंवला रस','Amla Juice','आवळा रस','fruit_juice','eat',True,
            ['ashwin','kartik','margshirsh'],['acidity','diabetes','bp'],['amla','tikta']),
        make_food('अनार रस','Pomegranate Juice','डाळिंब रस','fruit_juice','eat',True,
            ['ashwin','kartik','shravan'],['bp','diabetes','fever'],['madhur','amla']),
        make_food('अदरक रस','Ginger Juice','आलं रस','fruit_juice','eat',True,
            ['margshirsh','paush','magh'],['cold','cough','acidity'],['katu']),
        make_food('तुलसी रस','Tulsi Juice','तुळस रस','fruit_juice','eat',True,
            ALL,['fever','cold','cough'],['tikta','katu']),
        make_food('करेला रस','Bitter Gourd Juice','कारले रस','fruit_juice','eat',False,
            ['ashadh','shravan'],['diabetes'],['tikta']),
        make_food('लौकी रस','Bottle Gourd Juice','दुधी रस','fruit_juice','eat',False,
            ['ashadh','shravan','bhadrapad'],['bp','diabetes'],['madhur']),
        make_food('गाजर रस','Carrot Juice','गाजर रस','fruit_juice','eat',False,
            ['margshirsh','paush','magh'],['diabetes','bp'],['madhur']),
        make_food('आंवला-अदरक रस','Amla Ginger Juice','आवळा-आलं रस','fruit_juice','eat',True,
            ['ashwin','kartik','margshirsh'],['acidity','cold','cough'],['amla','katu']),

        # ================================================================
        # SOUP (सूप) — NEW — Image 5 item 9
        # ================================================================
        make_food('मूंग सूप','Moong Soup','मूग सूप','soup','eat',True,
            ALL,['fever','acidity','diabetes'],['madhur']),
        make_food('लौकी सूप','Bottle Gourd Soup','दुधी सूप','soup','eat',False,
            ['ashadh','shravan','bhadrapad'],['bp','diabetes','acidity'],['madhur']),
        make_food('सब्जी सूप','Vegetable Soup','भाजी सूप','soup','eat',False,
            ALL,['fever','acidity'],['madhur','lavana']),
        make_food('टमाटर सूप','Tomato Soup','टोमॅटो सूप','soup','less_eat',False,
            ['phalgun','chaitra','vaishakh'],['acidity'],['amla','lavana']),
        make_food('अदरक सूप','Ginger Soup','आलं सूप','soup','eat',True,
            ['margshirsh','paush','magh'],['cold','cough','fever'],['katu']),
        make_food('सेंडमलनी सूप','Mixed Vegetable Soup','मिक्स भाजी सूप','soup','eat',False,
            ALL,['acidity','fever'],['madhur','lavana']),

        # ================================================================
        # ROTI / BREAD (रोटी) — NEW — Image 5 item 12
        # ================================================================
        make_food('गेहूँ की रोटी / फुलका','Wheat Roti / Phulka','गव्हाची रोटी','roti','eat',False,
            ['margshirsh','paush','magh','phalgun'],['diabetes'],['madhur']),
        make_food('ज्वार की रोटी (भाकरी)','Jowar Roti','ज्वारीची भाकरी','roti','eat',False,
            ['vaishakh','jyeshtha','ashadh'],['diabetes','bp'],['madhur','kashaya']),
        make_food('बाजरे की रोटी (भाकरी)','Bajra Roti','बाजरीची भाकरी','roti','eat',False,
            ['margshirsh','paush','magh'],['bp','diabetes'],['madhur','kashaya']),
        make_food('चावल की रोटी','Rice Roti','तांदळाची भाकरी','roti','eat',False,
            ALL,['fever','acidity'],['madhur']),
        make_food('मक्के की रोटी','Maize Roti','मक्याची भाकरी','roti','eat',False,
            ['ashadh','shravan','bhadrapad'],['diabetes'],['madhur']),
        make_food('पराठा (बिना उड़द)','Paratha (without Urad)','पराठा','roti','less_eat',False,
            ['margshirsh','paush','magh','phalgun'],['diabetes'],['madhur']),
        make_food('पूरी','Puri','पुरी','roti','less_eat',False,
            ALL,['diabetes','acidity'],['madhur']),
        make_food('दोसा','Dosa','दोसा','roti','less_eat',False,
            ALL,['diabetes','acidity'],['amla','madhur']),
        make_food('उत्तपा','Uttapa','उत्तपा','roti','less_eat',False,
            ALL,['acidity'],['amla','madhur']),
        make_food('राजगिरा रोटी','Amaranth Roti','राजगिऱ्याची रोटी','roti','eat',True,
            ALL,['acidity','diabetes'],['madhur','kashaya']),
        make_food('बेसन चिल्ला','Besan Chilla','बेसन चिल्ला','roti','eat',False,
            ALL,['diabetes','acidity'],['madhur','kashaya']),

        # ================================================================
        # NASHTA / SNACKS (नाश्ता) — NEW — Image 5 item 13
        # ================================================================
        make_food('साबूदाना खिचड़ी','Sabudana Khichdi','साबुदाणा खिचडी','nashta','eat',True,
            ALL,['acidity'],['madhur','lavana']),
        make_food('पोहा','Poha','पोहे','nashta','eat',False,
            ALL,['acidity','fever'],['madhur','lavana']),
        make_food('उपमा','Upma','उपमा','nashta','eat',False,
            ALL,['acidity'],['madhur','lavana']),
        make_food('मखाना भुना','Roasted Fox Nuts','भाजलेला मखाना','nashta','eat',True,
            ALL,['acidity','diabetes'],['madhur','kashaya']),
        make_food('मूंगफली (भुनी)','Roasted Peanuts','भाजलेले शेंगदाणे','nashta','eat',False,
            ['margshirsh','paush','magh','phalgun'],['diabetes','bp'],['madhur','kashaya']),
        make_food('इडली','Idli','इडली','nashta','eat',False,
            ALL,['acidity','fever'],['madhur','amla']),
        make_food('ढोकला','Dhokla','ढोकळा','nashta','eat',False,
            ALL,['acidity'],['amla','madhur']),
        make_food('चिवड़ा','Chivda','चिवडा','nashta','less_eat',False,
            ALL,['acidity'],['madhur','lavana','katu']),

        # ================================================================
        # SWEET DISHES (मीठा) — NEW — Image 5 item 14
        # Ayovla murabba, barfi, rasgulla, etc.
        # ================================================================
        make_food('खीर (चावल)','Rice Kheer','तांदळाची खीर','sweet','eat',True,
            ALL,['acidity','fever'],['madhur']),
        make_food('हलवा (गेहूँ / शीरा)','Wheat Halwa / Sheera','कणकेचा शिरा','sweet','less_eat',True,
            ['margshirsh','paush','magh','phalgun'],['acidity'],['madhur']),
        make_food('लड्डू','Laddoo','लाडू','sweet','less_eat',True,
            ['margshirsh','paush','magh','phalgun'],['diabetes'],['madhur']),
        make_food('बर्फी','Barfi','बर्फी','sweet','less_eat',False,
            ['margshirsh','paush','magh'],['diabetes'],['madhur']),
        make_food('रसगुल्ला','Rasgulla','रसगुल्ला','sweet','less_eat',False,
            ALL,['diabetes','acidity'],['madhur']),
        make_food('पेड़ा','Peda','पेडा','sweet','less_eat',True,
            ['margshirsh','paush','magh'],['diabetes'],['madhur']),
        make_food('पूरन पोली','Puran Poli','पुरणपोळी','sweet','less_eat',False,
            ['phalgun','chaitra'],['diabetes','acidity'],['madhur']),
        make_food('गुड़ की चिक्की','Jaggery Chikki','गुळाची चिक्की','sweet','less_eat',True,
            ['margshirsh','paush','magh','phalgun'],['acidity'],['madhur']),
        make_food('सूजी हलवा','Sooji Halwa','रव्याचा शिरा','sweet','less_eat',False,
            ALL,['acidity'],['madhur']),
        make_food('मोदक','Modak','मोदक','sweet','less_eat',True,
            ['bhadrapad'],['acidity'],['madhur']),
        make_food('आंवला मुरब्बा','Amla Murabba','आवळा मुरंबा','sweet','eat',True,
            ALL,['acidity','diabetes'],['madhur','amla']),
        make_food('गाजर हलवा','Carrot Halwa','गाजर हलवा','sweet','less_eat',False,
            ['margshirsh','paush','magh'],['diabetes'],['madhur']),
        make_food('लौकी हलवा','Bottle Gourd Halwa','दुधी हलवा','sweet','less_eat',False,
            ['ashadh','shravan','bhadrapad'],['diabetes','acidity'],['madhur']),
        make_food('खांडवी','Khandvi','खांडवी','sweet','eat',False,
            ALL,['acidity','diabetes'],['madhur','amla']),
        make_food('चावल-खाँड-तिल-कुरा','Rice Khanda Til Mixture','तांदूळ-खांड-तीळ','sweet','less_eat',True,
            ['margshirsh','paush','magh'],['acidity'],['madhur','tikta']),
    ]

    for food in sample_foods:
        db.session.add(food)
    db.session.commit()
    print(f"✅ {len(sample_foods)} food items seeded.")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("\n🌿 आयुर्वेदिक आहार — Database Seeder")
        print("=" * 45)
        seed_admin()
        seed_seasons()
        seed_diseases()
        seed_tastes()
        seed_food_types()
        seed_foods()
        print("=" * 45)
        print("✅ All done! You can now run: python app.py\n")