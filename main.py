from unittest import case
from fonctions import *
from config import *


#Titre
lcd.clear()
lcd.putstr("BRIGHT'S SMART TRASH")
lcd.move_to(4,1)
lcd.putstr("POUBELLE: ")
lcd.move_to(15,1)
lcd.putstr("FERMEE")
while True:
    #jeux de lumières du ruban
    jeuleds(ruban_led)
    #allumer la série de leds vertes
    allumerled(led)
    
    
    #si un capteur détecte une proximité
    if(c1.value==0 | c2.value()==0 |c3.value()==0):
        #ouvrir la poubelle en faisant passant le ruban en couleur bleue
        ouverture(servo3,ruban_led)
        #initialisation de la valeur du bac en question
        bac=""
        #affectation de la valeur à evaluer
        value=0
        value = 1 if c1.value()==0 else 2 if c2.value()==0 else 3 if c3.value()==0 else 0
        
        match value:
            case 1:
                bac="1"
                #aaffichage à l'ecran du bac en question
                etat(lcd,bac)
                #ajustement des servomoteurs pour laisser passer l'objet jeté
                servo1.write_angle(40)
                servo2.write_angle(90)
            case 2:
                bac="2"
                #aaffichage à l'ecran du bac en question
                etat(lcd,bac)
                #ajustement des servomoteurs pour laisser passer l'objet jeté
                servo1.write_angle(90)
                servo2.write_angle(90)
            case 3:
                bac="3"
                #aaffichage à l'ecran du bac en question
                etat(lcd,bac)
                #ajustement des servomoteurs pour laisser passer l'objet jeté
                servo1.write_angle(90)
                servo2.write_angle(40)
        #fermer la poubelle en faisant passant le ruban en couleur rouge
        fermeture(servo3,ruban_led)
    
    
    
        
        
    
    
    
