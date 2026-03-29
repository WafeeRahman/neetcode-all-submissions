class StockSpanner:

    def __init__(self):
        self.priceStack = []
        

    def next(self, price: int) -> int:
        span = 0
        while self.priceStack and self.priceStack[-1][0] <= price:
            prevPrice, prevSpan = self.priceStack.pop()
            span += prevSpan
        
        self.priceStack.append((price, span+1))
        return span+1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)