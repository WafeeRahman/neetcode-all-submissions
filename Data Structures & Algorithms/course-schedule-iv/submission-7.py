class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for a, b in prerequisites:
            adj[a].append(b)


        def dfs(course, target, visit):
            if course == target:
                return True
            if course in visit:
                return False
            visit.add(course)
            for nei in adj[course]:
                if dfs(nei, target, visit):
                    return True
          
            return False
        
        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))
        
        return res

            