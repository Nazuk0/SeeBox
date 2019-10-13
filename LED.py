# -*- coding: utf-8 -*-
#LED.py

import RPi.GPIO as GPIO
import time

#GPIO = Genral Purpose Input Output
#BCM = Broadcom SOC référence au pin de la Raspberry
#GPIO.setup(num_branchement;GPIO.etat)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2,GPIO.OUT)  #Green
GPIO.setup(3,GPIO.OUT)  #Orange
GPIO.setup(4,GPIO.OUT)  #Red

Green = 2
Orange = 3
Red = 4

def RedLED_On():
    GPIO.output(Red,True)
    print("RED_ON")

def RedLED_Off():
    GPIO.output(Red,False)
    print("RED_OFF")

def OrangeLED_On():
    GPIO.output(Orange,True)
    print("ORANGE_ON")

def OrangeLED_Off():
    GPIO.output(Orange,False)
    print("ORANGE_OFF")

def GreenLED_On():
    GPIO.output(Green,True)
    print("GREEN_ON")

def GreenLED_Off():
    GPIO.output(Green,False)
    print("GREEN_OFF")


    