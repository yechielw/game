#!/bin/python

lights = {}

for i in range(100):
    
    lights[i] = False


for person in range(100):
    
    for light in range(100):
        
        if  (light+1) % (person+1) == 0:
            lights[light] = not lights[light]


for i in range(len(lights)):

    if lights[i] == True:
        print("🟡", end="")

    else:
        print("⚫", end="")

    if (i+1) % 10 == 0:
        print()

