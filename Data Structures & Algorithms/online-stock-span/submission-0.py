class StockSpanner:

    def __init__(self):
        self.priceStack = []
        

    def next(self, price: int) -> int:
        span = 0
        i = len(self.priceStack)-1
        while i>=0 and self.priceStack[i] <= price:
            span+=1
            i-=1
        
        self.priceStack.append(price)
        return span+1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)