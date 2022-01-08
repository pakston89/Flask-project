from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to home!"

@app.route("/sum/value")
def sum(value):
    result = value + 5
    return "The result is {}".format(str(result))
    
@app.route("/multiply/<int:value>")
def multiply(value):
	result = value * 5
	return "The result is {}".format(str(result))