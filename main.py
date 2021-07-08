from flask import Flask,jsonify,request
from flask.json import jsonify
from werkzeug.wrappers import request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'Name': 'Arshiya',
        'Contact': '9855650829', 
        'done': False
    },
    {
        'id': 1,
        'Name': 'Mannat',
        'Contact': '9834765082', 
        'done': False
    }
]


@app.route("/add-data",methods = ["POST"])
def add_task() :
    if not request.json :
        return jsonify({
            "status" : "error",
            "message" : "Please Provide the data"

        },400)

    contact = {
        'id': tasks[-1]['id']+1,
        'title': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False

    }

    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })

@app.route("/get-data")
def get_task() :
    return jsonify({
        "data" : tasks
    })


if (__name__ == '__main__') :
    app.run(debug = True)