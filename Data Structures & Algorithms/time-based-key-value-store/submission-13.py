class TimeMap:

    def __init__(self):
        self.keyVal = {} #key, val -> list w/ values and their timestamps
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyVal.keys():
            self.keyVal[key].append((value, timestamp))
        else:
            self.keyVal[key] = [(value, timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        #Get in O(logn)
        if not (key in self.keyVal.keys()):
            return ""

        l = 0
        r = len(self.keyVal[key])-1
        res = ""
        while l <= r:
            mid = (l+r)//2
            item = self.keyVal[key][mid]

            if item[1] <= timestamp:
                res = item[0]
                l=mid+1
            elif item[1] > timestamp:
                r=mid-1
        return res
        
