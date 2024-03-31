import requests


response = requests.get('https://httpbin.org/robots.txt')
print(response.text)
print(response.status_code)
print('Yay!')