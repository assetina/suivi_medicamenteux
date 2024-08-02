from machine import Pin
from time import sleep_ms, sleep
import dht
from servo import Servo
from machine import SoftI2C
from ecran.lcd_api import LcdApi
from ecran.i2c_lcd import I2cLcd
Liste2= ["rouge", "vert", "bleu", "blanc","bleu clair","jaune","violet","noir", "rouge-orange","gold","marron","gris","vert foncé","corail"]
Liste3= [[255,0,0], [0,255,0], [0,0,255], [255,255,255],[0,255,255],[255,255,0],[255,0,255],[0,0,0],[255,69,0],[255,215,0],[165,42,42],[126,126,126],[0,100,0],[255,127,80]]

    
#Allumer la led  
def allumerled(led):
    led.on()
    
#Eteindre la led  
def eteindreled(led):
    led.off()

#methode pour ouvrir la poubelle
def ouverture(servo3,ruban_led):
    #Faire passer le ruban au bleu
    ruban_bleu(ruban_led)
    #l'angle sera défini plus tard pour l'ouvertue de la poubelle
    servo3.write_angle(90)
    
    


#methode pour fermer la poubelle
def fermeture(servo3, ruban_led):
    #un autre angle sera défini pour la fermeture
    servo3.write_angle(90)
    #Faire passer le ruban au rouge
    ruban_rouge(ruban_led)
    
    
#PRINCIPALE
"""def principale(c1,c2,c3,servo1,servo2,servo3,lcd,ruban_led):
    #Faire passer le ruban au bleu
    ruban_bleu(ruban_led)
    #l'angle sera défini plus tard pour l'ouvertue de la poubelle
    servo3.write_angle(90)
    sleep(5)
    #un autre angle sera défini pour la fermeture
    servo3.write_angle(90)
    bac=""
    if(c1.value()==0):
        bac="1"
        etat(lcd,bac)
        servo1.write_angle(40)
        servo2.write_angle(90)
    if(c2.value()==0):
        bac="2"
        etat(lcd,bac)
        servo1.write_angle(90)
        servo2.write_angle(90)
    if(c3.value()==0):
        bac="3"
        etat(lcd,bac)
        servo1.write_angle(90)
        servo2.write_angle(40)
    
""" 

#pour definir si la poubelle est ouverte ou fermée
def etat(lcd,bac):
    lcd.move_to(15,1)
    lcd.putstr("OUVERTE")
    lcd.move_to(5,2)
    lcd.putstr("BAC: "+bac)
    lcd.move_to(4,3)
    lcd.putstr("VEUILLEZ PATIENTER")
    

def jeuleds(ruban_led):
    for i in Liste3:
        for j in range(ruban_led.len()):
            ruban_led[j]= tuple(i)
        ruban_led.write()
    
def fin(lcd):
    lcd.move_to(4,3)
    lcd.putstr("TRI TERMINE: MERCI!")
    
def ruban_rouge(ruban_led):
    for j in range(ruban_led.len()):
        ruban_led[j]= tuple(Liste3[0])
        ruban_led.write()


def ruban_bleu(ruban_led):
    for j in range(ruban_led.len()):
        ruban_led[j]= tuple(Liste3[2])
        ruban_led.write()
        
def ruban_vert(ruban_led):
    for j in range(ruban_led.len()):
        ruban_led[j]= tuple(Liste3[1])
        ruban_led.write()
        
        
def gps(gps):
    if uart.any():  # si nous avons reçu quelque chose...
        donnees_brutes = str(uart.readline())
        for x in donnees_brutes:
            gps.update(x)

        print('Latitude: ' ,gps.latitude_string())
        print('Latitude (tuple): ' , gps.latitude)
        print('Longitude: ' ,gps.longitude_string())
        print('Longitude (tuple): ' , gps.longitude)
        print('Altitude: ' , gps.altitude)
        print('Vitesse: ', gps.speed_string('kph'))
        print('Date: ' , gps.date_string('s_dmy'))
        print('')
        url = 'https://www.google.com/maps/search/?api=1&query=' +gps.latitude_string() + ',' + gps.longitude_string()
        print(url)


def mettre_en_veille(led,temps):
    # Mettre l'ESP32 en veille pendant 5 secondes
    print("Mise en veille de l'ESP32...")
    machine.deepsleep(temps)
    #Eteindre les leds vertes
    eteindreled(led)

def reveiller(led):
    # Réveiller l'ESP32
    print("Réveil de l'ESP32...")
    machine.reset()
    #Allumer les leds vertes
    allumerled(led)
    
    
def connection(username,password):
    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print('en cours de connexion...')
        open()
        sta_if.active(True)
        #sta_if.connect('atmyhome', 'home4internet')
        sta_if.connect(username, password)
        while not sta_if.isconnected():
            sta_if.disconnect()
            #pass

    print('connecté:', sta_if.ifconfig())