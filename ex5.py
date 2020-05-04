# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:03:24 2020

@author: DXT
"""

name = 'Mr. X'
age = 35 # not a lie
height = 74 # inches
height_centi = height*2.54
weight = 180 # lbs
weight_kilo = weight/2.2046
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")