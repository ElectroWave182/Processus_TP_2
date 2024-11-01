from os import *
from signal import *

def traitement(numero, frame):

    if numero == 10:
        print("réception d'un signal de numéro", numero)

    elif numero == 12:
        print("nouvelle réception d'un signal de numéro", numero)

signal(SIGUSR1, traitement)
signal(SIGUSR2, traitement)
while True:
    _ = False
