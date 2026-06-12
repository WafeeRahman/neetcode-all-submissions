class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        print(coins)
        memo = {}
        if amount == 0:
            return 0
        def dfs (amt):
            if amt == amount:
                return 0
            if amt > amount:
                return -1
            
            if amt in memo:
                return memo[amt]
            
            for choice in coins:
                coinChanges = 1 + dfs(amt+choice)
                if coinChanges != 0:
                    memo[amt] = min(memo.get(amt, float('inf')), coinChanges) 

            if amt in memo:
                return memo[amt]    

            
            memo[amt] = -1
            return memo[amt]
        dfs(0)
        return memo[0]