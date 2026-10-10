class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        maxf = 0
        res = 0
        l=0
        for r in range(len(s)):

            counts[s[r]] += 1
            #Take the max occuring frequency in the array..
            #Idea here is that we can replace our entire window with the max occuring frequent character
            #So if we can replace atleast k characters in our window (window - maxf is +ve), thats a valid character replacement
            if counts[s[r]] > maxf:
                maxf = counts[s[r]]
            
            windowLen = r-l+1

            while windowLen-maxf > k:
                counts[s[l]]-=1
                l+=1
                windowLen = r-l+1
            
            if windowLen - maxf <= k:
                res = max(res, windowLen)
            
        return res

            



