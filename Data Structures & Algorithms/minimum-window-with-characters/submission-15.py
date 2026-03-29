class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        countS = {}
        countT = {}
      
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        have = 0 
        need = len(countT.keys())
        minWindow = ""
        l=0
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r], 0) + 1

            if s[r] in t:
                if countS[s[r]] == countT[s[r]]:
                    have += 1

            #Sliding Window Condition, once we have all of the count matches we need, shrink the window
            while have == need:
                minWindow = s[l:r+1]
                countS[s[l]] = countS.get(s[l], 0) - 1
                if s[l] in t:
                    if countS[s[l]] < countT[s[l]]:
                        have -= 1
                l+=1
        return minWindow
