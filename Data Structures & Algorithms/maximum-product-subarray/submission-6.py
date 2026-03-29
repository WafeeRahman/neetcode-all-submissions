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
            #Keep track of the max, setting it the maximum value in the subarray
            #Which is the current Maximum * current number, or the currentMinimum * num in case that num is negative and currmin is negative
            #Or the number itself

            #This is how we keep currMax contigous, as we never compare the max with itself
               #CurrMax*num - if the max continues to increase, increase the maxproduct
               #CurrMin *num, if the current number and current min are negative and their product is
                  #Greater than the contigous product, then create a new window with this value starting
                  #OTWS if num is greater than the contigous max and the current max*num, then start a new window with it
            currMax = max(currProd, currMin * num, num)
            #Keep the current minimum contigous with the current subbarray
            currMin = min(currMin*num, num, currProd)
            res=max(currMax, res)
        return res



            

                




        