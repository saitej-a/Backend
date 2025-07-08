import requests
data={"username":"prasad","password":"123","role":"STUDENT"}
response= requests.get('http://127.0.0.1:8000/api/users/6')

print(response.json())