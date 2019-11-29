# Requirements: 
#   Atleast 3 integers
#   all the integers are odd or even except for one
#   return the exception
#   we do not need to go through the entire array
#   only until we find the exception
# Input:
#   [1, 3, 2]
#   [2, 4, 6, 10, 1]
#   [2, 1, 4]
#   [2, 2, 1, 4]
# Process:
#   To find the outlier,  we need to know what the other two integers are
#   so minimum we need to iterate through atleast 3 to find the answer
#   Approach1 - 
#   get the sum of the first three numbers to find what the outlier is
#   sorting doesn't matter, so we would need to iterate through theentire array
#   find the number that is divisible by the odd or even 
#   Approach2 - 
#   iterate through the array
#   add each number, if the number is  the outlier
#   approach 2 does not work because adding two odd numbers == even

# Notes:
#   2 + 4 + 3
#   3 + 1 + 2

# approach 1
def parity_outlier(arr) -> int:
     def outlier_is_even(arr):
        if (arr[0] + arr[1]) % 2 == 0:
            return arr[0] % 2 != 0
        return sum(arr) % 2 == 0

    outlier_is_even = outlier_is_even(arr[0:3])
    for n in arr:
        if outlier_is_even:
            if n % 2 == 0:
                return n 
        else:
            if n % 2 != 0:
                return n

tests = [[1, 3, 2], [2, 1, 3], [2, 1, 4, 6], [2, 4, 1, 6]]
answers = [2, 2, 1, 1]
for test, answer in zip(tests, answers):
    res = parity_outlier(test)
    print(res, 'Success: ', res == answer)