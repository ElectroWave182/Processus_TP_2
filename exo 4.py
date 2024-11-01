from os import *
from signal import *
from time import *

global pid

def traitement_1 (numero, frame):
    print("ping")
    sleep(1)
    kill(pid, 10)

def traitement_2 (numero, frame):
    print("pong")
    sleep(1)
    kill(pid, 10)

num = fork()

if num != 0:
    pid = num

    signal(SIGUSR1, traitement_1)
    sleep(1)
    kill(pid, 10)

else:
    pid = getppid()

    signal(SIGUSR1, traitement_2)

while True:
    sleep(1)