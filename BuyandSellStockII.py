__author__ = 'yibeihuang'
def maxProfit(prices):
        length = len(prices)
        profit = 0
        for i in xrange(1, length):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

prices = [1,3,7,6,9]
print(maxProfit(prices))