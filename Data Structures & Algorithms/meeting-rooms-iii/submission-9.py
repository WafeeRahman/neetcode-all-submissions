class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        free = [i for i in range(n)]
        minHeap = []
        roomCount = defaultdict(int)

        for interval in meetings:
            while minHeap and minHeap[0][0] <= interval[0]:
                heapq.heappush(free, heapq.heappop(minHeap)[1])
                
            if free:
                room = heapq.heappop(free)
                heapq.heappush(minHeap, (interval[1], room)) 
                roomCount[room] += 1
            else:
                
                releaseTime, room = heapq.heappop(minHeap)
                heapq.heappush(free, room)
                #Skip time and free up other rooms
                while minHeap and minHeap[0][0] <= interval[0]:
                    heapq.heappush(free, heapq.heappop(minHeap)[1])

                
                delta = interval[1] - interval[0]
                room = heapq.heappop(free)
                heapq.heappush(minHeap, (delta+releaseTime, room))
                roomCount[room] += 1
               
        max = float('-inf')
        maxKey = None

        for key in range(0, n):
            if roomCount[key] > max:
                max = roomCount[key]
                maxKey = key
        return maxKey

          
                
