@app.route('/')
def user_home():
    return """
    <html>
    <head>
        <title>Nexus AI Portal</title>
        <style>
            body { background: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 100px; }
            .card { background: #1e293b; display: inline-block; padding: 40px; border-radius: 15px; border: 1px solid #38bdf8; }
            input { display: block; width: 250px; padding: 12px; margin: 15px auto; border-radius: 8px; border: none; }
            button { background: #38bdf8; padding: 12px; width: 100%; border-radius: 8px; border: none; font-weight: bold; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2 style="color:#38bdf8;">🚀 Nexus AI Access</h2>
            <input type="text" placeholder="Instagram ID">
            <input type="password" placeholder="Password">
            <button onclick="alert('Redirecting to Payment...')">Login & Pay ₹99</button>
        </div>
    </body>
    </html>
    """
