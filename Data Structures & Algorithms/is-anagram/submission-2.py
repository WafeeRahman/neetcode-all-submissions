#With two strings s and t, return true if theyre annagrams of eachother
#Anagram: Each letter contains the exact same characters as the other, meaning same characters, and counts
#We can track counts with a hashmap, and compare the equalities of each hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for char in s:
            countS[char] = countS.get(char, 0) + 1
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        return countS == countT
        
        