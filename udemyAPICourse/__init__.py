from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from udemyAPICourse.resource.user import User, Users
from udemyAPICourse.resource.hello import HelloWorld

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///demo.db"
    db.init_app(app)

    api.add_resource(HelloWorld, '/')
    api.add_resource(User,'/user/<username>')
    api.add_resource(Users,'/users')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)