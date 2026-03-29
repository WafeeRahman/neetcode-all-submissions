class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        a = 0
        valuesSet = set()
        res = []
        while a < len(nums):

            while a > 1 and a < len(nums) and nums[a] == nums[a-1]:
                a+=1
            
            b=a+1
            while b < len(nums):
                while b>a+1 and b < len(nums) and nums[b] == nums[b-1]:
                    b+=1
                
                c=b+1
                d=len(nums)-1
                while c < d:
                    abcSum = nums[a] + nums[b] + nums[c] + nums[d]

                    if abcSum > target:
                        d-=1
                    elif abcSum < target:
                        c+=1
                    else:
                        if not tuple([nums[a], nums[b], nums[c], nums[d]]) in valuesSet:
                            valuesSet.add(tuple([nums[a], nums[b], nums[c], nums[d]]))
                            res.append([nums[a], nums[b], nums[c], nums[d]])
                        c+=1
                        d-=1

                        while c < d and nums[c] == nums[c-1]:
                            c+=1
                        while d > c and nums[d] == nums[d+1]:
                            d-=1
                b+=1
            a+=1
        return res    



