__author__ = 'yibeihuang'
def characterReplacement(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        keys, maxLen = set(), 0
        for i in s:
            if i not in keys:keys.add(i)
        while keys:
            key = keys.pop()
            count, length, pos = k, 0, []
            lsts,i = list(s),0
            while i<len(lsts):
                if lsts[i] != key and count!=0:
                    pos.append(i)
                    count, i, length = count-1, i+1, length+1
                elif lsts[i]!=key and count==0 and pos!=[]:
                    maxLen = max(maxLen, length)
                    count, length = 1, i-pos.pop(0)-1
                elif lsts[i]==key: i, length=i+1,length+1
                elif lsts[i]!=key and count==0 and pos==[]:
                    maxLen = max(maxLen, length)
                    i, length = i+1, 0
                    continue
            maxLen = max(maxLen,length)
        return maxLen

s='AABA'
k=0
print(characterReplacement(s,k))