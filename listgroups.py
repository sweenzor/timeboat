import httplib2
import urllib

import time
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('key.cfg')

#GET https://api.groupme.com/clients/groups
#  ?client_id=YOUR_CLIENT_ID
#  &token=YOUR_ACCESS_TOKEN

#GET https://api.groupme.com/clients/groups/GROUP_ID/lines
#  ?client_id=YOUR_CLIENT_ID
#  &token=YOUR_ACCESS_TOKEN

payload = {
  "group" : {
    "topic"       : "Night Out",
    "memberships" : [
      {
        "name"          : "Bob",
        "phone_number"  : "+1 2125555555"
      },
      {
        "name"          : "Anne",
        "email"         : "anne@example.com"
      },
      {
        "name"          : "John",
        "user_id"       : "1234567892"
      }
    ]
  }
}


http = httplib2.Http()

url = 'https://api.groupme.com/clients/groups'
body = dict(client_id = config.get('groupme', 'client_id', 0),
			token = config.get('groupme', 'token', 0))

#print urllib.urlencode(body)+str(payload)
print urllib.urlencode(body)
response, content = http.request(url, 'GET', body=urllib.urlencode(body))

print content
print response
