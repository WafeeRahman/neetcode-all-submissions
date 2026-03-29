class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket Sort, Count Frequencies and Place into Buckets

        count = {}
        buckets = [[] for i in range(len(nums)+1)] #Frequencies 

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for key in count:
            buckets[count[key]].append(key)

        res = []

        print(buckets)
        for i in range(len(buckets)-1, -1, -1):
            if not buckets[i]:
                continue
            for val in buckets[i]:
                res.append(val)
                if len(res) == k:
                    return res
        return res