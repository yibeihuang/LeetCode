__author__ = 'yibeihuang'
import re

def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<=1: return True
        i = 0
        j = len(s)-1
        while i<=j:
            while i<len(s)-1 and re.match('[^a-zA-Z0-9]',s[i]):
                i += 1
            while j>i and re.match('[^a-zA-Z0-9]',s[j]):
                j -= 1
            if j>=i and s[i].lower()!=s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True

s = 'a a'
print(isPalindrome(s))