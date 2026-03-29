class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0 

        while maxHeap or queue:
            top = None
            if maxHeap:
                top = heapq.heappop(maxHeap) 
                top += 1
            
            if top and top < 0:
                queue.append([top,time+n])
            
            

            print(maxHeap, queue, time)
            
            if queue and time >= queue[0][1]:
                x = queue.popleft()
                heapq.heappush(maxHeap, x[0])
            
            time += 1
        
        return time
            