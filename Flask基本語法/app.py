from flask import Flask, url_for, render_template, request, redirect

# 建立物件
app = Flask(__name__)

# 建立網站回應
@app.route("/")
def index():
    return render_template('index.html') # 渲染樣板

# 靜態路由
@app.route("/static")
def good():
    return '靜態路由'

# 動態路由
@app.route("/username/<username>")
def username(username):
    return 'I \' m {}'.format(username)

# 返回相對路由
@app.route('/returnUrl/<url>')
def returnUrl(url):
    return url_for(url) # /good

if __name__ == '__main__':
    app.debug = True
    app.run()