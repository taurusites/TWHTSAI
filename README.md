* Telegram Webhook Which connects to stammer.ai

** Introduction
This is a python based web hook aplication which will be using flask and gunicorn to connect to stammer.ai and will also run serverless (Right now possibly on cloudflare). Thi webhook will take input from a telegram chat and pass it through to stammer.ai and will then send the response back to the telegram chat.
We will also be using cloudflare to host our serverless application.
The idea behind this all is hove everything modular and with interfaces so that tomorrow if we want we could also plugin whatsapp for the chat portion or replace stammer with another provider if we so wish. The same idea also applies tro cloudflare, in case we wish to run serverless on AWS for example.
We could also consider authentication based webhook usage in case we want to monetize at a later stage.

** stammer.ai requirements
API Endpoint - https://cbr.fluidtrack.in/en/chatbot/api/v1/message/
Request Headers for API :
Content-Type: application/json
Authorization: Token <Your-API-Token>
Python example script : 
```import requests

# Define the API endpoint
url = "https://cbr.fluidtrack.in/en/chatbot/api/v1/message/"

# Set the headers for the request
headers = {
    'Authorization': 'Token <YOUR-API-TOKEN>',
    'Content-Type': 'application/json'
}

# Construct the data payload
data = {
    "chatbot_uuid": "12345678-1234-5678-1234-567812345678",
    "query": "Your message/string here.",
    "user_key": "Your message/string here.",
}

# Make the API request
response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 200:
    print("response:", response.json().get('data'))
else:
    error_data = response.json()
    print("Error:", error_data.get('message', '') + error_data.get('error', ''))
```
chatbot_uuid
 
(Type: UUID, Required)
Unique identifier (UUID) of the chatbot. You can find this UUID on the chatbot's detail page.

query
 
(Type: String, Required)
Message or query the user intends to send to the chatbot. Must be under 2000 characters.

user_key
 
(Type: String, Required)
A unique identifier/string, used to distinguish users interacting with the chatbot.
Example Response :
```json
{
    "message": "Chatbot successfully answered.",
    "data": {
        "answer": "If you have a specific question or need assistance with something, please let me know and I'll be happy to help.",
        "chat_id": 634
    }
}
```
Error Handling :
```json
// Response when API parameters are incorrect
{
    "message": "The provided parameters are not valid. Please check and try again.",
    "errors": {
        "chatbot_uuid": [
            "This field is required."
        ]
    }
}
```

For telegram we plan to use Telegraf library