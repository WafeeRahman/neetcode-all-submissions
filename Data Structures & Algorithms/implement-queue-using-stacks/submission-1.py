class MyQueue:

    def __init__(self):
        self.pushQ = deque([])
        self.popQ = deque([])
    
        

    def push(self, x: int) -> None:
        self.pushQ.append(x)
        

    def pop(self) -> int:
        print(self.pushQ, self.popQ)
        while self.pushQ:
            self.popQ.append(self.pushQ.popleft())
        print(self.pushQ, self.popQ)
        x=self.popQ.popleft()
        while self.popQ:
            self.pushQ.append(self.popQ.popleft())
    
      


        return x

    def peek(self) -> int:
        print(self.pushQ, self.popQ)
        while self.pushQ:
            self.popQ.append(self.pushQ.popleft())
        x=self.popQ[0]
        print(self.pushQ, self.popQ)
        while self.popQ:
            self.pushQ.append(self.popQ.popleft())
        print(self.pushQ, self.popQ)
        return x
        

    def empty(self) -> bool:
        return not self.pushQ
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()