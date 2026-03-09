from flask import Flask, render_template_string

app = Flask(__name__)

# Design ko seedha code ke andar daal diya hai
HTML = """
<!DOCTYPE html>
<html>
<head><title>Nexus AI</title></head>
<body style="background:#0f172a; color:white; text-align:center; padding-top:100px; font-family:sans-serif;">
    <h1 style="color:#38bdf8;">🚀 Nexus AI Portal</h1>
    <div style="background:#1e293b; display:inline-block; padding:40px; border-radius:15px; border:1px solid #38bdf8;">
        <input type="text" placeholder="Instagram ID" style="display:block; margin:10px auto; padding:12px; width:250px; border-radius:5px; border:none;">
        <input type="password" placeholder="Password" style="display:block; margin:10px auto; padding:12px; width:250px; border-radius:5px; border:none;">
        <button onclick="alert('Redirecting to Payment...')" style="background:#38bdf8; color:#0f172a; border:none; padding:12px 30px; border-radius:8px; cursor:pointer; font-weight:bold;">Login & Pay ₹99</button>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True, port=5000)