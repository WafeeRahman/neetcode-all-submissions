class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweetMap = defaultdict(list)
        
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.tweetMap[userId].append([self.time, tweetId])
        self.time-=1 #Decrement Time, as we're using a max heap to get the most recent times
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        maxHeap = []
        
        for tweets in self.tweetMap[userId]:
            maxHeap.append(tweets)
        
        for users in self.following[userId]:
            for tweets in self.tweetMap[users]:
                if users != userId:
                    maxHeap.append(tweets)
        
        heapq.heapify(maxHeap)
        res = []
        while maxHeap and len(res) < 10:
            tweet = heapq.heappop(maxHeap)
            res.append(tweet[1])
        return res
                    

    def follow(self, followerId: int, followeeId: int) -> None:
        followerSet = self.following[followerId]
        followerSet.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followerSet = self.following[followerId]
        if followeeId in followerSet:
            followerSet.remove(followeeId)
        
