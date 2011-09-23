from httplib2 import Http
from urllib import urlencode

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('key.cfg')

#POST https://api.groupme.com/clients/tokens
#  ?client_id=YOUR_CLIENT_ID
#  &client_secret=YOUR_CLIENT_SECRET
#  &device_id=YOUR_DEVICE_ID
#  &phone_number=YOUR_PHONE_NUMBER
#  &grant_type=client_credentials

h = Http()
data = dict(client_id = config.get('groupme', 'client_id', 0),
			client_secret = config.get('groupme', 'client_secret', 0),
			device_id = config.get('groupme', 'device_id', 0),
			phone_number = config.get('groupme', 'phone_number', 0),
			grant_type = 'client_credentials')

print urlencode(data)
resp, content = h.request("https://api.groupme.com/clients/tokens", "POST", urlencode(data))
print content
print resp