# 🍃 Ayurvedic Food Guidance System

A Flask-based Ayurvedic food recommendation system with multilingual support (Hindi, English, Marathi).

---

## Local Development

```bash
pip install -r requirements.txt
python load_data.py   # seed DB once
python app.py
```

Visit: http://localhost:5000  
Admin: http://localhost:5000/admin/ (username: admin / password: admin123)

---

```bash
python load_data.py
```

This creates the admin user and seeds all food/season/disease data.

---

## Project Structure

```
ayurvedic_food/
├── app.py                  # Flask app + routes + models
├── load_data.py            # One-time DB seed script
├── requirements.txt        # Python dependencies
├── Procfile                # Railway/Heroku start command
├── runtime.txt             # Python version pin
├── static/
│   ├── css/
│   │   ├── base.css        # Shared reset & font (loaded once via base.html)
│   │   ├── index.css
│   │   ├── recommendations.css
│   │   ├── admin_login.css
│   │   └── tabs/
│   └── js/
│       ├── index.js
│       ├── recommendations.js
│       └── tabs/
└── templates/
    ├── base.html           # Jinja2 layout
    ├── index.html
    ├── recommendations.html
    ├── admin_login.html
    └── tabs/
```