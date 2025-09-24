# -*- coding: utf-8 -*-
from scipy.special import comb, factorial, perm
from math import gcd, lcm
"""
Created on Wed Sep 10 11:04:51 2025

@author: Cole
"""

# "Borrowed" from tutorials
def check_divisibility(n):
    for m in [2, 3, 4, 5, 7, 9, 11]:
        print(f'{m}|{n}? {"yes" if n % m == 0 else "no"}')

"""
Q3 – Determine the GCD and LCM of the 2 following pairs using either the IPython terminal, or your own strategy:
    # NOTE: Feel free to skip this step if you used IPython to answer this segment
"""
    
q1 = [36, 87]

q1aGCD = gcd(q1[0], q1[1])
q1aLCM = lcm(q1[0], q1[1])


q2 = [512, 1024]

q1bGCD = gcd(q2[0], q2[1])
q1bLCM = lcm(q2[0], q2[1])


q3 = [3599, 9282]

q1bGCD = gcd(q3[0], q3[1])
q1bLCM = lcm(q3[0], q3[1])


"""
Q2 – Given the integer 5,495,693,092, determine some numbers it can be evenly divided into using the Divisibility Rules

"""

q2a = check_divisibility()
print("\n")
q2b = check_divisibility()


"""
Q3 – Given a subset of people, say 495 and 693 that need to be split into even teams, how would you calculate the largest
team occupancy count with the affect of minimising team count? What would that resulting team occupancy count be?
"""

q3 = 0


"""
Question 4 - EXTENSION:

A) Given a combination lock with a cmobination of length 3 and 40 numbers, and assuming without replacement,
   how many combinations can be made?

B) Assuming that it were actually true to its name, how many would there be then?

"""

q4amath = 0

q4apython = 0

q4bmath = 0

q4bpython = 0