from twilio.rest import Client

TWILIO_SID = "AC60ccc38ef2cf2cc3dbd0443deda1f19c"
TWILIO_AUTH_TOKEN = "e9e0060d3c282da111a74d6d368aa5b3"
TWILIO_VIRTUAL_NUMBER ="+16292763145"
TWILIO_VERIFIED_NUMBER = "+911234566788"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
