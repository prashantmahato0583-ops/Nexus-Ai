from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- AAPKA DATA ---
ADMIN_GMAIL = "nexusai119@gmail.com"
ADMIN_PASSWORD = "prashant@123456"
ADMIN_PHONE = "7903530625"

# --- ALL-IN-ONE DESIGN ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Nexus AI Project</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 50px; }
        .container { background: #1e293b; display: inline-block; padding: 30px; border-radius: 15px; border: 2px solid #38bdf8; width: 320px; position: relative; }
        .switch-tabs { margin-bottom: 20px; display: flex; justify-content: center; gap: 10px; }
        .tab { padding: 8px 15px; cursor: pointer; border-radius: 20px; font-size: 12px; border: 1px solid #38bdf8; background: transparent; color: #38bdf8; }
        .tab.active { background: #38bdf8; color: #0f172a; font-weight: bold; }
        input { display: block; width: 90%; padding: 12px; margin: 15px auto; border-radius: 8px; border: 1px solid #334155; background: #0f172a; color: white; }
        button { background: #38bdf8; color: #0f172a; border: none; padding: 12px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div class="container">
        <div class="switch-tabs">
            <button class="tab active" id="userBtn" onclick="showMode('user')">User Portal</button>
            <button class="tab" id="adminBtn" onclick="showMode('admin')">Admin Panel</button>
        </div>

        <div id="userSection">
            <h2 style="color:#38bdf8;">🚀 Nexus AI Portal</h2>
            <input type="text" placeholder="Instagram ID">
            <input type="password" placeholder="Password">
            <button onclick="alert('Redirecting to Payment...')">Login & Pay ₹99</button>
        </div>

        <div id="adminSection" class="hidden">
            <h2 style="color:#fbbf24;">🛡️ Nexus Admin</h2>
            <input type="email" id="admEmail" placeholder="Admin Gmail">
            <input type="password" id="admPass" placeholder="Password">
            <button style="background:#fbbf24;" onclick="checkAdmin()">Unlock Dashboard</button>
            <p style="font-size:10px; margin-top:10px; cursor:pointer;" onclick="alert('OTP sent to {{phone}}')">Forgot Password?</p>
        </div>
    </div>

    <script>
        function showMode(mode) {
            if(mode === 'user') {
                document.getElementById('userSection').classList.remove('hidden');
                document.getElementById('adminSection').classList.add('hidden');
                document.getElementById('userBtn').classList.add('active');
                document.getElementById('adminBtn').classList.remove('active');
            } else {
                document.getElementById('adminSection').classList.remove('hidden');
                document.getElementById('userSection').classList.add('hidden');
                document.getElementById('adminBtn').classList.add('active');
                document.getElementById('userBtn').classList.remove('active');
            }
        }
        function checkAdmin() {
            let e = document.getElementById('admEmail').value;
            let p = document.getElementById('admPass').value;
            if(e === "{{email}}" && p === "{{pw}}") {
                alert("Welcome Boss!");
            } else {
                alert("Access Denied!");
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, email=ADMIN_GMAIL, pw=ADMIN_PASSWORD, phone=ADMIN_PHONE)

if __name__ == "__main__":
    app.run(debug=True)
