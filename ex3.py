# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:29:43 2020

@author: DXT

What is the order of operations? 
In the United States we use an acronym called PEMDAS which
stands for Parentheses Exponents Multiplication Division Addition Subtraction. That’s the order
Python follows as well. 

The mistake people make with PEMDAS is to think this is a strict order,
as in “Do P, then E, then M, then D, then A, then S.” The actual order is you do the multiplication
and division (M&D) in one step, from left to right, then you do the addition and subtraction in
one step from left to right. So, you could rewrite PEMDAS as PE(M&D)(A&S).

"""

print("I will now count my chickens:")

# / (Division) has higher precedence over + (Addition)
# https://docs.python.org/3/reference/expressions.html

print("Hens", 25.0 + 30.0 / 6.0)
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print("Now I will count the eggs:")

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3 + 2 < 5 - 7?")

print(3.0 + 2.0 < 5.0 - 7.0)

print("What is 3 + 2?", 3.0 + 2.0)
print("What is 5 - 7?", 5.0 - 7.0)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal?", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)

