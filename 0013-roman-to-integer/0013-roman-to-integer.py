class Solution(object):
    def romanToInt(self, s):
        values={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        for i in range(len(s)):
            current=values[s[i]]
            if i<(len(s)-1):
                next=values[s[i+1]]
                if current>=next:
                    res+=current
                else:
                    res-=current
            else:
                res+=current
        return res