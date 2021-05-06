import os,json
from flask import Flask, request, make_response
from flask_cors import CORS

application = Flask(__name__)

CORS(application, supports_credentials=True)

@application.route("/hello", methods=["POST","GET"])
def hello():
	response = make_response(json.dumps({"code":0, "msg":"success", "data":{"name":"baibai"}}))
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Headers'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
	response.headers['Access-Control-Allow-Credentials'] = 'true'
	response.headers['Content-Type'] = 'application/json'
	return response

if __name__ == "__main__":
	application.run(host="0.0.0.0",port=5000,debug=True)



