# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 11:04:51 2025

@author: Cole
"""

import string

digits36 = string.digits + string.ascii_uppercase

# "borrowed" from tutorial
def dec2base(q, base):
    n = ''
    while q != 0:
        q, r = divmod(q, base)
        n = digits36[r] + n
    return n if len(n) > 0 else '0'

"""
This is a part implementation of a prmitive TODO LIST program.
- It takes in a list of unknown length
- Each index corresponds to a given task
- The user should be able to scroll through the entire list, one index at a time
- On reaching the end of the list, the program should return to the start of the list
"""

joblist = [
    "Complete KIT103 Assignment",
    "Go to gym",
    "Seriously, complete the assignment",
    "Pet an animal",
    "Caffeinate",
    "You still haven't done the assignment have you"
    # Plus whatever other jobs you have
    ]

def todo(jobs):
    stop = False
    
    while (not stop):
        selection = input("Enter (N)ext or (S)top : ")
            

"""
Q1 - What is the result of 45 % 7
"""

q1 = 0

"""
Q2 - Check your resulting answer using an appropriate function (Hint: look up!):
"""

q2 = 0

"""
Q3 - Convert one way to verify the first part, and convert the other way to verify the second part
"""

q3a = 0

q3b = 0

"""
Q4 - Check which number is larger using the int() function and either "<" or ">" depending on what your answer was
"""

q4a = 0

q4b = 0

q4c = 0