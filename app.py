from flask import Flask
from flask import render_template
from flask import request
from core.model import Model
from modules.Accounting.model.invoice import Invoice
import logging
import json

app = Flask(__name__)


@app.route('/',methods=['GET'])
def home():
	return render_template('index.html')

#max edit to test git push 27 July 2020, 9:57pm

@app.route('/rpc',methods=['GET','POST'])
def rpc():
	#create class instances, bad idea. need improvement
	model_instances = {
		"invoice": Invoice()
	}
	content = request.get_json()
	#app.logger.info("content: {}".format(content))
	model_name = content["model"]
	function = content["function"]
	arguments = content["arguments"]
	#app.logger.info("check rpc, model_name:{}, function:{}, arguments:{}".format(model_name,function,arguments))
	if model_name in model_instances:
		call_method = getattr(model_instances[model_name],function)
		app.logger.info(call_method(arguments))
		return json.dumps(call_method(arguments)),200
	else:
		return "Model not Found: {}".format(model_name),403 

if __name__ == "__main__":
		app.run(debug=True)
