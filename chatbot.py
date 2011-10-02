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


phrases = ['ponys.', 'no pizza', 'out of coffee', 'The saddest thing is a homeless man winning the lottery and spending all the money on charities that are fronts for drug smuggling.']
answers = ['hard to tell', 'ask again later', 'TITS OR GTFO', 'how dare you.', 'I will dance on your grave']


current = ''
while True:
	name, text = interact.last_line(1469199)
	if current != str(text):
		print str(name),': ',str(text)
		current = str(text)

	if current == 'Timebot, what is the saddest thing?':
		interact.post_line(1469199, random.choice(phrases))
	elif current[:7] == 'Timebot':
		interact.post_line(1469199, random.choice(answers))

	time.sleep(0.5)
