__author__ = 'yibeihuang'

class Solution():
    def findTrader(self, inputStr):
        self.priceMap, self.transHistory = dict(), dict()
        self._initData(inputStr)
        record = set()
        res = []
        for key in self.transHistory:
            for i in range(key, key+3):
                if i in self.priceMap:
                    price = self.priceMap[i]
                    for ele in self.transHistory[key]:
                        if ele.amount*(price-ele.lastprice)*(1 if ele.type=='BUY' else -1)>=500000:
                            if (ele.date, ele.name) not in record:
                                res.append([str(ele.date), ele.name])
        return res

    def _initData(self, inputStr):
        for ele in inputStr:
            lst = ele.split('|')
            if len(lst) == 2:
                self.priceMap[int(lst[0])]=float(lst[1])
                lastprice = float(lst[1])
            if len(lst) == 4:
                tmp = transaction(lst[0], lst[1], lst[2], lst[3], lastprice)
                if tmp.date in self.transHistory:
                    self.transHistory[tmp.date].append(tmp)
                else:
                    self.transHistory[tmp.date] = [tmp]


class transaction():
    def __init__(self, date, trader_name, trans_type, amount, lastprice):
        self.date = int(date)
        self.name = trader_name
        self.type = trans_type
        self.amount = float(amount)
        self.lastprice = float(lastprice)

sol = Solution()
inputS = ['16','0|20','0|K|SELL|300','0|W|BUY|500','0|T|BUY|5000','1|T|BUY|150000','3|25','8|K|SELL|60000','10|15','11|5']
print(sol.findTrader(inputS))