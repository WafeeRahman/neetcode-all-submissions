class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, flag):
            if i >= len(nums) or (i == len(nums)-1 and flag):
                return 0
            if flag:
                return max((dfs(i+2, True) + nums[i]), dfs(i+1, True))
            elif flag == False:
                return max((dfs(i+2, False) + nums[i]), dfs(i+1, False))
            
            return max(dfs(0, True), dfs(1, False))

        
        
        cache = {}

        def memo(i, flag):
            nonlocal cache
            if len(nums) == 1:
                return nums[0]
            if i >= len(nums) or (i == len(nums)-1 and flag):
                return 0
            if (i, flag) in cache:
                return cache[i, flag]
            else:
                if flag == True:
                    cache[(i, flag)] = max((memo(i+2, True) + nums[i]), memo(i+1, True)) 
                elif flag == False:
                    cache[(i, flag)] = max((memo(i+2, False) + nums[i]), memo(i+1, False))
            return cache[(i, flag)]
        
        return max(memo(1, False), memo(0, True))
