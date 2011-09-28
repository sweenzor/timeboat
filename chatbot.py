#! /usr/bin/python

import time
import ConfigParser

import groupme

auth = groupme.auth()
token = auth.request_token()
interact = groupme.interact(token)

config = ConfigParser.ConfigParser()
config.read('keys.cfg')
keys = config.items('groups')
keys['group_id']




current = ''
while True:
	name, text = interact.last_line(1452503)
	if current != str(text):
		print str(name),': ',str(text)
		current = str(text)

	time.sleep(0.5)
