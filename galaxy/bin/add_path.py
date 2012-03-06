#!/usr/bin/python

import os
import sys

print os.getcwd()
new_line = os.getcwd()

#f = file("/home/galaxy/bin/aa", "r")

try:
	f = file("/home/galaxy/bin/aa", "a")
	f.write("echo %s\n" % new_line)
	print "New line writte: %s" % new_line
except Exception, e: print e; sys.exit(-1)


#content = f.read()
#print content
