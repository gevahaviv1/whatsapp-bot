from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# List of WhatsApp group numbers
group_numbers = [
    'whatsapp:+12345678901',  # Replace with your WhatsApp group numbers
    'whatsapp:+10987654321',
    # Add more group numbers here
]

def send_message_to_groups(message):
    for group_number in group_numbers:
        message = client.messages.create(
            body=message,
            from_='whatsapp:+your_twilio_number',  # Your Twilio sandbox number
            to=group_number
        )
        print(f'Message sent to {group_number}: {message.sid}')

# Example usage
if __name__ == "__main__":
    send_message_to_groups("Hello, this is a test message to all groups!")

