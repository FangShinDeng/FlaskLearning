# 在udemy上學習用flask開發restful api
課程: https://www.udemy.com/course/flask-rest-api/learn/lecture/14050483#overview
課程: https://www.udemy.com/course/flask-rest-api/

## 建立虛擬環境, 並初始化
官方文獻: https://virtualenv.pypa.io/en/latest/
1. 安裝 pip install virtualenv
2. 初始化 virtualenv venv
3. 啟動 source venv/Scripts/activate (特別注意，其實就是去啟動activate.bat檔案就可以)
4. 確定是否成功啟動? 用pip list去看就可以知道了
5. 退出 deactivate
6. 導出套件包 pip freeze > requirements.txt
7. 安裝requirements.txt, 使用指令 pip install -r requirements

## 在虛擬環境上安裝需要的套件
pip install Flask 
pip install flask-restful

## HTTP協議
1. 就是用來定義 Client <-> Server 之間的協議
2. HTTP裡面有一個非常重要的詞就是 URL, Uniform Resource Locators (URLs) 去請求服務器上的res
3. http, https的差別在於secure 安全，是否有加密
4. HTTP的協議裡面有定義METHODS, 包含:GET, POST, PUT, DELETE

# 程式
1. flaskapi/main.py -> 原生flask開發API
2. restfulapi/app.py -> 用restul-flask 去開發API

## 了解用Postman去設計API
課程: 第三章-17

## Restful-Api 筆記
1. Restful-api return 的內容本身就已經是jsonify格式
2. reqparse 參數處理

## 將代碼重構
將資料夾結構整理好, 透過resource資料夾去整理

## SQLAlchemy 
1. 安裝 pip install flask_sqlalchemy

