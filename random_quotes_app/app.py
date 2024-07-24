from flask import Flask, render_template
import random

app = Flask(__name__)

# List of quotes
quotes = [
    "The best way to predict the future is to create it.",
    "You miss 100% of the shots you don't take.",
    "Every moment is a fresh beginning.",
    "Aspire to inspire before we expire.",
    "Everything you can imagine is real.",
    "Believe you can and you're halfway there.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Don't watch the clock; do what it does. Keep going.",
    "Keep your face always toward the sunshine—and shadows will fall behind you.",
    "It does not matter how slowly you go as long as you do not stop.",
    "You are never too old to set another goal or to dream a new dream.",
    "Act as if what you do makes a difference. It does.",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us.",
    "The future belongs to those who believe in the beauty of their dreams."
]

@app.route('/')
def index():
    random_quote = random.choice(quotes)
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

