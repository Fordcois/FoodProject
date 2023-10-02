# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import keys

client =Client(keys.account_sid,keys.auth_token)
def send_twillio_message(PhoneNumber,MessageBody):
    Message = client.messages.create(
        body=MessageBody,
        from_=keys.twilio_numer,
        to=PhoneNumber
    )