class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1
        l = 0
        r = 0

        while r < len(nums)-1:
            while r < len(nums)-1 and nums[r] == nums[r+1]:
                r+=1
            nums[l] = nums[r]
            l+=1
            r+=1
        
        print(nums, l, r)
        if r==len(nums)-1 and nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l+=1
        return l

            

        """
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] = 1
        
        i=0
        k=0
        for key in countMap.keys():
            if countMap[key] > 0:
                nums[i] = key
                countMap[key] = 0
                k+=1
            else:
                nums[i] = 0
            i+=1
        return k
        """

        