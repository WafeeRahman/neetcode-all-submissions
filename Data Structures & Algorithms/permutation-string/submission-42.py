class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        countS1 = [0] * 26
        countS2 = [0] * 26

        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if countS1[i] == countS2[i]:
                matches += 1

        l = 0
        s = s2      
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
  
            
            countS2[ord(s[r]) - ord('a')] += 1
            if countS2[ord(s[r]) - ord('a')] == countS1[ord(s[r]) - ord('a')]:
                matches += 1
            elif countS2[ord(s[r]) - ord('a')] == countS1[ord(s[r]) - ord('a')]+1:
                matches -= 1

            
            countS2[ord(s[l]) - ord('a')] -= 1
            if countS2[ord(s[l]) - ord('a')] == countS1[ord(s[l]) - ord('a')]:
                matches += 1
            elif countS2[ord(s[l]) - ord('a')] == countS1[ord(s[l]) - ord('a')]-1:
                matches -= 1
            l+=1
        return matches == 26
            



        