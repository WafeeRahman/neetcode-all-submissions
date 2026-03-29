class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        if not prerequisites:
            return True

        for i in range(len(prerequisites)):
            if not prerequisites[i][0] in adjList:
                adjList[prerequisites[i][0]] = []
            if not prerequisites[i][1] in adjList:
                adjList[prerequisites[i][1]] = []
            adjList[prerequisites[i][0]].append(prerequisites[i][1])
        
        def dfs(node, adjList, visit):
            if node in visit:
                return False
            
            visit.add(node)
            print(adjList)
            print(visit)
            for neighbor in adjList[node]:
                cycle = dfs(neighbor, adjList, visit)
                if not cycle:
                    return False
            visit.remove(node)
            return True

        for course in adjList.keys():
            if not dfs(course, adjList, set()):
                return False
        return True

        
            