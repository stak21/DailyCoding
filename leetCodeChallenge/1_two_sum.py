""" Brute force 
def two_sum(nums, target):
    for count1, i in enumerate(nums):
        for j in range(count1 + 1, len(nums)):
            if (i + nums[j]) == target:
                return [count1, j]

print(two_sum([1,2,3, 10], 12))
"""
def two_sum(nums, target):
    """ Hash two pass """
    """
        h = {}
        for count, i in enumerate(nums):
            h[i] = count

        for count, j in enumerate(nums):
            dif = target - j
            found = h.get(dif)
            
            if found and found != count:
                return [count, found]
    """
    """ Hash one pass attempt 1 """
    """
        h = {}
        for count, i in enumerate(nums):
            dif = target - i
            found = h.get(dif)
            h[i] = count
            if (found or found == 0) and found != count:
                return [found, count]
    """

    """ attempt 2 """
    h = {}
    for count, i in enumerate(nums):
        dif = target - i
        if dif in h:
            return [h[dif], count]
        else:
            h[i] = count


print(two_sum([1,2,3, 10], 12))
print(two_sum([3,1,13, 10], 16))
print(two_sum([1,2,23, 10], 33))
