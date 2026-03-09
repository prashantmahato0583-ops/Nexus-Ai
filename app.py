from flask import Flask, render_template_string, request, session, redirect

app = Flask(__name__)
app.secret_key = "nexus_ultra_secure_99"

# --- DATABASE (Fake for now) ---
users_db = {} # Yahan users ka data save hoga
ADMIN_DATA = {"email": "nexusai119@gmail.com", "pass": "prashant@123456"}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Nexus AI Official</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }
        .card { background: #1e293b; display: inline-block; padding: 30px; border-radius: 15px; border: 2px solid #38bdf8; width: 320px; }
        input { display: block; width: 90%; padding: 12px; margin: 10px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; }
        button { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; margin-top: 10px; }
        .toggle-link { color: #38bdf8; font-size: 12px; cursor: pointer; text-decoration: underline; display: block; margin-top: 15px; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div class="card">
        <div id="authBox">
            <h2 id="authTitle">Nexus Sign Up</h2>
            <input type="text" id="uName" placeholder="Full Name">
            <input type="email" id="uEmail" placeholder="Email Address">
            <input type="password" id="uPass" placeholder="Create Password">
            <button onclick="handleAuth()">Submit</button>
            <p class="toggle-link" onclick="toggleAuth()">Already have an account? Login</p>
        </div>

        <div id="portalBox" class="hidden">
            <h2 style="color:#38bdf8;">🚀 Nexus AI Portal</h2>
            <p style="font-size:12px;">Welcome to Automation World</p>
            <input type="text" placeholder="Instagram ID">
            <input type="password" placeholder="Instagram Password">
            <button onclick="alert('Redirecting to Payment Gateway...')">Login & Pay ₹99</button>
        </div>
    </div>

    <button style="position:fixed; bottom:10px; right:10px; width:auto; font-size:10px; padding:5px 10px;" onclick="location.href='/admin'">🛡️ Admin</button>

    <script>
        let isLogin = false;
        function toggleAuth() {
            isLogin = !isLogin;
            document.getElementById('authTitle').innerText = isLogin ? "Nexus Login" : "Nexus Sign Up";
            document.getElementById('uName').style.display = isLogin ? "none" : "block";
        }
        function handleAuth() {
            // Abhi ke liye hum direct andar bhej rahe hain
            alert(isLogin ? "Login Successful!" : "Account Created!");
            document.getElementById('authBox').classList.add('hidden');
            document.getElementById('portalBox').classList.remove('hidden');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/admin')
def admin():
    return f"<h1>Admin Panel for {ADMIN_DATA['email']}</h1><p>Check Users List Here.</p>"

if __name__ == "__main__":
    app.run(debug=True)
