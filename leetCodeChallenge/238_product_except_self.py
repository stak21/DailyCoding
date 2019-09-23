def productExceptSelf(nums):
        output = []
        total = 1
        for num in nums[:]:
            output.append(total)
            total *= num
        total = 1
        for i, num in enumerate(nums[::-1], start=1):
            output[-i] *= total
            total *= num

        return output

ex = [1,2,3,4]
res = [24,12,8,6]
out = productExceptSelf(ex)
if out == res:
    print('correct')
else:
    print('wrong')

    """
    Note:
        Easy solution is to find the product of all the numbers and iterate
        through again to divide by itself
        Advanced: Iterate through once and multiply the running total and add it
        to the array. Iterate through again, but reversed and do the same thing
    """
