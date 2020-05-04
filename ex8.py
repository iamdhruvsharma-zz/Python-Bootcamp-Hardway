# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:39:02 2020

@author: DXT
"""

print("{} {} {}".format('1', '2', '3'))

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your", 
                       "Own text here",
                       "Maybe a poem",
                       "Or a song about fear"
                       ))

