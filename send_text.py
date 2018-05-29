#   Description:
#       This is a mini project written in python from Udacity.com's Intro to Programming Nano Degree course. 
#    This program sends a text message to an sms enabled device.
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC124e65d626b3200355e560951d0693f2"
# Your Auth Token from twilio.com/console
auth_token  = "68cacea2c5055ede40cf0cb0e08431a5"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19047533854", 
    from_="+19045302662",
    body="Hello from Lassiter!")

print(message.sid)