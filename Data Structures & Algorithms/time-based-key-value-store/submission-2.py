class TimeMap:

    #Key -> Value, Timestamp
    def __init__(self):
        self.keyStore = {}

    #Set Each Key intially to a list of lists, each list includes the value and timestamp
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = [[value, timestamp]]
        else:
            self.keyStore[key].append([value, timestamp])
    #Binary Search, get values at O(logn) time.
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore or len(self.keyStore[key]) == 0:
            return ""
        else:
            l = 0 
            r = len(self.keyStore[key]) -1
            res = ""
            while l <= r:
                mid = (l+r) //2
                ksKey = self.keyStore[key]
                if ksKey[mid][1] <= timestamp:
                    res = ksKey[mid][0]
                #Binary Search
                if ksKey[mid][1] > timestamp:
                    r = mid-1
                elif ksKey[mid][1] < timestamp:
                    l = mid+1
                else:
                    return res
            return res

        
