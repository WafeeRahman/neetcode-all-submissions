class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        windowCount = defaultdict(int)

        s1Count = defaultdict(int)
        for i in range(len(s1)):
            s1Count[s1[i]] += 1
            print(s1, s2, i)
            windowCount[s2[i]] += 1
        
        if s1Count == windowCount:
            return True
        l=0
        for r in range(len(s1), len(s2)):
            print(windowCount)
            if windowCount == s1Count:
                return True

            windowCount[s2[r]] += 1
            
    

            windowCount[s2[l]] -= 1
            if windowCount[s2[l]] <= 0:
                del(windowCount[s2[l]])
            l+=1
        
        for char in s1:
            if not windowCount[char]:
                return False
            if windowCount[char] < s1Count[char]:
                return False

        return True


        