#!/usr/bin/python
# multiples of 3 and 6
# Requirements:
#  return the sum of numbers that are a multiple of 3 and 5 given a number
#   number that is both multiple of 3 and 5 only ocunts once
#   the numbers counted should be < the given number
#   if < 3 return 0
#   iterate through every number
# Input: 10
# Process: 
# 3 + 6 + 9 + 5
# iterate through each number as n
# if n is divisible by 3 or 5
# store that number in a list
# return the sum of the list
# Output: 23

def sum_of_multiples(num: int) -> int:
    if num < 3:
        return 0
    return sum([n for n in range(num) if n % 3 or n % 5])

print(sum_of_multiples(10))
