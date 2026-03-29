class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        if not prerequisites:
            return True

        #For each 2-tuple of course a and prereq b
        #Build Adjacency List For Each Course In Prerequisites
        #Map the course that needs the prerequisite (a) to a node (key)
        #And the course that is the prerequisite (b) to a node (key)
        for i in range(len(prerequisites)):
            if not prerequisites[i][0] in adjList:
                adjList[prerequisites[i][0]] = []
            if not prerequisites[i][1] in adjList:
                adjList[prerequisites[i][1]] = []

            #Add The Prerequisite as b as a directed edge to a
            adjList[prerequisites[i][0]].append(prerequisites[i][1])
        
        #If there is a cycle, that tells us that 
        #A course is a prequisite for a prerequisite
        #That is, a has prerequisite b, but b has prerequisite a, which is impossible
        #And invalid
        #DFS on each course and its associated prerequisites, keeping track each course we visited
        def dfs(node, adjList, visit):
            #If we've already visited this node in the current path
            #Then there is a cycle
            if node in visit:
                return False
            
            #Add The node
            visit.add(node)
            print(adjList)
            print(visit)
            
            #For each node adjacent, run dfs on the neighbor
            for neighbor in adjList[node]:
                #If the dfs returns false, there is a cycle
                cycle = dfs(neighbor, adjList, visit)
                if not cycle:
                    return False
            #If the prerequisite path is valid, pop the current node
            visit.remove(node)
            return True

        for course in adjList.keys():
            if not dfs(course, adjList, set()):
                return False
        return True

        
            