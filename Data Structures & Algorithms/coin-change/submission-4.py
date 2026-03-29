#With an array of coin values, and a target value
#Find the minimum amount of coin values that it takes to add to target
#[1,5,10] target 12, 3 coins, 2 10s and 1 1
#We can use a coin an unlimited amount of times

#At each step we have the decision to add the current coin, or skip it and add the next coin .. up until the nth coin
#When find a valid pathsum to target, we add one to the result, we can then explore decisions where we skip a coin
#If the pathsum exceeds target, negate the coins being added
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(curSum):
            if curSum >= amount:
                if curSum == amount:
                    return 0
                return -1
            
            #With each coin, we have n choices, to include each of the coins in the current decision 
            minCoins = float('inf')
            for i in range(len(coins)):
                numCoins = 0
                numCoins = 1 + dfs(curSum + coins[i])
                if numCoins > 0:
                    minCoins = min(numCoins, minCoins)
            return minCoins if minCoins != float('inf') else -1
        
        #Memoization, storing previous calls with a cache
        #We can store the amount of minimum coins for each current sum to reach the target
        #Also storing a value that indicates whether the current sum reaching the target is possible or not

        cache = {}
        def memo(curSum):
            #Check for currentSum in cache to see if it has an associated minimum amt of coins
            if curSum in cache:
                return cache[curSum]

            if curSum >= amount:
                if curSum == amount:
                    return 0
                return -1
            #Set the initial cache value to infinity, as there hasnt been a computed min
            cache[curSum] = float('inf')
            for i in range(len(coins)):
                numCoins = 0
                numCoins = 1 + memo(curSum+coins[i])
                #Cache the minimum amount of coins required to get to target
                #At each current sum at for each decision, if we see a repeated current sum
                #That was already computed, we can use the cache to save on repeated work
                #If we get a computed path to the sum, set the number of coins it takes
                if numCoins > 0:
                    cache[curSum] = min(cache[curSum], numCoins)
            return cache[curSum] if cache[curSum] != float('inf') else -1
        
        #Bottom Up Dynamic Programming
        def dp(amount):
            dp = [amount+1] * (amount+1)
            dp[0] = 0

            for i in range(1, amount+1):
                coinSum = 0
                for coin in coins:
                    #If we can compute a value with the current coin
                    if i - coin >= 0:
                        dp[i] = min(dp[i], 1+dp[i-coin])
            return dp[amount] if dp[amount] != amount+1 else -1
        return dp(amount)



 

            


   
                
            

            
