from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import configparser

app = Flask(__name__)

# config = configparser.ConfigParser()
# config.read('config.ini', encoding="utf-8-sig")

# # 本地 MYSQL
# MYSQLACCOUNT = config['MYSQL']['ACCOUNT']
# MYSQLPWD = config['MYSQL']['PASSWORD']
# MYSQLPORT = config['MYSQL']['PORT']
# MYSQLDBNAME = config['MYSQL']['DBNAME']

# # 配置SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{ACCOUNT}:{PASSWORD}@localhost:{PORT}/{DBNAME}".format(
#     ACCOUNT = MYSQLACCOUNT,
#     PASSWORD = MYSQLPWD,
#     PORT = MYSQLPORT,
#     DBNAME = MYSQLDBNAME  
# ))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Cars(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    carname = db.Column(db.String(80), unique=True, nullable=False)

# 創建資料庫
db.create_all()

# 查詢資料庫
query = db.Query.all