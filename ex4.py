# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:55:13 2020

@author: DXT
"""
# Assigning varible named car a value of 100
# The = (single-equal) assigns the value on the right to a variable on the left.
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passenger_per_car, "in each car.")