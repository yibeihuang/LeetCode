__author__ = 'yibeihuang'
import collections

def lengthOfLongestSubstringKDistinct(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        worddict, window, rst= dict(),collections.deque(), 0
        for i in s:
            if i in worddict:
                window.append(i)
                worddict[i] += 1
            else:
                if len(worddict) < k:
                    worddict[i] = 1
                    window.append(i)
                else:
                    while len(window)>0 and len(worddict)>=k:
                        first = window.popleft()
                        if first in worddict:
                            worddict[first] -= 1
                            if worddict[first]==0:
                                del worddict[first]
                    if len(worddict)<k:
                        worddict[i] = 1
                        window.append(i)
            rst = max(rst,len(window))
        return rst

s = ""
k = 4
print(lengthOfLongestSubstringKDistinct(s,k))