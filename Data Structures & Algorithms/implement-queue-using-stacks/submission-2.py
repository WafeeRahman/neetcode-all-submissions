class MyQueue:

    def __init__(self):
        self.pushstack = []
        self.popstack = []
        

    def push(self, x: int) -> None:
        self.pushstack.append(x)
        

    def pop(self) -> int:
        print("POP")
        print(self.pushstack)
        while self.pushstack:
            self.popstack.append(self.pushstack.pop())
        print(self.popstack)
        x = self.popstack.pop()
        while self.popstack:
            self.pushstack.append(self.popstack.pop())
        print(self.pushstack)
        return x



    def peek(self) -> int:
        print("PEEK")
        print(self.pushstack)
        while self.pushstack:
            self.popstack.append(self.pushstack.pop())
        print(self.popstack)
        x = self.popstack[-1]
        while self.popstack:
            self.pushstack.append(self.popstack.pop())
        print(self.pushstack)
        return x
        

    def empty(self) -> bool:
        return not self.pushstack and not self.popstack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()