__author__ = 'yibeihuang'
def shortestPalindrome( s):
        """
        :type s: str
        :rtype: str
        """
        count,p1 = 0,-1
        lsts = list(s)
        for i in range(len(lsts)):
            p,tmp = 0,0
            while i-p-1>-1 and i+p+1<len(lsts):
                # odd elements:
                if s[i-p-1]==s[i+p+1]:
                    p, tmp = p+1, tmp+2
                else: break
            if i-p-1==-1:count = max(count, tmp+1)
            if tmp+1==count: p1=0
            p,tmp=0,0
            while i-p>-1 and i+p+1<len(lsts):
                # even elements:
                if s[i-p]==s[i+p+1]:
                    p, tmp = p+1, tmp+2
                else: break
            if i-p==-1:count = max(count,tmp)
            if tmp==count: p1=0
        if p1==0:
            print count
            add = lsts[p1+count:len(lsts)][::-1]
            return ''.join(add+lsts[p1:])
        else:
            return ''.join(lsts[::-1][1:]+lsts)

def manacher(s):
        # premanipulate
        s='#'+'#'.join(s)+'#'
        RL=[0]*len(s)
        MaxRight=0
        pos,endpoint=0,0
        MaxLen=0
        for i in range(len(s)):
            if i<MaxRight:RL[i]=min(RL[2*pos-i], MaxRight-i)
            else:RL[i]=1
            # try broadening
            while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
                RL[i]+=1
            # update MaxRight,pos
            if RL[i]+i-1>MaxRight:
                MaxRight=RL[i]+i-1
                pos=i
                if i-RL[i]==-1:endpoint=RL[i]+i-1
            #update endpoint of the panlindrome
            MaxLen=max(MaxLen, RL[i])
        endpoint=endpoint/2 #actual idx in original string
        return ''.join(s.split('#'))[endpoint:][::-1]+''.join(s.split('#'))
        # return MaxLen-1

s = "ababbbabbaba"
# print(s)
# print(manacher(s))
# print(shortestPalindrome(s))
def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[-k:]+nums[:-k]

a=[1,2]
k=1
rotate(a,k)
print(a)