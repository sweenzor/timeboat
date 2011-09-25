#! /usr/bin/python

import time

current = ''
while True:
	fid = open('chatsim.txt', 'r')
	lines = fid.readlines()
	if current != lines[-1]:
		print lines[-1]
		current = lines[-1]

	fid.close()
	time.sleep(0.2)