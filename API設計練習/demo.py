import requests

res = requests.get('http://127.0.0.1:5000/user/Merry')

print(res)

print(res.json())