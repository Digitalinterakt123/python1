import requests
import json
import cgi


form = cgi.FieldStorage()
#emailid =  form.getvalue('email')
emailid="praneeeeth@yahoo.com"

def wcaLogin():
    url = "https://api3.ibmmarketingcloud.com/oauth/token"

    querystring = {"user_name": "vamsee@digitalinterakt.com", "password": "Digi2019@!", "auth_type": "password"}

    payload = "grant_type=refresh_token&client_id=5801dcb5-83cc-4642-8d8e-4412d3de869b&client_secret=f9d3bcd4-5ea1-47ac-85bb-0cbf91393ca1&refresh_token=rjDcehBBKUDMnUz3tNhbCoe44FUmcECqDT0veFjA7mfoS1&undefined="
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    result = response.text
    resp = json.loads(result)
    print("access_token :",resp['access_token'])
    addRecipient(resp['access_token'],emailid)

def addRecipient(access_token,emailid):
    url = "https://api3.ibmmarketingcloud.com/XMLAPI"

    querystring = {"user_name": "vamsee@digitalinterakt.com", "password": "Digi2019@!", "auth_type": "password"}

    payload = "<Envelope>\n  " \
              "<Body>\n   " \
              "<AddRecipient>\n    " \
              "  <LIST_ID>10412785</LIST_ID>\n      " \
              "  <CREATED_FROM>1</CREATED_FROM>\n    " \
              "  <UPDATE_IF_FOUND>true</UPDATE_IF_FOUND>\n" \
              "  <COLUMN>\n      " \
              "       <NAME>EMAIL</NAME>\n   " \
              "       <VALUE>emailid</VALUE>\n   " \
              "  </COLUMN>\n" \
              "  <COLUMN>\n   " \
              "    <NAME>email_form_location</NAME>\n " \
              "    <VALUE>blog_trends</VALUE>\n     " \
              "  </COLUMN>\n    " \
              "  <COLUMN>\n    " \
              "    <NAME>email_source</NAME>\n      " \
              "    <VALUE>blog</VALUE>\n    " \
              "  </COLUMN>\n      " \
              "  <COLUMN>\n" \
              "    <NAME>subscribe</NAME>\n   " \
              "    <VALUE>yes</VALUE>\n     " \
              "  </COLUMN>\n     " \
              "  <COLUMN>\n  " \
              "    <NAME>email_source_content</NAME>\n " \
              "    <VALUE>buyers_guide</VALUE>\n   " \
              "  </COLUMN>\n       " \
              "  <COLUMN>\n  " \
              "    <NAME>language</NAME>\n        " \
              "    <VALUE>en</VALUE>\n" \
              "  </COLUMN>\n    " \
              "\n    </AddRecipient>\n  " \
              "</Body>\n" \
              "</Envelope>"
    headers = {
        'Content-Type': "text/xml",
        'Authorization': "Bearer " + access_token
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    print(response.text)
wcaLogin()
