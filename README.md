# 學習使用Flask 
    學習連結: https://hackmd.io/@shaoeChen/SyP4YEnef?type=view

## Flask基本語法
- 創建flask物件
- 學會使用固定路由,動態路由,反饋相對路由
- 搭配 render_template 將html文件直接return回去

## 用Flask搭建簡易會員登入
- 了解static靜態資源的img及css架構
- templates內的html檔案，變數採用jinja2的架構，需要用 url_for('static', filename = 'css/style.css')
- 引用bootstrap5
- 將後端資料在前端顯示
- 繼承模板 {% extends 'index.html' %}
- 創建子模板 {% block content %} {% endblock %}
<br>`繼承的模板可以將子模板內的東西去修改`

# Max Flask教學參考
    學習連結: https://www.maxlist.xyz/2020/05/01/flask-list/#%E4%B8%80_Flask_%E5%85%A5%E9%96%80%E7%AF%87

## 了解如何處理 無限迴圈
    在主程式裡面 import 其他程式
    然後用 程式名.函式名(app) 來啟用該程式
    請查看範例app.py及userdata.py

## Restful API Users 設計練習
    
    參考學習: https://ithelp.ithome.com.tw/articles/10202521

    建立一個使用者CRUD的API
    1. 建立Api及Resource, 並用api.add_resource去新增資源
    2. 建立parser = reqparse.RequestParser(), 新增及處理參數
    

## 補充內容
1. 0.0.0.0 代表所有主機位置(https://ithelp.ithome.com.tw/articles/10224594)
2. jsonify 是為了返回是為json格式，若用一般{},則會顯示str
3. 了解*arg -> list, **kwarg -> dict, 及add_argument
