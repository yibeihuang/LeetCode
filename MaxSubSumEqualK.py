__author__ = 'yibeihuang'
def maxSubArrayLen(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = dict()
        rst,tmp = 0,0
        for i in range(len(nums)):
            tmp = tmp+nums[i]
            if tmp not in sums:sums[tmp]=i

            if tmp==k:rst=i+1
            elif tmp-k in sums:rst=max(rst, i-sums[tmp-k])
        # rst = 0
        # if k in sums:rst = max(sums[k])+1
        # for k1 in sums:
        #     if k1+k in sums:
        #         for j in sums[k1+k]:
        #             for t in sums[k1]:
        #                 rst = max(rst, (j-t))
        return rst

nums = [-5,8,2,-1,6,-3,7,1,8,-2,7]
k=-4
print(maxSubArrayLen(nums,k))