import requests

response = requests.get("https://theaxolotlapi.netlify.app/")
print(response.status_code)
print(response.text)