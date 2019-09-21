def maxSubArray(nums) -> int:
    largest = -float('inf')
    prev = 0
    for cur in nums:
        cur += prev
        if cur > largest:
            largest = cur
        if cur > 0:
            prev = cur
        else:
            prev = 0
    return largest
        

inputs = [[1], [1,2], [1, -1, 2], [2, -1, 2], [3, -1, -1, 3],
        [3, -1, -1, -1, 4], [-1], [-1, -3]]
answer = [1, 3, 2, 3, 4, 4, -1, -1]

for i, a in zip(inputs, answer):
    output = maxSubArray(i)
    if output == a:
        print("Correct")
    else:
        print("Wrong")



