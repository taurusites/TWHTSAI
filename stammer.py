import requests

class StammerClient:

  def __init__(self, api_key):
    self.url = 'https://api.stammer.ai/message'
    self.headers = {'Authorization': f'Bearer {api_key}'}

  def send_message(self, message):
    response = requests.post(self.url, 
                             headers=self.headers,
                             json={'message': message})
    return response.json()['reply']