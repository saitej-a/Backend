import requests
response= requests.delete('http://127.0.0.1:8000/api/user/delete/3',data={"auth_user":3})
print(response.json())