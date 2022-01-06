from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    elements = []
    for i in range(100):
        elements.append(lambda i : i * 2 / 1.5)
    return "Welcome to home!"

