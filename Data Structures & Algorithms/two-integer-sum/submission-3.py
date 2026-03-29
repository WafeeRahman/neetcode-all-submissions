#With an array of integers called nums, and a target, return the indexes of nums i and j where they are inequal and sum to target
#IE nums = [3,4,5,6], target = 7, nums[0] + nums[1] = 7 (3+4)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We can store the values as keys in a hashmaps, and their index positions as values

        valMap = {}

        for i in range(len(nums)):
            if target - nums[i] in valMap:
                return [valMap[target - nums[i]], i]
            valMap[nums[i]] = i
        
        return [-1,-1]


        