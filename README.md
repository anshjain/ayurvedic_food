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

## Deploy to Railway

### Step 1 — Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ayurvedic-food.git
git push -u origin main
```

### Step 2 — Create project on Railway

1. Go to [railway.app](https://railway.app) → **New Project**
2. Choose **Deploy from GitHub repo**
3. Select your repository
4. Railway auto-detects Python via Nixpacks and uses `Procfile` / `railway.json`

### Step 3 — Set Environment Variables

In your Railway service → **Variables** tab, add:

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | A long random string (e.g. generate with `python -c "import secrets; print(secrets.token_hex(32))"`) |
| `FLASK_DEBUG` | `false` |

> Railway automatically injects `PORT` — your app already reads it.

### Step 4 — Generate a public domain

Service → **Settings** → **Networking** → **Generate Domain**  
You'll get a `xxx.up.railway.app` URL.

### Step 5 — Seed the database

After the first deploy, open the Railway **Shell** (service → Shell tab):

```bash
python load_data.py
```

This creates the admin user and seeds all food/season/disease data.

> **Note on SQLite persistence:** Railway's filesystem persists between deploys (unlike Render's free tier), so your SQLite DB survives redeploys. For production scale, add a Railway PostgreSQL plugin and set `DATABASE_URL` to the plugin's connection string.

---

## Project Structure

```
ayurvedic_food/
├── app.py                  # Flask app + routes + models
├── load_data.py            # One-time DB seed script
├── requirements.txt        # Python dependencies
├── Procfile                # Railway/Heroku start command
├── railway.json            # Railway build + deploy config
├── nixpacks.toml           # Nixpacks build config (Python 3.11)
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

---

## Adding a PostgreSQL Database (optional, for production)

1. In Railway project canvas → **New** → **Database** → **PostgreSQL**
2. In your web service → **Variables**, Railway auto-links `DATABASE_URL`
3. Install the driver: add `psycopg2-binary==2.9.9` to `requirements.txt`
4. Push — Railway redeploys automatically
