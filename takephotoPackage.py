#!/usr/bin/python

import sys
import os
import subprocess
import timestamp
from timestamp import *
from subprocess import call

def photo():
	time=timestamp.getTime()
	subprocess.call(['raspistill -t 7000 -o ' + time], shell=True)
	print(time)
	return time

if __name__== "__main__":
	photo()
