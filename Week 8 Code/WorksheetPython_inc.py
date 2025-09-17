# -*- coding: utf-8 -*-
from itertools import product, permutations, combinations, combinations_with_replacement
from scipy.special import comb, factorial, perm
"""
Created on Wed Sep 10 11:04:51 2025

@author: Cole
"""

"""
Question 1:

Unfortunately for the land of the free, their political system has collapsed completely which has not
come as a shock to anyone. This means that it needs to be rebuilt from the ground up and there are a
lot of people vying for the lifetime role of Sitting Justice on the Supreme Court and all the power
that affords their flavour of political party. However, out of a possible 47 final round candidates,
only 9 can get in. How many different combinations of those candidates can make it in?

"""

# First, represent it mathmatically to check if the generated permutations match the maths
q1math = 0

q1python = 0

"""
Question 2:

For the iPhone 17, Apple “crack marketing team” has come up with a set of new buzzwords to apply to
their 3 flagship tiers. The first tier will have 1 word, the second will have 2, and the top range
will have 3. The words can be shared between model lines. Help the marketing execs come up with a
timeline of how long it will take to run all the possible names through focus groups by letting them
know just how many combinations there will be.

*To make this truer to life, I recommend conducting 1 equation for each tier of iPhone and summing
the total of all of the combinations for each model line.

"""
buzzwords = { "Svelte", "Uber",  "Peak", "Apex", "Titan", "Executive" }

q2math = 0

q2iPhoneBase = 0
q2iPhoneMidrange = 0
q2iPhoneTop = 0

q2total = 0

"""
Question 3:

In Tasmania, license plates often follow the pattern of [A-Z] [ A-Z]- [0-9] [0-9] [0-9] [0-9],
or 2 letters, 4 numbers. Examining this entirely in a vacuum excluding all other metadata and
specifics included with plate allocation, how many cars may operate on Tasmanian roads at any
given time given the pattern above?

"""

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

q3math = 0

q3python = 0

"""
Question 4:

A) Given a combination lock with a cmobination of length 3 and 40 numbers, and assuming without replacement,
   how many combinations can be made?

B) Assuming that it were actually true to its name, how many would there be then?

"""

q4amath = 0

q4apython = 0

q4bmath = 0

q4bpython = 0