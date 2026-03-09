import os
from flask import Flask, render_template_string, request, session, redirect

app = Flask(__name__)
app.secret_key = "nexus_secret_key_7903"

# --- AAPKA PRIVATE DATA ---
ADMIN_GMAIL = "nexusai119@gmail.com"
ADMIN_PASSWORD = "prashant@123456"
ADMIN_PHONE = "7903530625"

# --- COMMON CSS (Dono ke liye) ---
STYLE = """
<style>
    body { background: #0f172a; color: white; font-family: 'Segoe UI', sans-serif; text-align: center; padding-top: 50px; margin: 0; }
    .card { background: #1e293b; display: inline-block; padding: 40px; border-radius: 15px; border: 1px solid #38bdf8; width: 320px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    h2 { color: #38bdf8; margin-bottom: 20px; }
    input { display: block; width: 90%; padding: 12px; margin: 15px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; }
    button { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; transition: 0.3s; }
    button:hover { background: #7dd3fc; }
    .admin-btn { position: fixed; bottom: 20px; right: 20px; background: rgba(56, 189, 248, 0.2); color: #38bdf8; padding: 8px 15px; border-radius: 20px; text-decoration: none; font-size: 12px; border: 1px solid #38bdf8; }
    .admin-btn:hover { background: #38bdf8; color: #0f172a; }
</style>
"""

# --- USER PORTAL (Main Page) ---
@app.route('/')
def user_home():
    return f"""
    <html>
    <head><title>Nexus AI Portal</title>{STYLE}</head>
    <body>
        <div class="card">
            <h2>🚀 Nexus AI Portal</h2>
            <input type="text" placeholder="Instagram ID">
            <input type="password" placeholder="Password">
            <button onclick="alert('Redirecting to Payment...')">Login & Pay ₹99</button>
        </div>
        <a href="/admin" class="admin-btn">🛡️ Admin Login</a>
    </body>
    </html>
    """

# --- ADMIN PANEL ---
@app.route('/admin')
def admin_page():
    return f"""
    <html>
    <head><title>Admin Access</title>{STYLE}</head>
    <body>
        <div class="card">
            <h2>🛡️ Admin Login</h2>
            <form method="POST" action="/admin_login">
                <input type="email" name="email" placeholder="Admin Gmail" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Unlock Dashboard</button>
            </form>
            <a href="/" style="color:#94a3b8; font-size:12px; display:block; margin-top:10px;">Back to User Portal</a>
        </div>
    </body>
    </html>
    """

@app.route('/admin_login', methods=['POST'])
def do_login():
    email = request.form.get('email')
    pw = request.form.get('password')
    if email == ADMIN_GMAIL and pw == ADMIN_PASSWORD:
        return "<h1>Welcome Prashant! Control Panel Opening...</h1>"
    return "<h1>Invalid Credentials!</h1><a href='/admin'>Try Again</a>"

if __name__ == "__main__":
    app.run(debug=True)
