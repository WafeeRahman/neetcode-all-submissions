class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweetHeap = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweetHeap, (self.time, [userId, tweetId]))
        self.time -= 1




        

    def getNewsFeed(self, userId: int) -> List[int]:
        heapcopy = self.tweetHeap[:]
        res = []

        while heapcopy:
            if len(res) == 10:
                return res
            tweet = heapq.heappop(heapcopy)[1]
            if tweet[0] == userId or tweet[0] in self.following[userId]:
                res.append(tweet[1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if not followeeId in self.following[followerId]:
            self.following[followerId].add(followeeId)
            

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
