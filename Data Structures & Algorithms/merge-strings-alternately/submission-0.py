class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        newS=""

        i = 0
        j = 0

        while i < len(word1) and j < len(word2):
            newS += word1[i]
            newS += word2[j]
            i += 1
            j += 1

        if i < len(word1):
            newS += word1[i:]
        
        if j < len(word2):
            newS += word2[j:]

        return newS

        