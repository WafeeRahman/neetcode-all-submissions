class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        subSet = []
        subSum = 0
       
        #Back Tracking Algorithm
        def BackTrack(i, nums):
            #Nonlocals to keeptrack of the subSet Sum in O(1) lookup
            #The current subset to add, and result vector to append to 
            nonlocal subSum, res, subSet
            
            #Base Case, if we traverse outside of the nums we can add
            #or If subSum >= target
            if i >= len(nums) or subSum >= target:
                print(subSet, subSum)

                #If Subsum is equal to target, add a copy of the subset and return
                if subSum == target:
                    res.append(subSet[:])
                return
            
            #To find all of the combinations with a certain number, keep adding it 
            #In each recursive call until we reach a return call
            #Which means either the subSum was too high, or we got a correct answer
            if subSum <= target:
                subSum += nums[i]
                subSet.append(nums[i])
            
            #Keep calling backtrack until we reach a return statement
            #i.e 2,2,2,2,2. 10 >= 9 return
            BackTrack(i, nums)
            
            #When we reach a return statement, subtract the latest added number
            #And pop from the subset
            subSum -= nums[i]
            subSet.pop()
            
            #Try the next number, if it doesnt work, continue popping
            if subSum + nums[i] > target:
                return
            BackTrack(i+1, nums)
        
        BackTrack(0, nums)

        return res
            







        