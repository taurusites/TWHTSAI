from flask import Flask
from telegram import TelegramClient 
from whatsapp import WhatsAppClient
from stammer import StammerClient

app = Flask(__name__)

telegram = TelegramClient()
whatsapp = WhatsAppClient()  
stammer = StammerClient('API_KEY')

@app.route('/')
def webhook():
  msg = telegram.receive() or whatsapp.receive()
  response = stammer.send_message(msg)
  telegram.send(response) or whatsapp.send(response)
  
if __name__ == '__main__':
  app.run()