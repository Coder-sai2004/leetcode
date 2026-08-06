class StockSpanner:

    def __init__(self):
        self.res=[]
        self.st1=[]
        self.st2=[]
        

    def next(self, price: int) -> int:
        val=1
        while self.st1 and price>=self.st1[-1]:
            self.st1.pop()
            idx=self.st2.pop()
            val+=idx

        self.res.append(val)
        self.st1.append(price)
        self.st2.append(val)

        return self.res[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)