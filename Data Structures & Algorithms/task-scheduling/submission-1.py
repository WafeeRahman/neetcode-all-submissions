class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Counter will take count for all of the tasks, and leave all empty entries out
        #Given that there is a pattern (tasks repeat within range A-Z within the list of tasks)
        #We can use Counter to take the count
        #Place into a maxHeap by negating each count in heapq for each value in the count hashmap
        counts = [0] * 26
        maxHeap = []
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        for count in counts:
            if count > 0:
                maxHeap.append(-count)
        
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
            
            if queue and time >= queue[0][1]:
                x = queue.popleft()
                heapq.heappush(maxHeap, x[0])
            
            time += 1
        
        return time
            