__author__ = 'yibeihuang'
def summaryRanges(nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==1: return ["{}".format(nums[0])]
        p1,p2 = 0,1
        rst = []
        while p1<p2 and p2<len(nums):
            while p2<len(nums) and nums[p2]==nums[p2-1]+1:
                p2 += 1
            if p2>p1+1:
                string = '{}->{}'.format(nums[p1],nums[p2-1])
            else:
                string = '{}'.format(nums[p1])
            rst.append(string)
            if p2<=len(nums)-2:
                p1=p2
                p2=p1+1
            elif p2==len(nums)-1:
                rst.append('{}'.format(nums[-1]))
                return rst

        return rst

nums = [1,3,5,7]
print(summaryRanges(nums))