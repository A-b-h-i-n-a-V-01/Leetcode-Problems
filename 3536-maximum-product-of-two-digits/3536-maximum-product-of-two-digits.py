class Solution(object):
    def maxProduct(self, n):
        arr = list(str(n))
        large=-1
        for i in range(0,len(arr)-1):
            for k in range(i+1,len(arr)):
                if i==k:
                    continue
                no=int(arr[i])*int(arr[k])
                if no > large:
                    large=no
        return large