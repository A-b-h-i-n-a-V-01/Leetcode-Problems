class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index={}
        for i in range(0,len(nums)):
            if nums[i] not in index:
                index[nums[i]]=i
            else:
                if abs(i-index[nums[i]])<=k:
                    return True
                else:
                    index[nums[i]]=i
        return False