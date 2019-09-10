import requests
import json

url = "https://api3.ibmmarketingcloud.com/oauth/token"

querystring = {"user_name":"vamsee@digitalinterakt.com","password":"Digi2019@%21","auth_type":"password"}

payload = "grant_type=refresh_token&client_id=5801dcb5-83cc-4642-8d8e-4412d3de869b&client_secret=f9d3bcd4-5ea1-47ac-85bb-0cbf91393ca1&refresh_token=rjDcehBBKUDMnUz3tNhbCoe44FUmcECqDT0veFjA7mfoS1&undefined="
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

result = response.text
resp = json.loads(result)
print(resp['access_token'])
