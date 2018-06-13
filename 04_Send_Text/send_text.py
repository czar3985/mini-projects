from twilio.rest import Client

account_sid = "ACab1cde2345f6g78h9ij1k011121314m1"
auth_token = "abc12defgh34i567j8k9101112m1314n"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello world',
                              from_='+13123456789',
                              to='+64123456789'
                          )

print(message.sid)
