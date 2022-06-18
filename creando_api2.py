from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def person():

    rsp = {
        'id': 123,
        'name': 'Edgard',
        'is_alive': True,
        'favorite_sports': ['cycling', 'tennis', 'swimming'],
        'graduated': None
    }
    print(type(rsp))

    return rsp

@app.route("/persons", methods=['POST', 'GET'])
def new_person():
    print(request.json)
    print(request.method)
    # print(request.url)
    # print(request.data)

    return request.json