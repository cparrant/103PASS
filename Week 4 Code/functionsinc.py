# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:42:58 2025

@author: Cole
"""

'''
FUNCTION 1

This is a warmup function, it takes in a value, and returns the value multiplied by 3.
'''
def function1 (y):
    return 1 # REMOVE ME



'''
FUNCTION 2


This function takes in a set, and returns the cardinality of the set

NOTE - This function is designed not to use any external libraries or functions
See if you can make it work yourself!

Bonus - assuming that the input is a set of real numbers, what is the co-domain of this function? : 
'''
def function2 (y):
    return 1



'''
FUNCTION 3


This function is a Generator

This function takes in a set of values (y), and yields the absolute value of every element in the set.
i.e.: f(x) -> abs(x)

For this one, you can just use the built-in abs() function if you really want,
but you can also write your own version of it, if you're feeling ambitious.

(NOTE: The negative of a negative is...
       Two wrongs make a...)
'''
def function3 (y):
    yield 1



'''
FUNCTION 4

This function takes in a set of values (y), and returns only the set of values that have a factorial greater than 100.

You also need to implement a function to get that factorial.

As a bonus - is this function onto or one-to-one? :
'''
def function4 (y):
    x = set()
    
    return x

def factorial(n):
    result = 1
    
    return result



'''
FUNCTION 5

This function takes in a set of values (y), and returns the set of values that are prime.
'''
def function5 (y):
    output = set()
    isPrime = True
                
    return output
    
    
    
example = {-15, 2, 89, 1, 2, 3, -23, 15, 5}

# Just to be difficult, for function 1 and 3, you have to include them in a set comprehension!

a = # COMPLETE ME
b = function2(example)
c = # COMPLETE ME
d = function4(example)
e = function5(example)

print("A: ", a, "\nB: ", b, "\nC: ", c, "\nD: ", d, "\nE: ", e)