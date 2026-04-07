class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort(key=lambda x: x[0])
        taskQ = deque(tasks)
        taskHeap = []
        res = []
        time = 0
        while taskQ or taskHeap:

            while taskQ and time >= taskQ[0][0]:
                task = taskQ.popleft()
                scheduledRelease = task[1]
                idx = task[2]
                heapq.heappush(taskHeap, (scheduledRelease, idx, task))
            if taskHeap:
                processingTime, idx, _ = heapq.heappop(taskHeap)
                time += processingTime
                res.append(idx)
            else:
                time = taskQ[0][0]
        return res
        