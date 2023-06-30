# Codewars Challenges

# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

# My Solution:

def maps(arr):
    new_arr = []
    for i in arr:
        new_arr.append(i * 2)
    return new_arr