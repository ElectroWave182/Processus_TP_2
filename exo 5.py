from os import *
from time import *
from signal import *

global cpt
cpt = int(input())

def traitement(numero, frame):
    print("je m'exécute pendant 1 seconde")
    cpt = 1

signal(SIGUSR1, traitement)

while True:
    if cpt == 0:
        kill(getpid(), 2)

    else:
        cpt -= 1
        sleep(1)