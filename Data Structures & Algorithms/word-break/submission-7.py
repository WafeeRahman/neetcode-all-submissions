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
            res = False
            for word in wordDict:
                if word in s[i:i+len(word)]:
                    res = res or dfs(i+len(word))
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
        
       

        def dp():
            dp = [False] * (len(s)+1)
            dp[len(s)] = True
            wordSet = set(wordDict)
            for i in range(len(s)-1,-1,-1):
                for word in wordDict:
                    if dp[i]:
                        break

                    if not dp[i] and i+len(word) <= len(s) and s[i:i+len(word)] in wordSet:
                        print(s[i:i+len(word)])
                        dp[i] = dp[i+len(word)]
                    
                    
            print(dp)
            return dp[0]
        return dp()
                    



        



