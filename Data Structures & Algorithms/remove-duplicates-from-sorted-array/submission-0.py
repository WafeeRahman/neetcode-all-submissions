class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
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
            

        