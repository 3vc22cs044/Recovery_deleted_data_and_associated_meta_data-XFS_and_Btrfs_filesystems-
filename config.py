# config.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Vercel has a read-only filesystem except for /tmp
if os.environ.get('VERCEL'):
    UPLOAD_FOLDER = '/tmp/uploads'
    DB_PATH = '/tmp/files.db'
else:
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static/uploads')
    DB_PATH = os.path.join(BASE_DIR, 'files.db')

SECRET_KEY = os.environ.get('SECRET_KEY', 'replace-this-with-a-secret-key')
ADMIN_PASSWORD = 'admin123'  # change before production
ALLOWED_EXTENSIONS = None  # allow all by default

# ensure folders
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
