class FreqStack:

    def __init__(self):
        self.freqStack = []
        self.freqDict = defaultdict(int)

    def push(self, val: int) -> None:
        self.freqStack.append(val)
        self.freqDict[val]+=1

    def pop(self) -> int:
        maxVal = self.freqStack[0]
        for key in self.freqStack:
            if self.freqDict[key] >= self.freqDict[maxVal]:
                print(self.freqDict[key], self.freqDict[maxVal], key, maxVal)
                maxVal = key
        self.freqDict[maxVal]-=1
        print(self.freqStack, self.freqDict, maxVal)
        for i in range(len(self.freqStack)-1,-1,-1):
            if self.freqStack[i] == maxVal:
                x=self.freqStack.pop(i)
                
                return x

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()