from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app) 

class Hello(Resource):
    def get(self, empName):
        return "Hello Dear " + empName, 200


api.add_resource(Hello, '/hello/<string:empName>' )
app.run(debug=True)
