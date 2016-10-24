__author__ = 'yibeihuang'
def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        volumn = 0
        # for i in range(1,len(height)+1):
        #     for j in range(i, len(height)+1):
        #         volumn = max(volumn, (j-i)*min(height[j-1],height[i-1]))
        # return volumn
        left, right = 0, len(height)-1
        while left<right:
            h = min(height[left], height[right])
            volumn = max(volumn, (right-left)*h)
            while height[left]<=h and left<right: left += 1
            while height[right]<=h and left<right: right -= 1
        return volumn

height = [4,1,4,2,3,4,1]
print(maxArea(height))