# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 11:04:51 2025

@author: Cole
"""

import time

"""
This is a part implementation of a VERY primitive hash function.
This function takes in an arbitrary array of integers, and sorts them into buckets based on their value mod n.
The output variable is a list of length (mod) where each index has a list that can be append()'ed to.
This is similar to a hash table, but in a far more primitive way.
    - Your job is to implement the rest of the function

"""

def modular_sort(input, mod):
    output = [set() for _ in range(mod)]

# Test data
numbers = [15, 3, 8, 22, 7, 10]
modulus = 5

"""
This is a part implementation of a clock.
It uses the datetime.now() function to get the UNIX Time Epoch
    - It is your job to format that into readable time parseable by us mere mortals.

"""

def clock():
    while True:
        seconds_in_day = 86400
        seconds_in_hour = 3600
        seconds_in_minute = 60
        
        # Get seconds since midnight (UTC+10+Daylight Savings)
        seconds_today = int(time.time)

        hours = 0
        minutes = 0
        seconds = 0
        
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}\r", end='')
        time.sleep(1)

"""
This is a part implementation of a prmitive date calculator.
The function starts at 12, 12, which for our purposes is known to be a Monday.
    - Your job is to implement the rest of the function
    - Starting at 12/12, and taking in an arbitrary amount of days from the user, calculate what day, month, and weekday the resulting addition would be

"""

def date_manager():
    # Days in each month (not handling leap years)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Start date: Dec 12 (Monday)
    day = 12
    month = 12
    weekday = 0
    
    print(f"Start date: {days_of_week[weekday]}, {day:02d}/{month:02d}")
    
    add_days = input("Enter number of days to add: ")
    month_tracker = 0
    
    while True:
        if something:
            doSomething
        else:
            break
        
    # Calculate new weekday + month
    month = 0
    day = 0

    new_weekday = 0
    print(f"New date: {days_of_week[new_weekday]}, {day:02d}/{month:02d}")