from flask import Flask, render_template_string

app = Flask(__name__)

# --- DATA ---
ADMIN_GMAIL = "nexusai119@gmail.com"
ADMIN_PASSWORD = "prashant@123456"
ADMIN_PHONE = "7903530625"

HTML_LAYOUT = """
<!DOCTYPE html>
<html>
<head>
    <title>Nexus AI | Secure Access</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #0f172a; color: white; font-family: 'Segoe UI', sans-serif; text-align: center; padding-top: 30px; }
        .container { background: #1e293b; display: inline-block; padding: 25px; border-radius: 20px; border: 2px solid #38bdf8; width: 320px; box-shadow: 0 15px 35px rgba(0,0,0,0.5); }
        .nav-tabs { display: flex; justify-content: space-between; margin-bottom: 25px; background: #0f172a; border-radius: 10px; padding: 5px; }
        .tab { flex: 1; padding: 8px; cursor: pointer; border-radius: 8px; font-size: 12px; transition: 0.3s; border: none; background: transparent; color: #94a3b8; }
        .tab.active { background: #38bdf8; color: #0f172a; font-weight: bold; }
        input { display: block; width: 88%; padding: 12px; margin: 12px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; outline: none; }
        input:focus { border-color: #38bdf8; }
        .btn { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 95%; margin-top: 10px; }
        .hidden { display: none; }
        .status-text { font-size: 11px; color: #94a3b8; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="nav-tabs">
            <button class="tab active" id="btnSignUp" onclick="show('signup')">Sign Up</button>
            <button class="tab" id="btnLogin" onclick="show('login')">Login</button>
            <button class="tab" id="btnAdmin" onclick="show('admin')">Admin</button>
        </div>

        <div id="signupBox">
            <h2 style="color:#38bdf8;">Create Account</h2>
            <input type="text" placeholder="Full Name">
            <input type="email" placeholder="Email Address">
            <input type="password" placeholder="Create Password">
            <button class="btn" onclick="alert('Account Created! Now Login.')">Register Now</button>
        </div>

        <div id="loginBox" class="hidden">
            <h2 style="color:#38bdf8;">User Login</h2>
            <input type="email" placeholder="Email">
            <input type="password" placeholder="Password">
            <button class="btn" onclick="openPortal()">Login to Portal</button>
        </div>

        <div id="portalBox" class="hidden">
            <h2 style="color:#22c55e;">🚀 Nexus Portal</h2>
            <p class="status-text">Connected: Active</p>
            <input type="text" placeholder="Instagram Username">
            <input type="password" placeholder="Instagram Password">
            <button class="btn" style="background:#22c55e;" onclick="alert('Proceeding to Pay ₹99')">Start Bot & Pay</button>
        </div>

        <div id="adminBox" class="hidden">
            <h2 style="color:#fbbf24;">🛡️ Master Admin</h2>
            <input type="email" id="admE" placeholder="nexusai119@gmail.com">
            <input type="password" id="admP" placeholder="Admin Password">
            <button class="btn" style="background:#fbbf24;" onclick="checkAdmin()">View Users Data</button>
            <p class="status-text" onclick="alert('OTP sent to {{phone}}')">Forgot Password?</p>
        </div>
    </div>

    <script>
        function show(mode) {
            // Hide all
            document.getElementById('signupBox').classList.add('hidden');
            document.getElementById('loginBox').classList.add('hidden');
            document.getElementById('adminBox').classList.add('hidden');
            document.getElementById('portalBox').classList.add('hidden');
            
            // Remove active class
            document.getElementById('btnSignUp').classList.remove('active');
            document.getElementById('btnLogin').classList.remove('active');
            document.getElementById('btnAdmin').classList.remove('active');

            if(mode === 'signup') {
                document.getElementById('signupBox').classList.remove('hidden');
                document.getElementById('btnSignUp').classList.add('active');
            } else if(mode === 'login') {
                document.getElementById('loginBox').classList.remove('hidden');
                document.getElementById('btnLogin').classList.add('active');
            } else {
                document.getElementById('adminBox').classList.remove('hidden');
                document.getElementById('btnAdmin').classList.add('active');
            }
        }

        function openPortal() {
            document.getElementById('loginBox').classList.add('hidden');
            document.getElementById('portalBox').classList.remove('hidden');
        }

        function checkAdmin() {
            let e = document.getElementById('admE').value;
            let p = document.getElementById('admP').value;
            if(e === "{{email}}" && p === "{{pw}}") {
                alert("Access Granted! Opening Database...");
            } else { alert("Wrong Admin Details!"); }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_LAYOUT, email=ADMIN_GMAIL, pw=ADMIN_PASSWORD, phone=ADMIN_PHONE)

if __name__ == "__main__":
    app.run(debug=True)
