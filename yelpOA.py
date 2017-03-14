__author__ = 'yibeihuang'

def v10(string):
    if len(string)==1: return '1'+string
    res = []
    cnt = 1
    prev = string[0]
    for ele in string[1:]:
        if ele==prev:
            cnt+=1
        else:
            res.append(str(cnt)+prev)
            cnt = 1
            prev = ele
    res.append(str(cnt)+prev)
    return ''.join(res)

print(v10('aaabbca'))