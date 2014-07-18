from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC72618a5cc9f39dd76ffcee2f79133e1c"
auth_token  = "534754938deef53282cdb0ab0856d55c"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="Yo!",
    to="+40748749281",    # Replace with your phone number
    from_="+17855305760") # Replace with your Twilio number
print message.sid