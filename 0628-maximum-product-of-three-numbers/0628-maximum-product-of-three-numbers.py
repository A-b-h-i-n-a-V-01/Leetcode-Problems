class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        large= nums[-1]* nums[-2] * nums[-3]      
        if nums[0]*nums[1]* nums[-1] > large:
            large=nums[0]*nums[1]* nums[-1]
        return large