__author__ = 'yibeihuang'
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window = []
        for ele in nums:
            if len(window) < 3 and ele not in window:
                window.append(ele)
                window = sorted(window, reverse=True)
            elif len(window) == 3:
                if ele>window[0]:
                    window.pop()
                    window = [ele] + window
                elif ele>window[1]:
                    window.pop()
                    tmp = window[1]
                    window[1] = ele
                    window.append(tmp)
                elif ele>window[2]:
                    window[2] = ele
        if len(window)<3:
            return window[0]
        return window[2]

tst = [2,2,3,1]
sol = Solution()
print(sol.thirdMax(tst))