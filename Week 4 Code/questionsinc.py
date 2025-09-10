# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 05:48:54 2025

@author: Cole
"""

from itertools import product

def main():
    ANSWER_COLLECTION = list()
    
    #######################################################
    
    q1 = { x for x in range( 1, 5 ) if x % 2 == 0}
    
    ANSWER_COLLECTION.append(q1)
    
    #######################################################
    
    q2a = {x for x in range( 7, 10 ) } 
    q2b = { 1, 2, 3 }
    
    ANSWER_COLLECTION.append( 3 * len(q2a) )
    
    #######################################################
    
    q3a = { 1,9,3,7,2,4,2 }
    q3b = { 1,2,3 }
    
    ANSWER_COLLECTION.append(q3a or q3b)
    ANSWER_COLLECTION.append(q3a.union(q3b))
    
    #######################################################
    
    q4a = { 1,9,3,7,2,4,2 }
    q4b = { 1,2,3 }
    
    ANSWER_COLLECTION.append(q4a and q4b)
    ANSWER_COLLECTION.append(q4a.intersection(q4b))
    
    #######################################################
    
    q5a = { 9,7,1,5,9,1,3 }
    q5b = { a for a in range (0, 10) if a % 2 == 1 }
    
    ANSWER_COLLECTION.append(q5a.issubset(q5b))
    ANSWER_COLLECTION.append(q5a < q5b)
    
    #######################################################
    
    q6a = { 3,8,4,3,1 }
    q6b = { 1,2,3,5,9 }
    
    ANSWER_COLLECTION.append(q6a ^ q6b)
    
    #######################################################
    """
    
    q7a = ???
    q7b = ???
    q7c = ???
    
    ANSWER_COLLECTION.append(???)
    ANSWER_COLLECTION.append(???)
    
    ANSWER_COLLECTION.append(???)
    ANSWER_COLLECTION.append(???)
    
    #######################################################
    """
    
    return ANSWER_COLLECTION