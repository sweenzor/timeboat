import httplib2
import urllib

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
		self.config = ConfigParser.ConfigParser()
		self.config.read('keys.cfg')

	def test_oauth(self):
		pass


	def request_token(self):

		keys = dict(client_id = self.config.get('groupme', 'client_id', 0),
					client_secret = self.config.get('groupme', 'client_secret', 0),
					device_id = self.config.get('groupme', 'device_id', 0),
					phone_number = self.config.get('groupme', 'phone_number', 0),
					grant_type = 'authorization_code',
					code = self.config.get('groupme', 'code', 0))
		
		payload = urllib.urlencode(keys)
		resp, content = self.http.request("https://api.groupme.com/clients/tokens", "POST", payload)
		return content

if __name__ == "__main__":

	auth = groupme_auth()
	print auth.request_token()

