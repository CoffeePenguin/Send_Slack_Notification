import json

import requests


class SendSlackNotification:

    def setting(self):
        print('input your Webhook url!')
        self.web_hook_url = input()

    
    def send_message(self,message):
        self.data = json.dumps({
            'text': message
        })
        requests.post(self.web_hook_url,self.data)