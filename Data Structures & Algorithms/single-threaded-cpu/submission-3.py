class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        q = deque()
        notEnqueuedHeap = []
        maxTime = max([tasks[i][1] for i in range(len(tasks))])
        
        for i in range(len(tasks)):
            tasks[i].append(i)
            heapq.heappush(notEnqueuedHeap, tasks[i])
        
        taskHeap = []
        time = 0
        res = []
        while notEnqueuedHeap or taskHeap:
            
            while notEnqueuedHeap and time >= notEnqueuedHeap[0][0]:
                newTask = heapq.heappop(notEnqueuedHeap)
                print(newTask)
                completionTime = newTask[1]
                idx = newTask[2]
                heapq.heappush(taskHeap, [completionTime, idx, newTask])

            if taskHeap:
                    finished = heapq.heappop(taskHeap)[2]
                    res.append(finished[2])
                    time += finished[1]
            else:
                time=notEnqueuedHeap[0][0] 
        return res

        