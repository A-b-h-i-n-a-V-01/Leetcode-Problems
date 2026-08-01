class Solution(object):
    def reverseString(self, s):
        i=0
        j=len(s)-1
        temp=0
        for i in range(0,len(s)):
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            j-=1
            if i>=j:
                break
        return s