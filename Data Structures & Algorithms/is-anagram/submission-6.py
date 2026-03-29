class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = [0] * 26
        countT = [0] * 26

        for i in range(len(s)):
            char = s[i]
            countS[ord(char) - ord('a')] += 1
        
        for j in range(len(t)):
            char = t[j]
            countT[ord(char) - ord('a')] += 1
        
        for i in range(26):
            if countS[i] != countT[i]:
                return False
        
        return True