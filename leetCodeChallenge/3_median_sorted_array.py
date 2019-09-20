class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #         // two sorted arrays of size m, n
        #         // find the median, O(log (m+n))
        #         // median is the middle ish value
        #         // if the median has two numbers, divide it by 2 and that will be the result
        #         // typically log n is divide and conqeur approach
        #         // One idea would be to merge the two arrays and find the middle
        #         // two 
        #         // I have to figure out how to find the middle value
        #         // Because I have the length I can 
        #         // [1, 2, 3]
        #         // [5, 6]
        #         // n2 is smaller so start adding from there
        #         // get the middle value of n1 -> 2
        #         // get the first number of n2 and from there use dnc to figure out where to place it 
        #          // once i am finished going through the list, get the middle number if its odd and the middle two numbers if it is even and divide it by 2
        
        def findIndex(num, nums):
            mid = len(nums) // 2
            if len(nums) < = 2:
                
            if num >= nums[mid] and num <= nums[mid + 1]:
                return mid
            if num > nums[mid]:
                return insert(num, nums[:mid])
            elif num
                return insert(num, nums[mid:]) + mid

        if len(nums1) > lens(nums2):
            add = nums2
            nums = nums1
        else:
            add = nums1
            nums = nums2
        # iterate through insert as num
        for num in add:
            i = findIndex(num, nums)
            nums.insert(num, i)
        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            mid1 = nums[mid]
            mid2 = nums[mid-1]
            return (mid1 + mid2) / 2
        return nums[mid]

[1, 2,3, 6]
[4, 7]

num = 4

