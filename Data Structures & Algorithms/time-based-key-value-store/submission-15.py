class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append((value, timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        l=0
        r=len(self.keyStore[key])-1
        res = ""
        while l<=r:
            mid = (r+l)//2
            
            if self.keyStore[key][mid][1] > timestamp:
                r=mid-1
            elif self.keyStore[key][mid][1] <= timestamp:
                if self.keyStore[key][mid][1] == timestamp:
                    return self.keyStore[key][mid][0]
                res=self.keyStore[key][mid][0]
                l=mid+1
        return res
        
        
