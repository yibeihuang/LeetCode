__author__ = 'yibeihuang'
def removeKdigits(num, k):
    size = len(num)
    stack = ['0']
    for x in range(size):
        while stack[-1] > num[x] and len(stack) + k > x + 1:
            stack.pop()
        stack.append(num[x])
    while len(stack) > size - k + 1:
        stack.pop()
    return str(int(''.join(stack)))

num = "1300214"
k = 2

print(removeKdigits(num,k))