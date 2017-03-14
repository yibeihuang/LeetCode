__author__ = 'yibeihuang'
def findMaximumXOR( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # N = 5
        # mask = 0
        # maxv = 0
        # for i in reversed(range(N)):
        #     mask = mask | (1<<i)
        #     tmpset = set()
        #     for num in nums:
        #         tmpset.add(num & mask)
        #     tmp = maxv|1<<i
        #     for val in tmpset:
        #         if val^tmp in tmpset:
        #             maxv = tmp
        # return maxv
        answer = 0
        for i in range(5)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer

nums = [3,10,5,25,2,8]
print(findMaximumXOR(nums))