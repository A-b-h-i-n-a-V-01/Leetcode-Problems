class Solution(object):
    def isPalindrome(self, s):
        str=""
        for ch in s:
            if ch.isalnum():
                str+=ch
        return str.lower() == str[::-1].lower()