import requests
import sys
t = sys.argv[1]
d = 20
v = 69
base_url = "http://krismalen.pythonanywhere.com"
base_url = "http://127.0.0.1:8000"
url = f"{base_url}/stuurdata?temperatuur={t}&luchtdruk={d}&luchtvochtigheid={v}"

r = requests.get(url)

print(r.text)