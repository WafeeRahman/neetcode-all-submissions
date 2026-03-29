#Given an array of strings, store all strings that are anagrams as sublists. 
#Defn of anagram: Two or more words with the same amt of characters

# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]], act and cat are anagrams, aswell as the rest
#Single anagrams have no neighbours

#Approach, anagrams have the same sorted order of characters, we can use this to store each word in a sublist based on their sorted order


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords = defaultdict(list)
        res = []
        #Sort words and store them in a hashmap of lists
        for string in strs:
            sort = sorted(string)
            sort = ''.join(sort)
            sortedWords[sort].append(string)
        
        #Unload sublists into result vector
        for key in sortedWords:
            res.append(sortedWords[key])
        return res