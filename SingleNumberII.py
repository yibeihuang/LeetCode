__author__ = 'yibeihuang'
# def singleNumber(nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         a = 0
#         b = 0
#         for i in nums:
#             tmp = (~a&b&i)|(a&~b&~i)
#             b = (~a&~b&i)|(~a&b&~i)
#             a = tmp
#         return a|b
#
# nums=[11,12,12,12,13,13,13]
# print(singleNumber(nums))

i = 3
a = -i
si = "{0:b}".format(i)
sa = "{0:b}".format(a)
ss = "{0:b}".format(i&a)
print(ss)