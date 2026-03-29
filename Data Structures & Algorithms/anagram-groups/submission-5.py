class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramMap = defaultdict(list)
        for string in strs:
            lettercount = [0] * 26
            for char in string:
                lettercount[ord(char) - ord('a')] += 1
            anagramMap[tuple(lettercount)].append(string)
        
        return(list(anagramMap.values()))



        