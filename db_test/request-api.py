import requests

response = requests.get('http://192.168.1.78:5000/data')

print(response.text)