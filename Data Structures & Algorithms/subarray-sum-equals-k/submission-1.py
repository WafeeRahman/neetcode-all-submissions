class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
       preSum = {0:1}
       curSum = 0
       res = 0
       for num in nums:
           curSum += num #Populate Presums
           difference = curSum - k
           
           #Res = Current Sum + How Many ways to get k by taking away a prefix sum
           res += preSum.get(difference, 0)
           preSum[curSum] = 1 + preSum.get(curSum, 0) #Add Presum to Contig. Hashmap
            
       return res
        

        
