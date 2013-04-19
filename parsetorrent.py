#!/usr/bin/python
from bencode import *
from sys import argv

if len(argv) < 2:
	print 'specify the name of torrent file'
	exit()

# open file
tf = open(str(argv[1]), 'rb')
# read info
tinfo = bdecode(tf.read())
for key, value in tinfo.iteritems():
	print key, ':'
	if (isinstance(value, list)):
		for x in value:
			print '\t', x
	elif (isinstance(value, dict)):
		for x, y in value.iteritems():
			y = str(y)
			print '\t', x, ':', y if len(y) < 60 else y[:60]
	else:
		print '\t', value

tf.close()