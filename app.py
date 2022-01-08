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
	
@app.route("/inference/<int:epochs>")
def inference(epochs):
	vehicle_type = ["Car","Bus","Motorbike","Truck","Van"]
	vehicles_count = 0
	infer_stdout = ""
	for i in range(epochs):
		for j in vehicle_type:
			vehicles_count = vehicles_count + 1
			infer_stdout = infer_stdout + "Vehicle {}|{}|120Kmh \n".format(str(vehicles_count),j)
	return infer_stdout
	