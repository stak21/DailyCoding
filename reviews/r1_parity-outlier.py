# Review 1: 12/16/19 8:45
i# Requirements: 
#   Return the odd number out given a list of atleast three integers.
#       There will always be atleast one number that is different
# I/O:
#    [1, 2, 1] => 2
#     [2, 1, 2] => 1
#       [2, 1, 2, 4] => 1
#       [1, 1, 4, 5]
#       [2, 2, 2, 5] =.> 5
#       [1, 2, 2] => 1
#       [1, 1, 2] => 2

# Process:
#   Find the outlier by using the first three numbers
#   iterate through the array looking for the number that is either divisible by 2 or not
#   return that number

#   iterate through the first three numbers
#   if n is even add it to the list
#
#   if len of list == 1 return
#   if > 1 look for odd
#   if none look for even

# iterate through the entire list and use the outlier to find the number

