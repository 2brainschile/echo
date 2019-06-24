from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/webhook", methods = ['POST', 'GET'])
def hello():
    print(request.headers)
    print(request.data)
    return "OK"
