from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to home!"

@app.route("/sum/<int:value>")
def sum(value):
    result = value + 5
    return "The result is {}".format(str(result))
    
@app.route("/multiply/<int:value>")
def multiply(value):
	result = value * 5
	return "The result is {}".format(str(result))
	
@app.route("/inference/<int:n_inferences>")
def inference(n_inferences):
	vehicle_type = ["Car","Bus","Motorbike","Truck","Van"]
	for i in range(n_inferences):
		time.sleep(1)
		return "Vehicle {}|{}|120Kmh".format(str(i),vehicle_type[i])
	