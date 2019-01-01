# -*- coding: utf-8 -*-
"""
Created on Tue Jan 01 11:34:40 2019

@author: admin
"""

import random
computer_number = random.randint(1, 100)
print(computer_number)


def is_same(target, number):
    if target == number:
        result="Win"
    elif target > number:
        result="Low"
    else:
        result="High"
    return result

print("Hi.\nI chose a number between 1 and 100.")

guess = int(input("Please write a number in your mind and press enter. :   "))

higher_or_lower = is_same(computer_number, guess)

while higher_or_lower !="Win":
    if higher_or_lower == "Low":
        guess = int(input("It is higher. Think again:  "))
    else:
        guess = int(input("It is lower. Think again:   "))
        
    higher_or_lower = is_same(computer_number, guess)
    
input("Right!\n Good job.\n\n\n Press Enter to quit.")
