class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        res = []
      
        i=0

        while i < len(nums):

            while i >= 1 and i < len(nums) and nums[i] == nums[i-1]:
                i+=1

            j = i+1
            k = len(nums)-1
            print(i)

            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    print(i,j,k)
                    j+=1
                    k-=1
                    
                    while k>0 and nums[k] == nums[k+1]:
                        k-=1
                    
                    while j<len(nums) and nums[j] == nums[j-1]:
                        j+=1
            i+=1
        return res




        