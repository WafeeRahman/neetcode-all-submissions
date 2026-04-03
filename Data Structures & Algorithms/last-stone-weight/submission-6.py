class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        negativeStones = [-x for x in stones]
        heapq.heapify(negativeStones)

        while len(negativeStones) > 1:
            x = heapq.heappop(negativeStones)
            y = heapq.heappop(negativeStones)
            x = -x
            y = -y
            diff = abs(x-y)
            if diff == 0:
                continue
            else:
                y = diff
                heapq.heappush(negativeStones, -y)
        return -negativeStones[0] if negativeStones else 0



                