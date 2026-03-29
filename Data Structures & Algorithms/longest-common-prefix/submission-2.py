class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        prefixWord = strs[0]
        for word in range(1, len(strs)):
            pre = ""
            for i in range(len(strs[word])):
                if i < len(prefixWord):
                    if prefixWord[i] == strs[word][i]:
                        pre += strs[word][i]
                    else:
                        break
            prefixWord = pre

        return prefixWord



                