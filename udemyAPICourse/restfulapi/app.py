from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from resource.user import Users, User
from resource.hello import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(User,'/user/<username>')
api.add_resource(Users,'/users')

if __name__ == '__main__':
    app.run(debug=True)