#!/bin/sh

time=`python takephotoPackage.py`
mpack -s NewPackagesInSeeBox /home/pi/Desktop/SeeBox/$time seeboxtransverse@gmail.com
rm $time
