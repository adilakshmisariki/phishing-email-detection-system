from flask import Flask, render_template, request
import re

app = Flask(__name__)

phishing_keywords = [
    "urgent",
    "verify your account",
    "bank",
    "login immediately",
    "click here",
    "free money",
    "password",
    "winner"
]

def detect_phishing(email_text):
    score = 0

    for word in phishing_keywords:
        if word.lower() in email_text.lower():
            score += 1

    urls = re.findall(r'(https?://\S+)', email_text)

    if len(urls) > 0:
        score += 1

    if score >= 3:
        return "⚠️ Phishing Email Detected"
    else:
        return "✅ Safe Email"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""

    if request.method == 'POST':
        email_text = request.form['email']
        result = detect_phishing(email_text)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)