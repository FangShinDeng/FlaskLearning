from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

tasks = [
    {
        'id' : 1,
        'title': 'task1'
    },
    {
        'id' : 2,
        'title' : 'task2'
    }
]

People = {
    "Mark": {"age": 24, "gender": 'male'},
    "Tim" : {"age": 40, "gender": 'male'}
}

class Person(Resource):
    def get(self, name):
        return People[name]

class Car(Resource):
    def get(self, name):
        return jsonify({"name":name})

api.add_resource(Person, "/Person/<string:name>")
api.add_resource(Car, "/Car/<string:name>")

@app.route('/api/tasks', methods = ['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000, debug = True)
    