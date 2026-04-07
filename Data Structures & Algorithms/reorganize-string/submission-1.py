class Solution:
    def reorganizeString(self, s: str) -> str:
        countS = defaultdict(int)
        for char in s:
            countS[char] += 1
        charHeap = []
        for key in countS:
            heapq.heappush(charHeap, [-countS[key], key])
        prev = None
        res = ""
        while charHeap:
            newChar = heapq.heappop(charHeap)
            newChar[0] += 1
            if prev:
                heapq.heappush(charHeap, prev)
                prev = None
            prev = newChar if newChar[0] < 0 else None
            res+=newChar[1]
        return res if len(res) == len(s) else ''


        