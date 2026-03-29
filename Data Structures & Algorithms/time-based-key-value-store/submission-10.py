class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((value, timestamp))
        else:
            self.timeMap[key]= [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap.keys():
            return ""
        l = 0
        r = len(self.timeMap[key])-1
        values = self.timeMap[key]
        res = ""
        while l <= r:
            mid = (l+r)//2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid+1
            elif values[mid][1] > timestamp:
                r = mid-1
        return res
        
