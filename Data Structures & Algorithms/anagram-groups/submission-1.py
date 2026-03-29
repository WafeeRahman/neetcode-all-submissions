class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = defaultdict(list)

        for word in strs:
            sort = ''.join(sorted(word))
            anagrams[sort].append(word)
        
        for anagram in anagrams.keys():
            res.append(anagrams[anagram])
        
        return res
        
        