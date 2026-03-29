class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        countS1 = [0] * 26
        countS2 = [0] * 26
        matches = 0

        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1

        for i in range(26): 
            if countS1[i] == countS2[i]:
                matches += 1
        
        l = 0 
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            countS2[ord(s2[i]) - ord('a')] += 1
            char = s2[i]
            print(char)  
          
            if countS2[ord(s2[i]) - ord('a')] == countS1[ord(s2[i]) - ord('a')]:
                matches += 1
            elif countS2[ord(s2[i]) - ord('a')] ==  countS1[ord(s2[i]) - ord('a')] + 1:
                matches -= 1
            
            
            countS2[ord(s2[l]) - ord('a')] -= 1
            char = s2[l]
            if countS2[ord(s2[l]) - ord('a')] ==  countS1[ord(s2[l]) - ord('a')]:
                matches += 1
            elif countS2[ord(s2[l]) - ord('a')] ==  countS1[ord(s2[l]) - ord('a')] -1:
                matches -= 1
            l+=1
        return matches == 26
            