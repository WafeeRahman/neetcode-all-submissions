class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        sortedStringMap = {}
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString in sortedStringMap.keys():
                sortedStringMap[sortedString].append(string) 
            else: 
                sortedStringMap[sortedString] = [string]
        for key in sortedStringMap:
            res.append(sortedStringMap[key])
        return res
        