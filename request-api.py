import requests

response = requests.get('http://192.168.1.97:5000/data')

print(response.text)