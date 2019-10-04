def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        ''' move big numbers to the right '''
        ''' move small numbers to the left '''
        left_bounds = cur = 0
        right_bounds = len(nums) - 1
        while cur <= right_bounds:
            if nums[cur] == 0:
                nums[left_bounds], nums[cur] = nums[cur], nums[left_bounds]
                left_bounds += 1
                cur += 1
            elif nums[cur] == 2:
                nums[right_bounds], nums[cur] = nums[cur], nums[right_bounds]
                right_bounds -= 1
            else:
                cur += 1
nums_list = [[0], [0, 1], [1, 1, 0], [2, 1, 0], [2, 2, 2],[2, 2, 0]]
for num in nums_list:
    sortColors(num)
    print(num)

    ''' This problem gave me trouble. I couldn't realise that I needed to keep
    track of boundaries and move the boundaries once the right piece was in
    place. Its like bubble sort, once the greatest number is in place, -1 to the
    boundary. In this case, I know the what the bounds are and what hsould be in
    place. if its this number move it to that bound, if its that number move it
    to the other bound. Though this only works with three numbers, What happens
    when there is another? Do i make a bounds for that number too?'''
