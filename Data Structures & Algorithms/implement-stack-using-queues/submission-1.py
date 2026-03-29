class MyStack:

    def __init__(self):
        self.pushQ = deque([])
        self.popQ = deque([])

    def push(self, x: int) -> None:
        self.pushQ.append(x)
        

    def pop(self) -> int:
        print(self.pushQ)
        while self.pushQ:
            if len(self.pushQ) == 1:
                x = self.pushQ[0]
            self.popQ.append(self.pushQ.popleft())
        x = self.popQ.pop()
        print(self.popQ)
        while self.popQ:
            self.pushQ.append(self.popQ.popleft())
        
        return x
        

    def top(self) -> int:
        print(self.pushQ)
        while self.pushQ:
            if len(self.pushQ) == 1:
                x = self.pushQ[0]
            self.popQ.append(self.pushQ.popleft())
        while self.popQ:
            self.pushQ.append(self.popQ.popleft())
        return x
        

    def empty(self) -> bool:
        return not (self.pushQ) and not(self.popQ)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()