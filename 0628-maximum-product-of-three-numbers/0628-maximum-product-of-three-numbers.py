class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        large= nums[len(nums)-1]* nums[len(nums)-2] * nums[len(nums)-3 ]      
        if nums[0]*nums[1]* nums[len(nums)-1] > large:
            large=nums[0]*nums[1]* nums[len(nums)-1]
        return large