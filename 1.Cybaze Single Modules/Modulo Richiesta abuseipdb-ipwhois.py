import urllib3
import json
import requests

ip = input("Inserisci l\'IP da controllare: ")
http = urllib3.PoolManager()
url = "http://ipwhois.app/json/" + ip
r = http.request('GET', url)

response = json.loads(r.data)
print(response)


