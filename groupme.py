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
		pass

	def request_token(self):

		http = httplib2.Http()

		config = ConfigParser.ConfigParser()
		config.read('keys.cfg')
		keys = dict(
				client_id = config.get('groupme', 'client_id', 0),
					client_secret = config.get('groupme', 'client_secret', 0),
					device_id = config.get('groupme', 'device_id', 0),
					phone_number = config.get('groupme', 'phone_number', 0),
					grant_type = 'authorization_code',
					code = config.get('groupme', 'code', 0))
		

		print urllib.urlencode(keys)
		resp, content = http.request("https://api.groupme.com/clients/tokens", "POST", urllib.urlencode(keys))
		print content
		print resp

if __name__ == "__main__":

	auth = groupme_auth()
	auth.request_token()

