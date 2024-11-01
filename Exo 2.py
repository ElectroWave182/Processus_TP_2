from signal import *

def traitement(numero, frame):
    _ = False

signal(SIGINT, traitement)
while True:
    _ = False
