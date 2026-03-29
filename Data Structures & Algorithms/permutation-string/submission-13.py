class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Motivation: to find a window of len(s1) within s2 such that every character in s1 has the same count as s2
        #(Def'n Anagram)
        if len(s1) > len(s2): return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26
        matches = 0 #If we ever have as many matches as we have characters in the alphabet, that tells us we have a valid window
        for c in range(len(s1)):
            s1Count[ord(s1[c]) - ord('a')] += 1
            s2Count[ord(s2[c]) - ord('a')] += 1
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        l=0
        #Start at len(s1), since we already filled it above
        for r in range(len(s1), len(s2)):
            if (matches == 26):
                return True
            
            #Increment counts appropriately
            right = ord(s2[r]) - ord('a') 
            s2Count[right] += 1 
            
            if s2Count[right] == s1Count[right]:
                matches += 1
            elif s2Count[right] == s1Count[right]+1:
                matches -= 1
            
            left = ord(s2[l]) - ord('a') 
            s2Count[left] -= 1
            if s2Count[left] == s1Count[left]:
                matches += 1
            elif s2Count[left] == s1Count[left] -1:
                matches -= 1
            l+=1
           
        return True if matches == 26 else False



        