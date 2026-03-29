class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countT = defaultdict(int)
        for char in t:
            countT[char] += 1
        
        have = 0
        need = len(countT)

        countS = defaultdict(int)

        l = 0 
        minWindow = float('inf')
        res = (0,len(s))
        for r in range(len(s)):
            countS[s[r]] += 1


            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            

            while have == need:
                if minWindow >= (r-l+1):
                    res = (l,r)
                    minWindow = (r-l+1)
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        return "" if minWindow == float('inf') else s[res[0]:res[1]+1]


        