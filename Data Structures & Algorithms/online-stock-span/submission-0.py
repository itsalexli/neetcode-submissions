class StockSpanner:
    
    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        if not self.stocks:
            self.stocks.append([price, 1])
            return 1
        else:
            curr_span = 1
            while self.stocks and self.stocks[-1][0] <= price:
                curr_span += self.stocks[-1][1]
                self.stocks.pop()
            self.stocks.append([price, curr_span])
            return curr_span


    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)




