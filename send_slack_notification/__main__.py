import json

import requests


class SendSlackNotification:

    def setting(self):
        print('input your web hook url!')
        self.web_hook_url = input()
        print('Decide on a name for your notification bot!')
        self.username = input()

    
    def send_message(self,message):
        self.data = json.dumps({
            'text': message,
            'username': self.username
        })
        requests.post(self.web_hook_url,self.data)