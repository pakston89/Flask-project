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
	infer_stdout = ""
	for i in range(n_inferences):
		infer_stdout = infer_stdout + "Vehicle {}|{}|120Kmh \n".format(str(i),vehicle_type[i])
	return infer_stdout
	