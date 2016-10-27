__author__ = 'yibeihuang'
import collections

def lengthOfLongestSubstringKDistinct(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s)==0: return 0
        if len(s)<=k: return len(s)
        worddict, window, diff, rst= dict(),collections.deque(),0, 0
        for i in s:
            if i in worddict:
                window.append(i)
                worddict[i] += 1
            else:
                if diff < k:
                    worddict[i] = 1
                    diff += 1
                    window.append(i)
                else:
                    while len(window)>0 and diff>=k:
                        first = window.popleft()
                        if first in worddict:
                            worddict[first] -= 1
                            if worddict[first]==0:
                                del worddict[first]
                                diff -= 1
                    if diff<k:
                        worddict[i] = 1
                        diff += 1
                        window.append(i)
            rst = max(rst,len(window))
        return rst

s = "eaebsc"
k = 2
print(lengthOfLongestSubstringKDistinct(s,k))