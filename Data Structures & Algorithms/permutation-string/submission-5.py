class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Preamble and Base Cases:
        if len(s1) > len(s2): return False

        #Count the amount of appearances of characters  from s1 in s1 and s2
        s1Count, s2Count = [0] * 26, [0] * 26
        
        #If we have 26 matches (each alpha character in s1 and s2 have matching counts), then we have an anagram within the string
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] +=1
            s2Count[ord(s2[i]) - ord('a')] +=1

        #Increment matches according to how many characters from s1 have matching counts in s2
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        
        #Sliding Window, increment and decrement matches based on the matches within windows of len(s1)
      
        l=0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26