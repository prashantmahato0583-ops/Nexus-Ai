import os
from flask import Flask, render_template_string, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "nexus_secret_key_7903" # Session security ke liye

# --- AAPKA PRIVATE DATA ---
ADMIN_GMAIL = "nexusai119@gmail.com"
ADMIN_PASSWORD = "prashant@123456"
ADMIN_PHONE = "7903530625"

# --- HTML DESIGN ---
HTML_LAYOUT = """
<!DOCTYPE html>
<html>
<head>
    <title>Nexus AI Admin</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #0f172a; color: white; font-family: 'Segoe UI', sans-serif; text-align: center; padding-top: 50px; }
        .box { background: #1e293b; padding: 30px; border-radius: 15px; border: 2px solid #38bdf8; display: inline-block; width: 320px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
        h2 { color: #38bdf8; margin-bottom: 20px; }
        input { display: block; width: 90%; padding: 12px; margin: 15px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; }
        button { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; transition: 0.3s; }
        button:hover { background: #7dd3fc; }
        .link { color: #94a3b8; cursor: pointer; font-size: 13px; display: block; margin-top: 15px; text-decoration: none; }
        .link:hover { color: #38bdf8; }
        .success-msg { color: #4ade80; font-size: 14px; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="box">
        <h2>🛡️ Nexus Admin</h2>
        
        {% if mode == 'login' %}
        <form method="POST" action="/admin_login">
            <input type="email" name="email" placeholder="Gmail" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Unlock Dashboard</button>
        </form>
        <a href="/forgot" class="link">Forgot Password?</a>
        
        {% elif mode == 'forgot' %}
        <p style="font-size: 14px;">Verification code will be sent to:<br><b>+91 {{phone}}</b></p>
        <form method="POST" action="/send_otp">
            <button type="submit">Send OTP via SMS</button>
        </form>
        <a href="/admin" class="link">Back to Login</a>
        
        {% elif mode == 'otp' %}
        <p class="success-msg">OTP Sent successfully!</p>
        <input type="text" placeholder="Enter 6-digit OTP">
        <button onclick="alert('Access Granted! Password is: {{real_pass}}')">Verify OTP</button>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/admin')
def admin_page():
    return render_template_string(HTML_LAYOUT, mode='login', phone=ADMIN_PHONE)

@app.route('/admin_login', methods=['POST'])
def do_login():
    email = request.form.get('email')
    password = request.form.get('password')
    if email == ADMIN_GMAIL and password == ADMIN_PASSWORD:
        return "<h1>Welcome Prashant! Dashboard Loading...</h1>"
    return "<h1>Access Denied! Galat details hain.</h1><a href='/admin'>Try Again</a>"

@app.route('/forgot')
def forgot_page():
    return render_template_string(HTML_LAYOUT, mode='forgot', phone=ADMIN_PHONE)

@app.route('/send_otp', methods=['POST'])
def send_otp():
    # Asli SMS ke liye Twilio use hota hai, abhi hum direct dikha rahe hain
    return render_template_string(HTML_LAYOUT, mode='otp', real_pass=ADMIN_PASSWORD)

@app.route('/')
def user_home():
    return "<h1>Nexus AI User Portal (Public)</h1><p>Login with Instagram to start bot.</p>"

if __name__ == "__main__":
    app.run(debug=True)
