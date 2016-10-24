__author__ = 'yibeihuang'
def longestSubstring(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s == '' or len(s)<k: return 0
        rst, count = 0, {}
        maxVal = 0
        i = 1
        while i <len(s): #for i in... while// while i ... for i ...
            while i<len(s) and s[i]==s[i-1]:
                if s[i] in count:
                    count[s[i]] += 1
                else: count[s[i]] = 2
                i += 1
            if s[i-1] in count and count[s[i-1]]<k:
                for ele in count: count[ele]=0
            else:
                for ele in count: rst = rst+count[ele]
            maxVal= max(maxVal, rst)
            i+=1
        return maxVal

s='aaabb'
k=3
print(longestSubstring(s,k))