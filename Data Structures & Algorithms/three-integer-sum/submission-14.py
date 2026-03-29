class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        #Sort to Apply Two Sum II,  aswell as easy duplicates
        nums.sort()

        for i, v in enumerate(nums):
            
            if v >0: #Sum of any +tve values will always be greater than zero
                continue
            if i > 0 and v == nums[i-1]: #If we encounter a duplicate continue
                continue 
            
            #Run Two Sum II w/ Target ZERO
            l = i+1
            r = len(nums)-1
            while l < r:
                sumTotal = nums[i] + nums[l] + nums[r] 
                if sumTotal > 0:
                    r-=1
                elif sumTotal < 0:
                    l+=1
                else:
                    res.append([nums[i], nums[l], nums[r]]) #Append Solution
                    
                    #Move pointers
                    l+=1
                    r-=1

                    #Avoid Duplicates in L
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        return res
        