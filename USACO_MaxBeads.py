__author__ = 'yibeihuang'
def MaxBeads(necklace):
    #input str
    #output int
    necklace = list(necklace)
    count, maxnum = 0, 0
    index_w, index_r, index_b = -1,-1,-1
    flag, prev = 0, ''
    for i in range(len(necklace)):
        if necklace[i]=='w':
            j,k = i-1,i+1
            while necklace[(j)%len(necklace)]==necklace[i]:j-=1
            while necklace[(k)%len(necklace)]==necklace[i]:k+=1
            if necklace[j]==necklace[k]:necklace[i]=necklace[j]

    for i in range(len(necklace)):
        if necklace[i]=='w':
            if (i>0 and necklace[i-1]!='w') or i==0:index_w = i
            count += 1
        elif necklace[i]=='r':
            if 'r' == prev:count+=1
            else:
                prev, index_r, flag = 'r', i, flag+1
                if flag==3:
                    maxnum = max(maxnum, count)
                    if index_w!=-1:count = max((index_r-index_b),(index_r-index_w))+1
                    else:count = index_r-index_b+1
                    flag -= 1
                else:count+=1
        elif necklace[i]=='b':
            if 'b'==prev:count+=1
            else:
                prev, index_b, flag = 'b', i, flag+1
                if flag==3:
                    maxnum=max(maxnum,count)
                    if index_w!=-1:count = max((index_b-index_r),(index_b-index_w))+1
                    else:count = index_b-index_r+1
                    flag -= 1
                else:count+=1
    i, countw = 0,0
    while necklace[i]=='w':
        countw, i = countw+1, i+1
    maxnum=max(maxnum,count+countw)
    if necklace[i]=='r':
        countr = 0
        while necklace[i]=='r': countr+=1
        count = max(count, len(necklace)-min(index_w,index_b)+countr+countw)
    else:
        countb = 0
        while necklace[i]=='b': countb, i= countb+1,i+1
        count = max(count,len(necklace)-min(index_w,index_r)+countb+countw)
    return max(maxnum,count)

necklace='wwwbbrwrbrbrrbrbrwrwwrbwrwrrb'
print MaxBeads(necklace)