__author__ = 'yibeihuang'
import heapq
def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ##  Method 1
        # rst = []
        # hashmap = dict()
        # for i in nums:
        #     if i in hashmap: hashmap[i]+=1
        #     else: hashmap[i]=1
        # while len(rst)<k:
        #     count = 0
        #     for num in hashmap:
        #         if hashmap[num]>count:
        #             count = hashmap[num]
        #             tmp=num
        #     rst.append(tmp)
        #     del hashmap[tmp]
        # return rst

        ## Method 2
        res = []
        hashmap = dict()
        for i in nums:
            if i in hashmap: hashmap[i]+=1
            else: hashmap[i]=1
        hparr = []
        for key in hashmap:
            heapq.heappush(hparr, (-hashmap[key], key))
        n = 1
        while n<=k:
            res.append(heapq.heappop(hparr)[1])
            n += 1
        return res

nums = [5,3,1,1,1,3,73,1]
k = 2
rst = topKFrequent(nums, k)