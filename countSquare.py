__author__ = 'yibeihuang'

def countSquare(st, end):
    cnt = 0
    if st>=end: return cnt
    for i in range(st, end+1):
        j = 1
        while j*j <= i:
            if j*j==i:
                cnt+=1
                break
            j+=1
        i+=1
    return cnt
def  getMinimumUniqueSum(arr):
    count = len(arr)
    rst = []
    for ele in arr:
        start, end = ele.split(' ')
        num = countSquare(int(start), int(end))
        rst.append(num)
    return rst

arr = ['9 25']
print(getMinimumUniqueSum(arr))