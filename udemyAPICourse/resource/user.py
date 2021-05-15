from flask_restful import Resource, reqparse

userList = [
    {
        "name":"mark",
        "password":"mark123"
    },
    {
        "name" : "merry",
        "password" : "merry123"
    }
]

class User(Resource):

    # 參數處理
    parser = reqparse.RequestParser()
    parser.add_argument('password', type = str, required = True, help = 'password is required')

    def get(self, username):
        user_check = [user for user in userList if user['name'] == username]
        if user_check:
            return user_check[0], 200
        else:
            return {'message':'user not found'}, 204
    
    def post(self, username):
        user_check = [user for user in userList if user['name'] == username]
        data = User.parser.parse_args()
        print(data)
        if user_check:
            return {'message':'user already exist'}
        else:
            user = {"name":username, "password":data['password']}
            userList.append(user)
            return user, 201
    
    def delete(self, username):
        user_check = [user for user in userList if user['name'] == username]
        if user_check:
            userList.remove(user_check[0])
            return {'message':'user delete done'}
        else:
            return {'user not found'}, 204

    def put(self, username):
        user_check = [user for user in userList if user['name'] == username]
        data = User.parser.parse_args()
        if user_check:
            userIndex = userList.index(user_check[0])
            userList[userIndex]['password'] = data['password']
            return {'message':'update success'}
        else:
            return {'user not found'}, 204


class Users(Resource):
    def get(self):
        return userList
