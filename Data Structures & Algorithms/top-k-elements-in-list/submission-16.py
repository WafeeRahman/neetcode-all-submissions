class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Given an array of integers, return the top K elements based on frequency

        #[1,2,2,3,3,3] --> top 3 would be 3,2,1 (elements)

        #Few ways we can do this; sorting based on frequency, using a minheap and removing all elements until we're left with topk
        #Or we can do bucket sort, based on the frequencys that elements take
        #Regardless, our first step is to count the frequencies of the elements

        countNums = defaultdict(int)
        for i in range(len(nums)):
            countNums[nums[i]] += 1
        minHeap = []
        
        for num in countNums:
            minHeap.append([countNums[num], num])
        
        """
        heapq.heapify(minHeap)

        while len(minHeap) > k:
            heapq.heappop(minHeap)
        
        return [i[1] for i in minHeap]
        """

        frequencies = [[] for i in range(len(nums)+1)] #Frequencies range from 1..N inclusive

        for num in countNums:
            count = countNums[num]

            frequencies[count].append(num)
        
        res = []

        for i in range(len(frequencies)-1, -1, -1):
            if len(frequencies[i]) < 1:
                continue
            
            for num in frequencies[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res


        
