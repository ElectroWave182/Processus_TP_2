from signal import *

def traitement(numero, frame):
    print("le temps imparti est écoulé")
    exit()

def entree(numero, frame):
    _ = False

alarm(3)
signal(SIGALRM, traitement)

print("entrez un nombre :")
nb = input()
if nb.isdigit():
    signal(SIGALRM, entree)
    print("bravo")
