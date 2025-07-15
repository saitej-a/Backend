import requests
data={"username":"sai","password":"123"}
header={'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUyNDcxMDQxLCJpYXQiOjE3NTIzODQ2NDEsImp0aSI6ImRmM2QzYzRlNmUwMTRlMzJhNDBjZTNkNTE1N2YzMjQ5IiwidXNlcl9pZCI6MX0.hwy7Iu03nBKareHZy__r1gmi7hz0SefDAyoiwyseKgc'}
response= requests.get('http://localhost:8000/api/messages/?conversation=2',headers=header,data={"receiver":6,"body":"Hey Prasad","conversation":1})

print(response.json())