from flask import Flask, jsonify, request

app = Flask(__name__)

usersList = [
    {
        'name':'mark',
        'age': 24
    },
    {
        'name':'merry',
        'age': 27
    }
]

@app.route('/')
def index():
    return "Hello world"

# 返回用戶清單
@app.route('/users', methods = ['GET'])
def users():
    return jsonify(usersList)

# 新增用戶
@app.route('/user', methods = ['POST'])
def create_user():
    newuser = request.get_json()
    # [user for user in users if user['name'] == name]
    user_check = [user for user in usersList if user['name'] == newuser['name']]
    if user_check:
        return jsonify({'message':'user already exist'})
    else:
        usersList.append(newuser)
        return jsonify({'message': 'user created'})

# 刪除用戶
@app.route('/user/<username>', methods = ['DELETE'])
def delete_user(username):
    user_check = [user for user in usersList if user['name'] == username]
    if user_check:
        usersList.remove(user_check[0])
        return jsonify({'message':'user delete done'})
    else:
        return jsonify({'message':'delete error'}) 

# 更新用戶
@app.route('/user', methods = ['PUT'])
def update_user():
    newuser = request.get_json()
    user_check = [user for user in usersList if user['name'] == newuser['name']]
    if request.method == 'PUT':
        if user_check:
            userIndex = usersList.index(user_check[0])
            usersList[userIndex]['age'] = newuser['age']
            return jsonify({'message':'update user done'})
        else:
            return jsonify({'message':'error update'})
        
if __name__ == '__main__':
    app.run(debug = True)
    