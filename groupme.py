import httplib2
import urllib
import json

import ConfigParser


class groupme_auth(object):

#POST https://api.groupme.com/clients/tokens
#  ?client_id=YOUR_CLIENT_ID
#  &client_secret=YOUR_CLIENT_SECRET
#  &device_id=YOUR_DEVICE_ID
#  &phone_number=YOUR_PHONE_NUMBER
#  &grant_type=client_credentials

#POST https://api.groupme.com/clients/tokens
#  ?client_id=YOUR_CLIENT_ID
#  &client_secret=YOUR_CLIENT_SECRET
#  &device_id=YOUR_DEVICE_ID
#  &phone_number=YOUR_PHONE_NUMBER
#  &grant_type=authorization_code
#  &code=YOUR_AUTHORIZATION_CODE

	def __init__(self):
		self.http = httplib2.Http()
		config = ConfigParser.ConfigParser()
		config.read('keys.cfg')
		key_list = config.items('groupme')
		self.keys = {}
		for key in key_list:
			self.keys[key[0]] = key[1]

	def test_oauth(self):
		pass

	def request_token(self):

		payload = dict(
					client_id = self.keys['client_id'],
					client_secret = self.keys['client_secret'],
					device_id = self.keys['device_id'],
					phone_number = self.keys['phone_number'],
					grant_type = 'authorization_code',
					code = self.keys['code'])
		
		payload = urllib.urlencode(payload)
		url = 'https://api.groupme.com/clients/tokens'
		resp, content = self.http.request(url, 'POST', payload)
		content = json.loads(content)
		self.token = content[u'response'][u'access_token']

		return self.token

if __name__ == "__main__":

	auth = groupme_auth()
	print auth.request_token()

