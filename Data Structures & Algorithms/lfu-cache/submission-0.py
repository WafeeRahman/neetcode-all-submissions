
class LFUCache:

    def __init__(self, capacity: int):
        self.keyVal = {}
        self.freq = {}
        self.freqList = defaultdict(OrderedDict)
        self.cap = capacity
        self.minFreq = 0
        

    def get(self, key: int) -> int:
        if key in self.keyVal:
            node = self.keyVal[key]
            freq = self.freq[key]
            self.freq[key] += 1
            del self.freqList[freq][key]
            if self.minFreq == freq and not self.freqList[self.minFreq]:
                self.minFreq += 1
            self.freqList[self.freq[key]][key] = node
            self.freqList[self.freq[key]].move_to_end(key, last=True)
            return node
        else:
            return -1


        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.keyVal:
            self.keyVal[key] = value
            freq = self.freq[key]
            self.freq[key] += 1
            del self.freqList[freq][key]
            if self.minFreq == freq and not self.freqList[self.minFreq]:
                self.minFreq += 1
            self.freqList[self.freq[key]][key] = value
            self.freqList[self.freq[key]].move_to_end(key, last=True)
        else:
            if len(self.keyVal) == self.cap:
                k, v = self.freqList[self.minFreq].popitem(last=False)
                del(self.keyVal[k])
                del(self.freq[k])
              
        
            self.keyVal[key] = value
            self.freq[key] = 1
            self.minFreq = 1
            self.freqList[self.freq[key]][key] = value
            self.freqList[self.freq[key]].move_to_end(key, last=True)
         

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)