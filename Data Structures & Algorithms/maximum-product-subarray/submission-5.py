class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Kadanes Algorithm
        #We need to find a maximum product of a contigous product of a subarray
        #There can be negative and positive values in the array, which means we cannot
        #Change window based on if the product is negative or positive
        #Which means we need to keep track of negative products from the minimum product aswell



        res = max(nums)
        currMax = 1
        currMin = 1

        for num in nums:
            #If i is zero, it will zero out everything, therefore
            #Skip it and make a new window for subarray
            if num == 0:
                currMax = 1
                currMin = 1
                continue
            #Take the current product of the subarray
            currProd = currMax * num
            currMax = max(currMax*num, currMin * num, num)
            currMin = min(currMin*num, num, currProd)
            res=max(currMax, res)
        return res



            

                




        