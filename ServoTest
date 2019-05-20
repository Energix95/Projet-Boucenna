import serial
import time
from Maestro import maestro

servo = maestro.Controller()

print("Veuillez choisir une expression :") 

choix = int(input("1. Neutre\n2. Joie\n3. Triste\n4. Surpris\n5. Colère"))

if(choix == 1) :
        print("Vous aves choisi l'expression Neutre")

        servo.setAccel(0,50)
        servo.setTarget(0,6000)

        time.sleep(1)

        servo.setAccel(0,50)
        servo.setTarget(0,1000)


if(choix == 2) :
        print("Vous avez choisi l'expression Joie")

if(choix == 3) :
        print("Vous avez choisi l'expression Triste")
        
if(choix == 4) :
        print("Vous avez choisi l'expression Surpris")
        
if(choix == 5) :
        print("Vous avez choisi l'expression Colère")
servo.close()


