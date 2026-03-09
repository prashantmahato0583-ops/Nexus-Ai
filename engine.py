import google.generativeai as genai

API_KEY = "AIzaSyAQUMdNxlZaLqSoOHU7niHefE-X13xlkEA"
genai.configure(api_key=API_KEY)

def get_ai_reply(user_message):
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Nexus AI ko dosti wali bhasha sikhai gayi hai
    prompt = f"Tum Nexus AI ho, Prashant ne banaya hai. User se uski bhasha mein dosti se baat karo: {user_message}"
    response = model.generate_content(prompt)
    return response.text