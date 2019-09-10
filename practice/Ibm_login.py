import http.client

conn = http.client.HTTPConnection("api3.bmmarketingcloud.com", 443)

payload = "grant_type=refresh_token&client_id=5801dcb5-83cc-4642-8d8e-4412d3de869b&client_secret=f9d3bcd4-5ea1-47ac-85bb-0cbf91393ca1&refresh_token=rjDcehBBKUDMnUz3tNhbCoe44FUmcECqDT0veFjA7mfoS1&undefined="

headers = {
    'Content-Type': "application/x-www-form-urlencoded"
    }

conn.request("POST", "oauth,token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data)
print(data.decode("utf-8"))