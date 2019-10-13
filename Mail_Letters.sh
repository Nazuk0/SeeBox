#!/bin/sh

time=`python takephoto.py`
mpack -s NewLetterInSeeBox /home/pi/Desktop/SeeBox/$time seeboxtransverse@gmail.com 
rm $time
