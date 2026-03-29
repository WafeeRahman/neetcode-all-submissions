class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        preFixArr = [1] * len(nums)
        postFixArr = [1] * len(nums)
        preFixProduct = 1
        postFixProduct = 1
        
        for i in range(len(nums)): 
            preFixProduct *= nums[i]
            preFixArr[i] = preFixProduct

            
            postFixProduct *= nums[len(nums)-1-i]
            postFixArr[len(nums)-1-i] = postFixProduct
            

        print(preFixArr)
        print(postFixArr)

        for i in range(len(nums)):
            preLeft = preFixArr[i-1] if i > 0 else 1
            postRight = postFixArr[i+1] if i < (len(nums) -1) else 1
            res.append(preLeft*postRight)

        return res

        
