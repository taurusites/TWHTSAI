import requests 

class WhatsAppClient:

  def __init__(self):
    self.url = 'https://api.whatsapp.com/send'
  
  def receive(self):
    # Get message from WhatsApp
  
  def send(self, message):
    requests.post(self.url, json={'text': message})