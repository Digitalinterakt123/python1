import requests

url = "https://api3.ibmmarketingcloud.com/XMLAPI"

querystring = {"user_name":"vamsee@digitalinterakt.com","password":"Digi2019@%21","auth_type":"password"}

payload = "<Envelope>\n  <Body>\n    <AddRecipient>\n      <LIST_ID>10412785</LIST_ID>\n      <CREATED_FROM>1</CREATED_FROM>\n      <UPDATE_IF_FOUND>true</UPDATE_IF_FOUND>\n      <COLUMN>\n        <NAME>EMAIL</NAME>\n        <VALUE>praneeth1235@gmail.com</VALUE>\n      </COLUMN>\n       <COLUMN>\n        <NAME>email_form_location</NAME>\n        <VALUE>blog_trends</VALUE>\n      </COLUMN>\n       <COLUMN>\n        <NAME>email_source</NAME>\n        <VALUE>blog</VALUE>\n      </COLUMN>\n       <COLUMN>\n        <NAME>subscribe</NAME>\n        <VALUE>yes</VALUE>\n      </COLUMN>\n       <COLUMN>\n        <NAME>email_source_content</NAME>\n        <VALUE>buyers_guide</VALUE>\n      </COLUMN>\n       <COLUMN>\n        <NAME>language</NAME>\n        <VALUE>en</VALUE>\n      </COLUMN>\n      \n    </AddRecipient>\n  </Body>\n</Envelope>"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Bearer ayZ3arlZa38-b83xMo9YoQI5eYRnDLnYDrIexW2CRCY8S1"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)