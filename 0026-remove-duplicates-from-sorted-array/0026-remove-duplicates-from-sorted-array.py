class Solution(object):
    def removeDuplicates(self, nums):
        ctr=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[ctr]=nums[i]
                ctr+=1
        return ctr