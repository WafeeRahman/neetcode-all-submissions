class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []

        if a > 0:
            heapq.heappush(maxHeap,[-a, "a"])
        if b > 0:
            heapq.heappush(maxHeap,[-b, "b"])
        if c > 0:
            heapq.heappush(maxHeap,[-c, "c"])

        res = ""
        i=0
        blocked = None
        while maxHeap:
            newChar = heapq.heappop(maxHeap)
            
            if blocked:
                heapq.heappush(maxHeap, blocked)
                blocked = None
         
            if (len(res) >= 2 and not res[i-1] == res[i-2] == newChar[1]):
                newChar[0] += 1
                res += newChar[1]
                i+=1
            elif len(res) < 2:
                newChar[0] += 1
                res += newChar[1]
                i+=1
            else:
                blocked = newChar


            if newChar[0] < 0 and not blocked:
                heapq.heappush(maxHeap, newChar)
        
        return res