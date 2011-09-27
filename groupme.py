#! /usr/bin/python

import httplib2
import urllib
import json
import uuid

import ConfigParser


def cfg_to_dict():
	config = ConfigParser.ConfigParser()
	config.read('keys.cfg')
	key_list = config.items('groupme')
	keys = {}
	for key in key_list:
		keys[key[0]] = key[1]

	return keys


class auth(object):

	#POST https://api.groupme.com/clients/tokens
	#	?client_id=YOUR_CLIENT_ID
	#	&client_secret=YOUR_CLIENT_SECRET
	#	&device_id=YOUR_DEVICE_ID
	#	&phone_number=YOUR_PHONE_NUMBER
	#	&grant_type=client_credentials

	#POST https://api.groupme.com/clients/tokens
	#	?client_id=YOUR_CLIENT_ID
	#	&client_secret=YOUR_CLIENT_SECRET
	#	&device_id=YOUR_DEVICE_ID
	#	&phone_number=YOUR_PHONE_NUMBER
	#	&grant_type=authorization_code
	#	&code=YOUR_AUTHORIZATION_CODE

	def __init__(self):
		self.http = httplib2.Http()
		self.keys = cfg_to_dict()

	def test_oauth(self):
		pass

	def request_code(self):
		"""Check if code exists, if not request with client credentials"""
		pass

	def request_token(self):

		url = 'https://api.groupme.com/clients/tokens'
		payload = dict(
					client_id = self.keys['client_id'],
					client_secret = self.keys['client_secret'],
					device_id = self.keys['device_id'],
					phone_number = self.keys['phone_number'],
					grant_type = 'authorization_code',
					code = self.keys['code'])
		payload = urllib.urlencode(payload)
		
		resp, content = self.http.request(url, 'POST', payload)
		content = json.loads(content)
		self.keys['token'] = content[u'response'][u'access_token']

		return self.keys['token']


class interact(object):

	def __init__(self, token):
		self.token = token
		self.http = httplib2.Http()
		self.keys = cfg_to_dict()

	def list_groups(self):

		#GET https://api.groupme.com/clients/groups
		#	?client_id=YOUR_CLIENT_ID
		#	&client_secret=YOUR_CLIENT_SECRET
		#	&token=YOUR_ACCESS_TOKEN

		url = 'https://api.groupme.com/clients/groups?'
		payload = dict(
					client_id = self.keys['client_id'],
					client_secret = self.keys['client_secret'],
					token = self.token)
		payload = urllib.urlencode(payload)

		response, content = self.http.request(url+payload, 'GET')

		return content
	
	def check_membership(self, group_id):

		#GET https://api.groupme.com/clients/groups/GROUP_ID/memberships
		#	?client_id=YOUR_CLIENT_ID
		#	&client_secret=YOUR_CLIENT_SECRET
		#	&token=YOUR_ACCESS_TOKEN

		url = 'https://api.groupme.com/clients/groups/%s/memberships?' % group_id
		payload = dict(
					client_id = self.keys['client_id'],
					client_secret = self.keys['client_secret'],
					token = self.token)
		payload = urllib.urlencode(payload)

		response, content = self.http.request(url+payload, 'GET')

		return content

	def list_lines(self, group_id):

		#GET https://api.groupme.com/clients/groups/GROUP_ID/lines
		#	?client_id=YOUR_CLIENT_ID
		#	&client_secret=YOUR_CLIENT_SECRET
		#	&token=YOUR_ACCESS_TOKEN	

		url = 'https://api.groupme.com/clients/groups/%s/lines?' % group_id
		payload = dict(
					client_id = self.keys['client_id'],
					client_secret = self.keys['client_secret'],
					token = self.token)
		payload = urllib.urlencode(payload)
		print payload

		response, content = self.http.request(url+payload, 'GET')

		return content

	def create_group(self, group_topic, members):

		#POST https://api.groupme.com/clients/groups
		#	?client_id=YOUR_CLIENT_ID
		#	&client_secret=YOUR_CLIENT_SECRET
		#	&token=YOUR_ACCESS_TOKEN
		#{
		#	group : {
		#		topic		:	"Night Out",
		#		memberships	:	[
		#			{
		#				name			:	"Bob",
		#				phone_number	:	"+1 2125555555"
		#			},
		#			{
		#				name			:	"Anne",
		#				email			:	"anne@example.com"
		#			},
		#			{
		#				name			:	"John",
		#				user_id			:	"1234567892"
		#			}
		#		]
		#	}
		#}

		spec =	{'group': 
					{
						'topic': group_topic,
						'memberships': members
					}
				}

		url = 'https://api.groupme.com/clients/groups?'
		payload = dict(
					client_id = self.keys['client_id'],
					client_secret = self.keys['client_secret'],
					token = self.token)
		payload = urllib.urlencode(payload)

		resp, content = self.http.request(url+payload, 'POST', json.dumps(spec))

		return content

	def post_line(self, group_id, line_text):

		#POST https://api.groupme.com/clients/groups/GROUP_ID/lines
		#	?client_id=YOUR_CLIENT_ID
		#	&client_secret=YOUR_CLIENT_SECRET
		#	&token=YOUR_ACCESS_TOKEN
		#{
		#	line : {
		#		source_guid	:	"YOUR_GUID_HERE",
		#		text		:	"Hello world",
		#		picture_url	:	null,
		#		location	:	{
		#			lat                    : "40.738206",
		#			lng                    : "-73.993285",
		#			name                   : "GroupMe HQ",
		#			foursquare_venue_id    : "1234567890",
		#			foursquare_checkin     : true
		#		}
		#	}
		#}

		spec =	{'line': 
					{
						'source_guid': str(uuid.uuid1()),
						'text': line_text,
						#'picture_url': '',
						#'location': ''
					}
				}

		url = 'https://api.groupme.com/clients/groups/%s/lines?' % group_id
		payload = dict(
					client_id = self.keys['client_id'],
					client_secret = self.keys['client_secret'],
					token = self.token)
		payload = urllib.urlencode(payload)

		resp, content = self.http.request(url+payload, 'POST', json.dumps(spec))

		return content


if __name__ == "__main__":

	auth = auth()
	token = auth.request_token()
	print token

	interact = interact(token)


	# check basic interaction

	#print interact.list_groups()
	#print interact.check_membership(1434247)
	#print interact.list_lines(1434247)


	# create new group:

	membs = [
				{
					'name': 'lie-bot',
					'user_id': '2523951'
				},
				{
					'name': 'matt',
					'user_id': '53878'
				}		
			]

	#print interact.create_group('devgroup', membs)


	# interact with that group

	group_id = 1452503
	print interact.list_lines(group_id)
	print interact.post_line(group_id, 'hello to u!')
