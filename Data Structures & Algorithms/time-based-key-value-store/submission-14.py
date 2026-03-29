#Implement a data structure that supports storing multiple values for the same key, with different timestamps
#Aswell as looking up the keys value at a specified timestamp, looking up keys should return the most recent timestamp
#Where in lookup, we must lookup values in the key where timestamp are <= the current tiemstamp
#We're garunteed that all timestamps set are increased each tiem they are set
class TimeMap:

    def __init__(self):
        self.keyStore = {} #key -> [(value, timestamp)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.keyStore:
            self.keyStore[key] = [(value, timestamp)]
        self.keyStore[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.keyStore:
            return ""
        
        valueList = self.keyStore[key]
        l = 0 
        r = len(valueList) -1 
        
        res = ""
        
        while l <= r:
            mid = (l+r) // 2
            
            if valueList[mid] == timestamp:
                return valueList[mid][0]
            
            if valueList[mid][1] <= timestamp:
                res = valueList[mid][0]
                l = mid+1
            
            elif valueList[mid][1] > timestamp:
                r = mid-1
        
        return res


        
        
