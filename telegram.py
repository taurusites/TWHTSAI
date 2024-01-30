import requests

class TelegramClient:

  def __init__(self):
    self.url = 'https://api.telegram.org/botTOKEN/sendMessage'

  def receive(self):
    # Get message from Telegram
  
  def send(self, message):
    requests.post(self.url, json={'text': message})