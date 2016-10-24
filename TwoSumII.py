__author__ = 'yibeihuang'
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers)==1: return [0]
        p1, p2 = 0, len(numbers)-1
        while numbers[p1]+numbers[p2]!=target:
            if numbers[p1]+numbers[p2]<target:
                p1 += 1

            elif numbers[p1]+numbers[p2]>target:
                p2 -= 1
        return [p1+1,p2+1]