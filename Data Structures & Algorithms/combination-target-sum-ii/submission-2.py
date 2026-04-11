class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curComb = []
        candidates.sort()
        def genComb(i, curSum):
            if i >= len(candidates):
                if curSum == target:
                    res.append(curComb[:])
                return
            if curSum == target:
                res.append(curComb[:])
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                if curSum + candidates[j] <= target:
                    curComb.append(candidates[j])
                    genComb(j+1, curSum+candidates[j])
                    curComb.pop()
        
        genComb(0, 0)
        return res
