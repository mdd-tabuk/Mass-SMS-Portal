from twilio.rest import Client
import os

# Twilio Credentials (Stored in GitHub Secrets)
ACCOUNT_SID = os.getenv("ACd3877f49f79adc3d81c7d3a120a41263")
AUTH_TOKEN = os.getenv("e46a4de560509bd9e2588d537a927a23")
FROM_NUMBER = os.getenv("+15073535376")
TO_NUMBER = os.getenv("+966509640181")  # Your recipient number
MESSAGE = "Hello! This is a test SMS from GitHub using Twilio."

# Initialize Twilio Client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Send SMS
message = client.messages.create(
    body=MESSAGE,
    from_=FROM_NUMBER,
    to=TO_NUMBER
)

print(f"✅ SMS Sent! Message SID: {message.sid}")
