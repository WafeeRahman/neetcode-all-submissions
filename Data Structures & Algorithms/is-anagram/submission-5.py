class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Def'n Anagram --> Strings that have the same occurence count of characters

        countS = [0] * 26
        countT = [0] * 26

        for char in s:
            countS[ord(char) - ord('a')] += 1
        
        for char in t:
            countT[ord(char) - ord('a')] += 1

        return countS == countT
        