# ========================================================================
# load_data.py — Seed the database with reference + sample food data
# ========================================================================
# Run once after setting up the database:
#   python load_data.py
#
# Safe to re-run — skips any data that already exists.
# ========================================================================

from app import app, db
from app import Season, Disease, Taste, FoodType, FoodItem, AdminUser, HealthyCombination, HarmfulCombination
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




def seed_healthy_combinations():
    if HealthyCombination.query.first():
        print("⏭️  Healthy combinations already seeded, skipping.")
        return

    def hc(group_num, group_hi, group_en, group_mr,
           sub_hi, sub_en, sub_mr,
           when_hi, when_en, when_mr,
           with_hi, with_en, with_mr,
           after_hi, after_en, after_mr,
           order=0):
        return HealthyCombination(
            group_number=group_num,
            group_name_hi=group_hi, group_name_en=group_en, group_name_mr=group_mr,
            sub_group_hi=sub_hi,   sub_group_en=sub_en,   sub_group_mr=sub_mr,
            when_hi=when_hi,       when_en=when_en,       when_mr=when_mr,
            with_items_hi=with_hi, with_items_en=with_en, with_items_mr=with_mr,
            after_items_hi=after_hi, after_items_en=after_en, after_items_mr=after_mr,
            display_order=order
        )

    # ── Group 1: रोटी / पराठा / पूरी / रोटी पोहा / बाटी / बाफला ──
    g1_name_hi = 'रोटी / पराठा / पूरी / रोटी पोहा / बाटी / बाफला'
    g1_name_en = 'Roti / Paratha / Puri / Roti Poha / Bati / Bafla'
    g1_name_mr = 'रोटी / पराठा / पुरी / रोटी पोहा / बाटी / बाफला'
    combos = [
        hc(1, g1_name_hi, g1_name_en, g1_name_mr,
           'सब्जी + दाल', 'Sabzi + Dal', 'भाजी + डाळ',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'सब्जी + दाल + सलाद + लौजी + अचार + चटनी + फल + नमकीन',
           'Sabzi + Dal + Salad + Lauji + Pickle + Chutney + Fruit + Namkeen',
           'भाजी + डाळ + सलाद + लौजी + लोणचे + चटणी + फळ + नमकीन',
           'जल', 'Water', 'पाणी', 1),
        hc(1, g1_name_hi, g1_name_en, g1_name_mr,
           'सब्जी (बिना दाल)', 'Sabzi (without Dal)', 'भाजी (डाळाशिवाय)',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'सब्जी + सलाद + लौजी + अचार + चटनी + फल + नमकीन',
           'Sabzi + Salad + Lauji + Pickle + Chutney + Fruit + Namkeen',
           'भाजी + सलाद + लौजी + लोणचे + चटणी + फळ + नमकीन',
           'रस / जूस', 'Juice', 'रस / ज्यूस', 2),
        hc(1, g1_name_hi, g1_name_en, g1_name_mr,
           'सब्जी + कढ़ी', 'Sabzi + Kadhi', 'भाजी + कढी',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'सब्जी + कढ़ी + सलाद + अचार + चटनी + नमकीन',
           'Sabzi + Kadhi + Salad + Pickle + Chutney + Namkeen',
           'भाजी + कढी + सलाद + लोणचे + चटणी + नमकीन',
           'छाछ', 'Buttermilk', 'ताक', 3),
        hc(1, g1_name_hi, g1_name_en, g1_name_mr,
           'सब्जी + छाछ', 'Sabzi + Buttermilk', 'भाजी + ताक',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'सब्जी + छाछ + सलाद + चटनी + नमकीन',
           'Sabzi + Buttermilk + Salad + Chutney + Namkeen',
           'भाजी + ताक + सलाद + चटणी + नमकीन',
           'अन्य तरल पदार्थ', 'Other Liquids', 'इतर तरल पदार्थ', 4),
        hc(1, g1_name_hi, g1_name_en, g1_name_mr,
           'सब्जी + रायता', 'Sabzi + Raita', 'भाजी + रायता',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'सब्जी + रायता + नमकीन',
           'Sabzi + Raita + Namkeen',
           'भाजी + रायता + नमकीन',
           'अन्य तरल पदार्थ', 'Other Liquids', 'इतर तरल पदार्थ', 5),
        hc(1, g1_name_hi, g1_name_en, g1_name_mr,
           'दूध', 'Milk', 'दूध',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'दूध', 'Milk', 'दूध',
           'जल / मीठा / सूखा मेवा', 'Water / Sweet / Dry Fruit', 'पाणी / गोड / सुका मेवा', 6),
        hc(1, g1_name_hi, g1_name_en, g1_name_mr,
           'मीठा (दूध वाला)', 'Sweet (Milk-based)', 'गोड (दुधाचे)',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'मीठा - दूध वाला', 'Milk-based Sweet', 'दुधाचे गोड',
           'दूध', 'Milk', 'दूध', 7),
        hc(1, g1_name_hi, g1_name_en, g1_name_mr,
           'मीठा (चाशनी वाला)', 'Sweet (Syrup-based)', 'गोड (चाशनीचे)',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'मीठा - चाशनी वाला', 'Syrup-based Sweet', 'चाशनीचे गोड',
           'दूध', 'Milk', 'दूध', 8),
        hc(1, g1_name_hi, g1_name_en, g1_name_mr,
           'फल', 'Fruit', 'फळ',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'फल', 'Fruit', 'फळ',
           '', '', '', 9),
    ]

    # ── Group 2: चीला ──
    combos += [
        hc(2, 'चीला', 'Chilla', 'चीला',
           '', '', '',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'सलाद + अचार + चटनी + नमकीन',
           'Salad + Pickle + Chutney + Namkeen',
           'सलाद + लोणचे + चटणी + नमकीन',
           'नींबू पानी, कोकम', 'Lemon Water, Kokum', 'लिंबू पाणी, कोकम', 20),
    ]

    # ── Group 3: चावल ──
    g3_hi = 'चावल'; g3_en = 'Rice'; g3_mr = 'तांदूळ'
    combos += [
        hc(3, g3_hi, g3_en, g3_mr,
           'सादा चावल', 'Plain Rice', 'सादे तांदूळ',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'घृत + नमक + जीरा\nघृत + बूरा + काली मिर्च\nदूध\nमीठा - दूध वाला\nमीठा - चाशनी वाला\nफल, आम रस',
           'Ghee + Salt + Cumin\nGhee + Sugar + Black Pepper\nMilk\nMilk-based Sweet\nSyrup-based Sweet\nFruit, Mango Juice',
           'तूप + मीठ + जिरे\nतूप + साखर + मिरे\nदूध\nदुधाचे गोड\nचाशनीचे गोड\nफळ, आंब्याचा रस',
           'अन्य तरल पदार्थ', 'Other Liquids', 'इतर तरल पदार्थ', 30),
        hc(3, g3_hi, g3_en, g3_mr,
           'मसाला चावल / खिचड़ी', 'Masala Rice / Khichdi', 'मसाला तांदूळ / खिचडी',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'सब्जी + दाल + सलाद + लौजी + अचार + चटनी + फल + नमकीन\nसब्जी + सलाद + लौजी + अचार + चटनी + फल + नमकीन\nसब्जी + कढ़ी + सलाद + अचार + चटनी + नमकीन\nसब्जी + छाछ + सलाद + चटनी + नमकीन\nसब्जी + रायता + नमकीन',
           'Sabzi+Dal+Salad+Lauji+Pickle+Chutney+Fruit+Namkeen\nSabzi+Salad+Lauji+Pickle+Chutney+Fruit+Namkeen\nSabzi+Kadhi+Salad+Pickle+Chutney+Namkeen\nSabzi+Buttermilk+Salad+Chutney+Namkeen\nSabzi+Raita+Namkeen',
           'भाजी+डाळ+सलाद+लौजी+लोणचे+चटणी+फळ+नमकीन\nभाजी+सलाद+लौजी+लोणचे+चटणी+फळ+नमकीन\nभाजी+कढी+सलाद+लोणचे+चटणी+नमकीन\nभाजी+ताक+सलाद+चटणी+नमकीन\nभाजी+रायता+नमकीन',
           'बिना तला नमकीन', 'Non-fried Namkeen', 'बिनतळलेले नमकीन', 31),
    ]

    # ── Group 4: दलिया ──
    g4_hi = 'दलिया'; g4_en = 'Daliya'; g4_mr = 'दलिया'
    combos += [
        hc(4, g4_hi, g4_en, g4_mr,
           'सादा', 'Plain', 'सादे',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'दूध / छाछ\nमीठा दूध',
           'Milk / Buttermilk\nMilk-based Sweet',
           'दूध / ताक\nदुधाचे गोड',
           'बिना तला नमकीन', 'Non-fried Namkeen', 'बिनतळलेले नमकीन', 40),
        hc(4, g4_hi, g4_en, g4_mr,
           'नमकीन दलिया', 'Namkeen Daliya', 'नमकीन दलिया',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'सब्जी + सलाद + लौजी + अचार + चटनी + फल + नमकीन\nसब्जी + कढ़ी + सलाद + अचार + चटनी + नमकीन\nसब्जी + छाछ + सलाद + चटनी + नमकीन',
           'Sabzi+Salad+Lauji+Pickle+Chutney+Fruit+Namkeen\nSabzi+Kadhi+Salad+Pickle+Chutney+Namkeen\nSabzi+Buttermilk+Salad+Chutney+Namkeen',
           'भाजी+सलाद+लौजी+लोणचे+चटणी+फळ+नमकीन\nभाजी+कढी+सलाद+लोणचे+चटणी+नमकीन\nभाजी+ताक+सलाद+चटणी+नमकीन',
           'नारियल पानी', 'Coconut Water', 'नारळ पाणी', 41),
        hc(4, g4_hi, g4_en, g4_mr,
           'महेरी', 'Maheri', 'महेरी',
           '', '', '',
           'कढ़ी - छाछ\nछाछ (औषधि)\nसब्जी',
           'Kadhi - Buttermilk\nMedicinal Buttermilk\nSabzi',
           'कढी - ताक\nऔषधी ताक\nभाजी',
           'जल\nऔषधि जल\nबिना तला नमकीन', 'Water\nMedicinal Water\nNon-fried Namkeen', 'पाणी\nऔषधी पाणी\nबिनतळलेले नमकीन', 42),
    ]

    # ── Group 5: खींच ──
    combos += [
        hc(5, 'खींच', 'Kheench', 'खींच',
           '', '', '', '', '', '',
           'घृत + घास तले गर्म',
           'Ghee + Warm Fried Grass',
           'तूप + उकडलेले गरम',
           'जल', 'Water', 'पाणी', 50),
    ]

    # ── Group 6: दूध ──
    combos += [
        hc(6, 'दूध', 'Milk', 'दूध',
           'सूखा मेवा + मीठा', 'Dry Fruit + Sweet', 'सुका मेवा + गोड',
           'प्रारम्भ / मध्य / अंत', 'Start / Middle / End', 'सुरुवात / मध्य / शेवट',
           'सूखा मेवा + मीठा दूध वाला\nसूखा मेवा + मीठा चाशनी वाला (दाल छोड़कर)\nरोटी, पराठा, पूरी\nघृत',
           'Dry Fruit + Milk-based Sweet\nDry Fruit + Syrup-based Sweet (except dal)\nRoti, Paratha, Puri\nGhee',
           'सुका मेवा + दुधाचे गोड\nसुका मेवा + चाशनीचे गोड (डाळ सोडून)\nरोटी, पराठा, पुरी\nतूप',
           'जल\nबिना तला नमकीन', 'Water\nNon-fried Namkeen', 'पाणी\nबिनतळलेले नमकीन', 60),
    ]

    # ── Group 7: दही - छाछ ──
    combos += [
        hc(7, 'दही - छाछ', 'Curd - Buttermilk', 'दही - ताक',
           '', '', '', '', '', '',
           'रोटी - पराठा - पूरी - रोटी पोहा - बाटी बाफला\nचावल - खिचड़ी - दलिया - महेरी\nनमकीन (बिना दाल)',
           'Roti-Paratha-Puri-Roti Poha-Bati Bafla\nRice-Khichdi-Daliya-Maheri\nNamkeen (without Dal)',
           'रोटी-पराठा-पुरी-रोटी पोहा-बाटी बाफला\nतांदूळ-खिचडी-दलिया-महेरी\nनमकीन (डाळाशिवाय)',
           'जल\nअन्य तरल पदार्थ\nबिना तला नमकीन',
           'Water\nOther Liquids\nNon-fried Namkeen',
           'पाणी\nइतर तरल पदार्थ\nबिनतळलेले नमकीन', 70),
    ]

    # ── Group 8: फल ──
    combos += [
        hc(8, 'फल', 'Fruit', 'फळ',
           '', '', '', '', '', '',
           'रोटी - पराठा - पूरी - रोटी पोहा - बाटी बाफला - चावल - खिचड़ी - दलिया\n(एक साथ सभी फल न दें, बीच-२ में 1-1 लाकर देते जाएं)',
           'Roti-Paratha-Puri-Roti Poha-Bati Bafla-Rice-Khichdi-Daliya\n(Avoid giving all fruits at once; serve one by one at intervals)',
           'रोटी-पराठा-पुरी-रोटी पोहा-बाटी बाफला-तांदूळ-खिचडी-दलिया\n(सर्व फळे एकत्र देऊ नका, एक-एक करत द्या)',
           'नारियल पानी', 'Coconut Water', 'नारळ पाणी', 80),
    ]

    # ── Group 9: सत्तू ──
    combos += [
        hc(9, 'सत्तू', 'Sattu', 'सत्तू',
           '', '', '',
           'मध्य', 'Middle', 'मध्य',
           'एक बार में ही पूरा दें, अंतर न करें',
           'Give all at once without pause',
           'एकाच वेळी संपूर्ण द्या, अंतर करू नका',
           'बिना तला नमकीन', 'Non-fried Namkeen', 'बिनतळलेले नमकीन', 90),
    ]

    # ── Group 10: मीठा ──
    combos += [
        hc(10, 'मीठा', 'Sweet', 'गोड',
           '', '', '', '', '', '',
           'रोटी - पराठा - पूरी - रोटी पोहा - बाटी बाफला + सूखा मेवा + दूध',
           'Roti-Paratha-Puri-Roti Poha-Bati Bafla + Dry Fruit + Milk',
           'रोटी-पराठा-पुरी-रोटी पोहा-बाटी बाफला + सुका मेवा + दूध',
           'बिना तला नमकीन', 'Non-fried Namkeen', 'बिनतळलेले नमकीन', 100),
    ]

    # ── Group 11: नमकीन ──
    combos += [
        hc(11, 'नमकीन', 'Namkeen', 'नमकीन',
           '', '', '', '', '', '',
           'रोटी - पराठा - पूरी - रोटी पोहा - बाटी बाफला\n(हर तरल पदार्थ के बाद कुछ चबाने देते जाएं)',
           'Roti-Paratha-Puri-Roti Poha-Bati Bafla\n(After every liquid, give something to chew)',
           'रोटी-पराठा-पुरी-रोटी पोहा-बाटी बाफला\n(प्रत्येक तरल पदार्थानंतर काहीतरी चावण्यासाठी द्या)',
           '', '', '', 110),
    ]

    # ── Group 12: अन्य तरल पदार्थ ──
    combos += [
        hc(12, 'अन्य तरल पदार्थ', 'Other Liquids', 'इतर तरल पदार्थ',
           '', '', '',
           'मध्य', 'Middle', 'मध्य',
           'मध्य में जल के स्थान पर देते जाएं जिससे अंत में सब एक साथ न रह जाए',
           'Give during meal in place of water, so they do not accumulate at the end',
           'जेवणाच्या मध्यभागी पाण्याऐवजी द्या जेणेकरून शेवटी सर्व एकत्र राहणार नाहीत',
           '', '', '', 120),
    ]

    for c in combos:
        db.session.add(c)
    db.session.commit()
    print(f"✅ {len(combos)} healthy combinations seeded.")


def seed_harmful_combinations():
    if HarmfulCombination.query.first():
        print("⏭️  Harmful combinations already seeded, skipping.")
        return

    def hx(group_num, group_hi, group_en, group_mr,
            sub_hi, sub_en, sub_mr,
            avoid_hi, avoid_en, avoid_mr,
            alt_hi, alt_en, alt_mr,
            reason_hi, reason_en, reason_mr,
            order=0):
        return HarmfulCombination(
            group_number=group_num,
            group_name_hi=group_hi, group_name_en=group_en, group_name_mr=group_mr,
            sub_group_hi=sub_hi,    sub_group_en=sub_en,    sub_group_mr=sub_mr,
            avoid_with_hi=avoid_hi, avoid_with_en=avoid_en, avoid_with_mr=avoid_mr,
            alternative_hi=alt_hi,  alternative_en=alt_en,  alternative_mr=alt_mr,
            reason_hi=reason_hi,    reason_en=reason_en,    reason_mr=reason_mr,
            display_order=order
        )

    NA = ''; VIRUDDH = 'विरुद्ध आहार'; VIRUDDH_EN = 'Viruddha Ahara (Incompatible Food)'; VIRUDDH_MR = 'विरुद्ध आहार'
    DWIDAAL = 'द्विदल अंतराय'; DWIDAAL_EN = 'Dwidala Interval (pulse interval needed)'; DWIDAAL_MR = 'द्विदल अंतराय'

    harmful = [
        # 1) चीला
        hx(1,'चीला','Chilla','चीला',
           'सादा','Plain','सादे',
           'दही, छाछ\nसब्जी मिश्रित\nमीठा',
           'Curd, Buttermilk\nMixed Vegetables\nSweet',
           'दही, ताक\nभाजी मिश्रित\nगोड',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 10),

        # 2) दाल
        hx(2,'दाल','Dal','डाळ',
           NA,NA,NA,
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, DWIDAAL+' / '+VIRUDDH, DWIDAAL_EN+' / '+VIRUDDH_EN, DWIDAAL_MR+' / '+VIRUDDH_MR, 20),

        # 3) कढ़ी
        hx(3,'कढ़ी','Kadhi','कढी',
           'हरी सब्जी','Green Vegetable','हिरवी भाजी',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 30),
        hx(3,'कढ़ी','Kadhi','कढी',
           'सूखी सब्जी','Dry Vegetable','सुकी भाजी',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 31),

        # 4) सलाद
        hx(4,'सलाद','Salad','सलाड',
           'हरी सलाद','Green Salad','हिरवे सलाड',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 40),
        hx(4,'सलाद','Salad','सलाड',
           'अनाज सलाद','Grain Salad','धान्य सलाड',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, DWIDAAL,DWIDAAL_EN,DWIDAAL_MR, 41),

        # 5) अचार
        hx(5,'अचार','Pickle','लोणचे',
           NA,NA,NA,
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 50),

        # 6) चटनी
        hx(6,'चटनी','Chutney','चटणी',
           NA,NA,NA,
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 60),

        # 7) रायता
        hx(7,'रायता','Raita','रायता',
           'हरी सब्जी','Green Vegetable','हिरवी भाजी',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 70),
        hx(7,'रायता','Raita','रायता',
           'सूखी सब्जी','Dry Vegetable','सुकी भाजी',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 71),
        hx(7,'रायता','Raita','रायता',
           'छाछ','Buttermilk','ताक',
           'दूध, फल, फलरस, सब्जी रस',
           'Milk, Fruit, Fruit Juice, Vegetable Juice',
           'दूध, फळ, फळाचा रस, भाजीचा रस',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 72),

        # 8) कढ़ी - छाछ
        hx(8,'कढ़ी - छाछ','Kadhi Buttermilk','कढी - ताक',
           NA,NA,NA,
           'दूध, फल, फल रस',
           'Milk, Fruit, Fruit Juice',
           'दूध, फळ, फळाचा रस',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 80),

        # 9) सब्जी
        hx(9,'सब्जी','Vegetable','भाजी',
           'अनाज सब्जी','Grain Vegetable','धान्य भाजी',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 90),
        hx(9,'सब्जी','Vegetable','भाजी',
           'मटर, हरा चना','Peas, Green Gram','मटर, हिरवा चणा',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 91),
        hx(9,'सब्जी','Vegetable','भाजी',
           'हरा ज्वार, मूंग','Green Jowar, Moong','हिरवी ज्वारी, मूग',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 92),
        hx(9,'सब्जी','Vegetable','भाजी',
           'हरा तुअर','Green Tuvar','हिरवी तूर',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 93),
        hx(9,'सब्जी','Vegetable','भाजी',
           'लौजी','Lauji','लौजी',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 94),

        # 10) दलिया
        hx(10,'दलिया','Daliya','दलिया',
           'छाछ (महेरी)','Buttermilk (Maheri)','ताक (महेरी)',
           'दूध व दूध उत्पाद\nफल, फल रस',
           'Milk & Milk Products\nFruit, Fruit Juice',
           'दूध व दूध उत्पाद\nफळ, फळाचा रस',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 100),

        # 11) तरल द्रव्य
        hx(11,'तरल द्रव्य','Liquid Items','तरल पदार्थ',
           'औषधि जल','Medicinal Water','औषधी पाणी',
           'दही, छाछ, दूध',
           'Curd, Buttermilk, Milk',
           'दही, ताक, दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 110),
        hx(11,'तरल द्रव्य','Liquid Items','तरल पदार्थ',
           'ठंडा जल','Cold Water','थंड पाणी',
           'दही, छाछ, दूध, तेज गर्म वस्तु',
           'Curd, Buttermilk, Milk, Very Hot Items',
           'दही, ताक, दूध, खूप गरम पदार्थ',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 111),
        hx(11,'तरल द्रव्य','Liquid Items','तरल पदार्थ',
           'सूप','Soup','सूप',
           'दही, छाछ, दूध, तेज गर्म वस्तु',
           'Curd, Buttermilk, Milk, Very Hot Items',
           'दही, ताक, दूध, खूप गरम पदार्थ',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 112),
        hx(11,'तरल द्रव्य','Liquid Items','तरल पदार्थ',
           'फल रस','Fruit Juice','फळाचा रस',
           'दही, छाछ, दूध\nजल, खटाई, बूरा',
           'Curd, Buttermilk, Milk\nWater, Sour, Powdered Sugar',
           'दही, ताक, दूध\nपाणी, आंबट, बुरा',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 113),
        hx(11,'तरल द्रव्य','Liquid Items','तरल पदार्थ',
           'सब्जी रस','Vegetable Juice','भाजीचा रस',
           'दही, छाछ, दूध\nजल, खटाई',
           'Curd, Buttermilk, Milk\nWater, Sour',
           'दही, ताक, दूध\nपाणी, आंबट',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 114),
        hx(11,'तरल द्रव्य','Liquid Items','तरल पदार्थ',
           'छाछ','Buttermilk','ताक',
           'दही, फलरस, दूध उत्पाद',
           'Curd, Fruit Juice, Milk Products',
           'दही, फळाचा रस, दूध उत्पाद',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 115),
        hx(11,'तरल द्रव्य','Liquid Items','तरल पदार्थ',
           'लापसी','Lapsi','लापशी',
           'दही - छाछ',
           'Curd - Buttermilk',
           'दही - ताक',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 116),
        hx(11,'तरल द्रव्य','Liquid Items','तरल पदार्थ',
           'सत्तू','Sattu','सत्तू',
           'दही, छाछ, दूध, फलरस',
           'Curd, Buttermilk, Milk, Fruit Juice',
           'दही, ताक, दूध, फळाचा रस',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 117),

        # 12) खींच
        hx(12,'खींच','Kheench','खींच',
           NA,NA,NA,
           'दूध',
           'Milk',
           'दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 120),

        # 13) दूध
        hx(13,'दूध','Milk','दूध',
           NA,NA,NA,
           'दही, छाछ, फलरस\nसब्जी रस\nसब्जी (हरी मिर्च, तोरई, सलाद)\nखटाई\nफल (आम छोड़कर सभी)\nमसाला (नमक, लाल मिर्च, गुड़, इमली, गरम मसाला)\nसीड्स (सेंगदाना, तिल, अलसी)\nदाल (सभी)\nखटाई (इमली, अमचूर आदि)\nचिकनाई (तेल)\nनारियल पानी\nसत्तू',
           'Curd, Buttermilk, Fruit Juice\nVegetable Juice\nVegetables (Green Chilli, Ridge Gourd, Salad)\nSour items\nAll Fruits except Mango\nSpices (Salt, Red Chilli, Jaggery, Tamarind, Garam Masala)\nSeeds (Peanut, Sesame, Flaxseed)\nAll Pulses\nSour (Tamarind, Dry Mango Powder)\nFat (Oil)\nCoconut Water\nSattu',
           'दही, ताक, फळाचा रस\nभाजीचा रस\nभाज्या (हिरवी मिरची, दोडका, सलाड)\nआंबट\nआंबा सोडून सर्व फळे\nमसाले (मीठ, लाल मिरची, गूळ, चिंच, गरम मसाला)\nबिया (शेंगदाणे, तीळ, जवस)\nसर्व डाळी\nआंबट (चिंच, आमचूर इ.)\nचिकण पदार्थ (तेल)\nनारळ पाणी\nसत्तू',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 130),

        # 14) फल
        hx(14,'फल','Fruit','फळ',
           NA,NA,NA,
           'दूध, दही, छाछ, जल',
           'Milk, Curd, Buttermilk, Water',
           'दूध, दही, ताक, पाणी',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 140),

        # 15) मीठा
        hx(15,'मीठा','Sweet','गोड',
           'दूध वाला मीठा','Milk-based Sweet','दुधाचे गोड',
           'छाछ, फलरस, खटाई',
           'Buttermilk, Fruit Juice, Sour',
           'ताक, फळाचा रस, आंबट',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 150),
        hx(15,'मीठा','Sweet','गोड',
           'दूध सब्जी','Milk Vegetable','दूध भाजी',
           'फल, जल, सत्तू',
           'Fruit, Water, Sattu',
           'फळ, पाणी, सत्तू',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 151),
        hx(15,'मीठा','Sweet','गोड',
           'दूध अनाज','Milk Grain','दूध धान्य',
           '(विरुद्ध — avoid separately)',
           '(Incompatible combination)',
           '(विरुद्ध — वेगळे टाळा)',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 152),
        hx(15,'मीठा','Sweet','गोड',
           'दूध सूखा मेवा','Milk Dry Fruit','दूध सुका मेवा',
           '(विरुद्ध — avoid separately)',
           '(Incompatible combination)',
           '(विरुद्ध — वेगळे टाळा)',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 153),
        hx(15,'मीठा','Sweet','गोड',
           'दूध फल','Milk Fruit','दूध फळ',
           'फल, जल, सत्तू',
           'Fruit, Water, Sattu',
           'फळ, पाणी, सत्तू',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 154),
        hx(15,'मीठा','Sweet','गोड',
           'चाशनी सब्जी','Syrup Vegetable','चाशनी भाजी',
           'जल', 'Water', 'पाणी',
           NA,NA,NA,
           'सर्दी, गला खराब, कफ','Cold, Sore Throat, Phlegm','सर्दी, घसा बिघडणे, कफ', 155),
        hx(15,'मीठा','Sweet','गोड',
           'चाशनी अनाज (हलवा)','Syrup Grain (Halwa)','चाशनी धान्य (हलवा)',
           'जल', 'Water', 'पाणी',
           NA,NA,NA,
           'सर्दी, गला खराब, कफ','Cold, Sore Throat, Phlegm','सर्दी, घसा बिघडणे, कफ', 156),
        hx(15,'मीठा','Sweet','गोड',
           'चाशनी दाल हलवा','Syrup Dal Halwa','चाशनी डाळ हलवा',
           'दूध, छाछ, फल रस, खटाई',
           'Milk, Buttermilk, Fruit Juice, Sour',
           'दूध, ताक, फळाचा रस, आंबट',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 157),
        hx(15,'मीठा','Sweet','गोड',
           'चाशनी दाल लड्डू','Syrup Dal Laddu','चाशनी डाळ लाडू',
           'दूध, छाछ, फल रस, खटाई',
           'Milk, Buttermilk, Fruit Juice, Sour',
           'दूध, ताक, फळाचा रस, आंबट',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 158),
        hx(15,'मीठा','Sweet','गोड',
           'चाशनी सीड्स लड्डू','Syrup Seeds Laddu','चाशनी बिया लाडू',
           'दूध, छाछ, फल रस, खटाई',
           'Milk, Buttermilk, Fruit Juice, Sour',
           'दूध, ताक, फळाचा रस, आंबट',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 159),
        hx(15,'मीठा','Sweet','गोड',
           'चाशनी पाक','Syrup Pak','चाशनी पाक',
           '(विरुद्ध संयोजन से बचें)',
           '(Avoid incompatible combinations)',
           '(विरुद्ध संयोजन टाळा)',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 160),
        hx(15,'मीठा','Sweet','गोड',
           'अन्य मीठा','Other Sweets','इतर गोड',
           'छाछ, फल रस, खटाई',
           'Buttermilk, Fruit Juice, Sour',
           'ताक, फळाचा रस, आंबट',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 161),

        # 16) नमकीन
        hx(16,'नमकीन','Namkeen','नमकीन',
           'बिना तला दाल','Non-fried Dal','बिनतळलेली डाळ',
           'दही, छाछ, दूध, फल रस',
           'Curd, Buttermilk, Milk, Fruit Juice',
           'दही, ताक, दूध, फळाचा रस',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 161),
        hx(16,'नमकीन','Namkeen','नमकीन',
           'तला अनाज','Fried Grain','तळलेले धान्य',
           'दूध',
           'Milk',
           'दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 162),
        hx(16,'नमकीन','Namkeen','नमकीन',
           'तला हुआ दाल','Fried Dal','तळलेली डाळ',
           'दही, छाछ, दूध, फल रस',
           'Curd, Buttermilk, Milk, Fruit Juice',
           'दही, ताक, दूध, फळाचा रस',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 163),
        hx(16,'नमकीन','Namkeen','नमकीन',
           'तला हुआ सब्जी','Fried Vegetable','तळलेली भाजी',
           'दूध',
           'Milk',
           'दूध',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 164),
        hx(16,'नमकीन','Namkeen','नमकीन',
           'तला सूखा मेवा','Fried Dry Fruit','तळलेला सुका मेवा',
           'दही, छाछ, दूध, फल रस',
           'Curd, Buttermilk, Milk, Fruit Juice',
           'दही, ताक, दूध, फळाचा रस',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 165),
        hx(16,'नमकीन','Namkeen','नमकीन',
           'भजिया','Bhajiya','भजी',
           'दूध, फल रस',
           'Milk, Fruit Juice',
           'दूध, फळाचा रस',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 166),

        # 17) दही - छाछ
        hx(17,'दही - छाछ','Curd - Buttermilk','दही - ताक',
           NA,NA,NA,
           'दूध, फल रस, फल\nखटाई, मीठा\nनारियल पानी\nसीड्स, तैल\nदाल\nगुड़ (इमली पानी)\nपनीर, तेज गर्म वस्तु',
           'Milk, Fruit Juice, Fruit\nSour, Sweet\nCoconut Water\nSeeds, Oil\nPulse\nJaggery (Tamarind Water)\nPaneer, Very Hot items',
           'दूध, फळाचा रस, फळ\nआंबट, गोड\nनारळ पाणी\nबिया, तेल\nडाळ\nगूळ (चिंच पाणी)\nपनीर, अति गरम पदार्थ',
           NA,NA,NA,
           'विरुद्ध आहार / स्वास्थ्य खराब',
           'Viruddha Ahara / Harmful to Health',
           'विरुद्ध आहार / आरोग्य बिघडते', 170),

        # 18) घृत
        hx(18,'घृत','Ghee','तूप',
           NA,NA,NA,
           'खटाई, नींबू',
           'Sour, Lemon',
           'आंबट, लिंबू',
           NA,NA,NA, VIRUDDH,VIRUDDH_EN,VIRUDDH_MR, 180),
    ]

    for h in harmful:
        db.session.add(h)
    db.session.commit()
    print(f"✅ {len(harmful)} harmful combinations seeded.")


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
        seed_healthy_combinations()
        seed_harmful_combinations()
        print("=" * 45)
        print("✅ All done! You can now run: python app.py\n")