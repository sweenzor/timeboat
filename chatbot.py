#! /usr/bin/python

import time
import ConfigParser
import random

import groupme

auth = groupme.auth()
token = auth.request_token()
interact = groupme.interact(token)

config = ConfigParser.ConfigParser()
config.read('keys.cfg')
keys = config.items('groups')


phrases = ['ponys.', 'no pizza']


current = ''
while True:
	name, text = interact.last_line(1452503)
	if current != str(text):
		print str(name),': ',str(text)
		current = str(text)

	if current == 'Liebot, what is the saddest thing?':
		interact.post_line(1452503, random.choice(phrases))
		
	time.sleep(0.5)
