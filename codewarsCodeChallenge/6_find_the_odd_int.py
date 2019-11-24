# find the odd int 
# Requirements:
#   Given an array, find the int that appears an odd number of times.
#   There will always be only one integer that appears an odd number of times.
#   
# Input: [1, 2, 2]
# Process:
#   approach one: use a set
#       for each number
#       if the number is in the set
#           remove the number from the set
#       else
#           add the number to the set
#   return the first number in the set
# Output: 1

def odd_int(nums) -> int:
    odd = set()
    for n in nums:
        if n in odd:
            odd.remove(n)
        else:
            odd.add(n)
    return odd.pop()

print((odd_int([1, 2, 2]) == 1), 1)
print((odd_int([1, 2, 2, 1, 3]) == 3), 3)
print((odd_int([1]) == 1), 1)
print((odd_int([1, 1, 1]) == 1), 1)
print((odd_int([1, 1, 1 , 2, 2]) == 1), 1)
