class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        curComb = []
        def genComb(i, curSum):
            if curSum >= target:
                if curSum == target:
                    res.append(curComb[:])
                return
            if i >= len(candidates):
                if curSum == target:
                    res.append(curComb[:])
                return
            

            
            curComb.append(candidates[i])
            genComb(i+1,curSum+candidates[i])
            curComb.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1  
            genComb(i+1, curSum)
        genComb(0, 0)
        return res