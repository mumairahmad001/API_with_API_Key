import requests

apiKey = 'Muhammad'
# url = 'https://127.0.0.1:8080/getname?user=Muhammad'
url = 'https://127.0.0.1:8080/apistatus'
headers = {'X-API-Key':'1db4f85ce1701159b1a770771c831db975d4fd279af31b29'}
response = requests.get(url, headers = headers, verify=False)
print(response.content)
