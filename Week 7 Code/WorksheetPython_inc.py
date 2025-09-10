# -*- coding: utf-8 -*-
from itertools import product, permutations
from scipy.special import factorial
"""
Created on Wed Sep 10 11:04:51 2025

@author: Cole
"""

"""
Question 1:

For many years now, airports around the world have been identified with a
simple 3 letter identifier, making pilot communication easier and passenger
confusion grow year on year (i.e. LAX, LHR, SYD, etc.). However, the world
population grows and so does the number of airports, including passenger,
research, and military. The last one being of particular importance.

The US spending budget has increased year over year leading to progressively
more air force bases being built, which has made the US Army worry that, if
they run out of letter permutations, passenger aircraft may start landing at
US Air force bases.

You, as the sole computer scientist working for USGOV, have been tasked with
figuring out how many more stations the US can build assuming there are already
3,572 airports around the world already. 

"""
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# First, represent it mathmatically to check if the generated permutations match the maths
q1a = 26**3

q1b = len([''.join(p) for p in product(alphabet, repeat=3)])

"""
Question 2:

For the iPhone 17, Apple "crack marketing team" has come up with a set of new
buzzwords to apply to their 3 flagship tiers. The first tier will have 1 word,
the second will have 2, and the top range will have 3. The words can be shared
between model lines. Help the marketing execs come up with a timeline of how
long it will take to run all the possible names through focus groups by letting
them know just how many permutations there will be. 

"""
buzzwords = { "Svelte", "Uber",  "Peak", "Apex", "Titan", "Executive" }

q2a = 6 * 6**2 * 6**3

q2b = len([''.join(b) for b in product(buzzwords, repeat=6)])

"""
Question 3:

Given 15 pool balls to a table, how many unique ways can they be racked up?

"""

balls = { "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10", "b11", "b12", "b13", "b14", "b15"}

q3a = factorial(15)/factorial(15 - 15) # or just factorial(15)

#q3b = len({b for b in permutations(balls, 15)}) # this is unsafe to run