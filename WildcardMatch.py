__author__ = 'yibeihuang'
import time

def isMatch(s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        # origin = list(s)
        # pattn = list(p)
        if len(p)!=len(s) and '*' not in p: return False
        for i in range(len(s)):
            if i<len(p) and p[i]==s[i]: continue
            elif i<len(p) and p[i]=='?': continue
            elif i<len(p) and p[i]=='*':
                j = i
                while j < len(s):

                    if isMatch(s[j:],p[i+1:]):break
                    else:j+=1
                if j==len(s) and i+1<len(p): return False
                else: return True
            else: return False
        if i+1 <len(p) and ''.join(''.join(p[i+1:]).split('*')): return False
        return True

def isMatchII(s,p):
    s_cur, p_cur = 0,0
    match, star = 0, -1
    while s_cur<len(s):
        if p_cur<len(p) and (s[s_cur]==p[p_cur] or p[p_cur]=='?'):s_cur, p_cur = s_cur+1, p_cur+1
        elif p_cur<len(p) and p[p_cur]=='*':
            match,star = s_cur,p_cur
            p_cur+=1
        elif star!=-1:
            p_cur = star+1
            match = match+1
            s_cur = match
        else: return False
    while p_cur<len(p) and p[p_cur]=='*':
        p_cur+=1
    if p_cur==len(p):return True
    else:return False

s="babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab"
p="***bba**a*bbba**aab**b"
start = time.time()
print(isMatch(s,p))
end = time.time()
print(end-start)

start2 = time.time()
print(isMatchII(s,p))
end2 = time.time()
print(end2-start2)