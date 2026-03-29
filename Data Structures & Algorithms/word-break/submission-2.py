#We're given a dictionary of words and a string s of potentially concatantaed words
#Accroding to the dictionary

#We need to traverse the string s and check if each word is able to be broken into words from the dictionary
#We can build a substring for each letter in word and try matching it to a word in wordDict
#We can either try matching each substring of s to a word in the dictionary, but it would be more efficient
#To try matching each word in worddict to a substring in s, as len(worddict) < len(s)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i >= len(s):
                if i == len(s):
                    return True
                return False

            #We have the decision to start each word at the ith position
            res = True
            for word in wordDict:
                if word in s[i:i+len(word)]:
                    res = res and dfs(i+len(word))
            return res
      

        cache = {}
        def memo(i):
            if i in cache:
                return cache[i]
            
            if i >= len(s):
                if i == len(s):
                    return True
                return False
            cache[i] = False
            
            for word in wordDict:
                if word in s[i:i+len(word)]:
                    cache[i] = cache[i] or memo(i+len(word))
            return cache[i]
        
        return memo(0)
        



