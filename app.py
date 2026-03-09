from flask import Flask, render_template_string, request

app = Flask(__name__)
app.secret_key = "nexus_final_boss_7903"

# --- ADMIN DETAILS ---
ADMIN_GMAIL = "nexusai119@gmail.com"
ADMIN_PASSWORD = "prashant@123456"
ADMIN_PHONE = "7903530625"

# --- DESIGN ---
HTML_LAYOUT = """
<!DOCTYPE html>
<html>
<head>
    <title>Nexus AI Project</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 40px; }
        .main-card { background: #1e293b; display: inline-block; padding: 25px; border-radius: 15px; border: 2px solid #38bdf8; width: 310px; box-shadow: 0 10px 25px rgba(0,0,0,0.4); }
        .tabs { display: flex; justify-content: center; gap: 8px; margin-bottom: 20px; }
        .t-btn { padding: 6px 12px; border-radius: 20px; border: 1px solid #38bdf8; background: transparent; color: #38bdf8; cursor: pointer; font-size: 11px; }
        .t-btn.active { background: #38bdf8; color: #0f172a; font-weight: bold; }
        input { display: block; width: 90%; padding: 12px; margin: 12px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; }
        .go-btn { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; margin-top: 10px; }
        .hidden { display: none; }
        .footer-text { font-size: 11px; color: #94a3b8; margin-top: 15px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="main-card">
        <div class="tabs">
            <button class="t-btn active" id="uT" onclick="toggle('user')">User Access</button>
            <button class="t-btn" id="aT" onclick="toggle('admin')">Admin Master</button>
        </div>

        <div id="uSec">
            <div id="step1">
                <h2 style="color:#38bdf8; margin-bottom:5px;">Join Nexus</h2>
                <p style="font-size:11px; margin-bottom:15px;">Create account to start automation</p>
                <input type="text" placeholder="Your Name">
                <input type="email" placeholder="Email Address">
                <input type="password" placeholder="Create Password">
                <button class="go-btn" onclick="nextStep()">Create Account & Continue</button>
            </div>
            
            <div id="step2" class="hidden">
                <h2 style="color:#38bdf8;">🚀 Nexus Portal</h2>
                <p style="font-size:11px;">Enter Instagram details for bot setup</p>
                <input type="text" placeholder="Instagram Username">
                <input type="password" placeholder="Instagram Password">
                <button class="go-btn" onclick="pay()">Login & Pay ₹99</button>
            </div>
        </div>

        <div id="aSec" class="hidden">
            <h2 style="color:#fbbf24;">🛡️ Admin Login</h2>
            <input type="email" id="aE" placeholder="nexusai119@gmail.com">
            <input type="password" id="aP" placeholder="Password">
            <button class="go-btn" style="background:#fbbf24;" onclick="checkA()">Unlock Database</button>
            <p class="footer-text" onclick="alert('OTP sent to {{phone}}')">Forgot Password?</p>
        </div>
    </div>

    <script>
        function toggle(m) {
            if(m === 'user') {
                document.getElementById('uSec').classList.remove('hidden');
                document.getElementById('aSec').classList.add('hidden');
                document.getElementById('uT').classList.add('active');
                document.getElementById('aT').classList.remove('active');
            } else {
                document.getElementById('aSec').classList.remove('hidden');
                document.getElementById('uSec').classList.add('hidden');
                document.getElementById('aT').classList.add('active');
                document.getElementById('uT').classList.remove('active');
            }
        }
        function nextStep() {
            document.getElementById('step1').classList.add('hidden');
            document.getElementById('step2').classList.remove('hidden');
        }
        function pay() {
            alert("Redirecting to Secure Payment Gateway... ₹99");
        }
        function checkA() {
            let e = document.getElementById('aE').value;
            let p = document.getElementById('aP').value;
            if(e === "{{email}}" && p === "{{pw}}") {
                alert("Access Granted! Welcome Prashant.");
            } else { alert("Invalid Credentials!"); }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def main():
    return render_template_string(HTML_LAYOUT, email=ADMIN_GMAIL, pw=ADMIN_PASSWORD, phone=ADMIN_PHONE)

if __name__ == "__main__":
    app.run(debug=True)
