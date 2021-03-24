from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        if request.values['uname'] == 'admin' and request.values['psw'] == '1234':
            return "Success Login"
        else:
            return render_template('login.html')

    return render_template('login.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

