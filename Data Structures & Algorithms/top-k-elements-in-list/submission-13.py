class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #Frequency (1..N)
        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        for num, count in count.items():
            freq[count].append(num)

        for i in range(len(freq) - 1, -1 , -1):
            if freq[i]:
                for j in range(len(freq[i]) -1, -1, -1):
                    if len(res) == k:
                        return res
                    res.append(freq[i][j])
        return res

