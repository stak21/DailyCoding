""" Brute force 
def two_sum(nums, target):
    for count1, i in enumerate(nums):
        for j in range(count1 + 1, len(nums)):
            if (i + nums[j]) == target:
                return [count1, j]

print(two_sum([1,2,3, 10], 12))
"""

""" Hash pass """
def two_sum(nums, target):
    h = {}
    for count, i in enumerate(nums):
        h[i] = count

    for count, j in enumerate(nums):
        dif = target - j
        found = h.get(dif)
        
        if found and found != count:
            return [count, found]

print(two_sum([1,2,3, 10], 12))
print(two_sum([3,1,13, 10], 16))
print(two_sum([1,2,23, 10], 33))
