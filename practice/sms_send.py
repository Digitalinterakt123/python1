
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACb724a7a535afead182302196f3182617'
auth_token = '6a8523e22def907eccf5e4879bb4d9d7'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15132582773',
                     to='+918977818527'
                 )

print(message.sid)