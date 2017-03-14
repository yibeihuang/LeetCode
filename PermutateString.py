__author__ = 'yibeihuang'


def PermutateStr(string):
    strlist = sorted(string)
    recurPerm( [], strlist)

def recurPerm(tmp, strlist):
    if strlist==[]:
        print(''.join(tmp))
    for i in range(len(strlist)):
        newlst = strlist[:i]+strlist[i+1:]
        recurPerm(tmp+[strlist[i]], newlst)

PermutateStr('ABC')
