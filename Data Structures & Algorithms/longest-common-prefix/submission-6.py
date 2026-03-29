class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixWord = strs[0]
        
        for i in range(1, len(strs)):
            longestCommonPrefix = ""
            word = strs[i]
            for j in range(len(word)):
                if j < len(prefixWord) and word[j] == prefixWord[j]:
                    longestCommonPrefix += word[j]
                else:
                    break
            prefixWord = longestCommonPrefix
        return prefixWord
                


        