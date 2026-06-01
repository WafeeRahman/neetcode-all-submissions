class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        adj = {}
        for word in wordList:
            adj[word] = []
        
        for i in range(len(wordList)):
           
            for j in range(len(wordList)):
                if wordList[i] == wordList[j]:
                    continue
                
                charDiff = 0
                for k in range(len(wordList[j])):
                    if wordList[i][k] != wordList[j][k]:
                        charDiff += 1
                if charDiff <= 1:
                    adj[wordList[i]].append(wordList[j])
        print(adj)

        visit = set([beginWord])
        q = deque([beginWord])
        trans=0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return trans+1
                print(node, adj[node])
                for nei in adj[node]:
                    if nei in visit:
                        continue
                    visit.add(nei)
                    q.append(nei)
            trans+=1
        return 0