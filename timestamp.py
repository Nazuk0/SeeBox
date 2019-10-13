#!/usr/bin/python

import time
import datetime
import os
import sys

def getTime():
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y-%H:%M:%S')
	newname='Photos/'+st+'.jpg'
	return newname

#sys.exit(newname)

if __name__=='__main__':
	getTime()
