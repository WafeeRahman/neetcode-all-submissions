class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = defaultdict(list)
      
        #Build Adjacency List Based off of the patterns
        #We can create by replacing one letter at a time
        #In Word

        for word in wordList:
            for i in range(len(word)):
                wordCopy = list(word)
                wordCopy[i] = "*"
                adjList[''.join(wordCopy)].append(word)
                
  
        def bfs(node, target, adjList):
            visit = set()
            visit.add(node)
            queue = deque([node])
            lengthReps = 1
            while queue:
                for i in range(len(queue)):
                    word = queue.popleft()
                    if word == target:
                        return lengthReps
        
                    for i in range(len(word)):
                        qNode = word[:i] + "*" + word[i+1:len(word)]
                        print(qNode)
                        for nei in adjList[qNode]:
                            print(nei)
                            if nei not in visit:
                                queue.append(nei)
                                visit.add(nei)
                lengthReps += 1
            return 0
        return bfs(beginWord, endWord, adjList)




            

        
        


