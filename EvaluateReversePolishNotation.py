__author__ = 'yibeihuang'
import re
import operator

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    if len(tokens)==1: return int(tokens[0])
    stack = []
    i = 0
    while i<len(tokens):
        if re.match('^-?[0-9]+$', tokens[i]):
            stack.append(int(tokens[i]))
            i += 1
        elif tokens[i]== '+' and len(stack)>=2:
            op1 = stack.pop()
            op2 = stack.pop()
            rst = int(op1)+int(op2)
            stack.append(rst)
            i+=1
        elif tokens[i]== '-' and len(stack)>=2:
            op1 = stack.pop()
            op2 = stack.pop()
            rst = int(op2)-int(op1)
            stack.append(rst)
            i+=1
        elif tokens[i]== '*' and len(stack)>=2:
            op1 = stack.pop()
            op2 = stack.pop()
            rst = int(op2)*int(op1)
            stack.append(rst)
            i+=1
        elif tokens[i]== '/' and len(stack)>=2:
            op1 = stack.pop()
            op2 = stack.pop()
            rst = int(op2)/int(op1)
            # rst = int(operator.truediv(int(op2), int(op1)))
            stack.append(rst)
            i+=1

    return stack[0]

# class Solution:
#     # @param {string[]} tokens
#     # @return {integer}
#     def __init__(self):
#         self.operators = {
#             '+': lambda y, x: x + y,
#             '-': lambda y, x: x - y,
#             '*': lambda y, x: x * y,
#             '/': lambda y, x: int(operator.truediv(x, y))
#         }
#
#     def evalRPN(self, tokens):
#         if not tokens:
#             return 0
#
#         stack = []
#
#         for token in tokens:
#             if token in self.operators:
#                 stack.append(self.operators[token](stack.pop(), stack.pop()))
#             else:
#                 stack.append(int(token))
#
#         return stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))