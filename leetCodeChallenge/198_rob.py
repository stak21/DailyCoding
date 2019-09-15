def rob(nums):
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        a, b, c= 0, 1, 2
        temp = nums[0]
        while c < len(nums):
            nums[c] += temp
            temp = max(nums[a], nums[b])
            a += 1
            b += 1
            c += 1
        return max(nums[a], nums[b])

""" Things I did wrong:
    I didn't check for null
    I checked the index instead of the array[inx]
"""
li = [1,2,3,4]
print(rob(li))
