class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)
        for string in strs:
            wordCount = [0] * 26
            for letter in string:
                wordCount[ord(letter) - ord('a')] += 1
            key = tuple(wordCount)
            anaMap[key].append(string)
        
        return [anaMap[key] for key in anaMap]
            