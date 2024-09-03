import requests

r = requests.get('https://httpbin.org/basic-auth/abdullah/tessting', auth=('abdullah', 'tessting'))

print(r.text)
