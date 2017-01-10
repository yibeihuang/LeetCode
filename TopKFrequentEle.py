__author__ = 'yibeihuang'
def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rst = []
        hashmap = dict()
        for i in nums:
            if i in hashmap: hashmap[i]+=1
            else: hashmap[i]=1
        while len(rst)<k:
            count = 0
            for num in hashmap:
                if hashmap[num]>count:
                    count = hashmap[num]
                    tmp=num
            rst.append(tmp)
            del hashmap[tmp]
        return rst

nums = [1,1,1,2,2,3]
k=2
rst = topKFrequent(nums, k)