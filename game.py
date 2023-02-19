#!/bin/python
from colorama import Fore, Back  


lights = {}

for i in range(100):
    
    lights[i] = False


for person in range(100):
    
    for light in range(100):
        
        if  (light+1) % (person+1) == 0:
            lights[light] = not lights[light]


for i in range(len(lights)):

    if lights[i] == True:
         print(Back.YELLOW + Fore.BLACK + '{0: >2}'.format(str(i+1)), end="")

    else:
         print(Back.BLACK + "⚪", end="")

    if (i+1) % 10 == 0:
        print(Back.BLACK + " ")

