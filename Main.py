# -*- coding: utf-8 -*-
#Main.py

#Import des modules
from LED import GreenLED_On
from LED import GreenLED_Off
from LED import OrangeLED_On
from LED import OrangeLED_Off
from LED import RedLED_On
from LED import RedLED_Off

import RPi.GPIO as GPIO
import subprocess
import time

#Initialisation de la numérotation et des E/S
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14,GPIO.IN)  #Captor Hall Effect
GPIO.setup(15,GPIO.IN)  #Captor Letter
GPIO.setup(18,GPIO.IN)  #Captor Package

#PIN
Back_Door = 14
Letter = 15
Package = 18

#Variables
vert = 0
orange = 0
Nb_lettres = 0
Nb_lettres_T = 0
Nb_colis = 0
Nb_colis_T = 0

while True:
    #Vérifie que la porte arrière est fermée
    while(GPIO.input(Back_Door) == False):
        print("Back door is closed")
        #Vérifie aucun contenu
        if ((vert == 0) and (orange == 0)):
            RedLED_On()
            GreenLED_Off()
            OrangeLED_Off()

        #Vérifie arrivé lettres ou colis
        state_letter = GPIO.input(Letter)
        state_package = GPIO.input(Package)

        if(state_letter == False):
            vert = 1
            Nb_lettres += 1
        if(state_package == True):
            orange = 1
            Nb_colis += 1


        #Conséquence de contenu
        if(vert == 1):
            RedLED_Off()
            GreenLED_On()
            if(Nb_lettres>Nb_lettres_T):
                subprocess.call(["/home/pi/Desktop/SeeBox/Mail_Letters.sh"], shell=True)
                Nb_lettres_T = Nb_lettres
            time.sleep(0.04)
            print("Vous avez du courrier:",Nb_lettres)
            print("Vous avez des colis:",Nb_colis)

        if(orange == 1):
            if(Nb_colis>Nb_colis_T):
                subprocess.call(["/home/pi/Desktop/SeeBox/Mail_Packages.sh"], shell=True)
                Nb_colis_T = Nb_colis
            RedLED_Off()
            OrangeLED_On()
            time.sleep(0.04)
            print("Vous avez du courrier:",Nb_lettres)
            print("Vous avez des colis:",Nb_colis)
        
    #RAZ
    vert = 0
    orange = 0
    Nb_lettres = 0
    Nb_lettres_T = 0
    Nb_colis = 0
    Nb_colis_T = 0
    

#run a program
#sudo python /path/to/file.py
