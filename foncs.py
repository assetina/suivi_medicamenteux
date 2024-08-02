from machine import Pin
from time import sleep_ms, sleep

#Allumer la led  
def allumerled(led):
    led.on()
    
#Eteindre la led  
def eteindreled(led):
    led.off()
    
    
#Allumer le buzzer  
def allumerbuzzer(buzzer):
    buzzer.on()
    
#Eteindre le buzzer  
def eteindrebuzzer(buzzer):
    buzzer.off()