class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = {}
        self.following = {}
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        user_tweets = self.tweets.get(userId)
        if user_tweets == None:
            self.tweets[userId] = [(tweetId, self.order)]
        else:
            self.tweets[userId] = user_tweets + [(tweetId, self.order)]
        self.order = self.order + 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        feed_users = self.following.get(userId)
        if feed_users == None:
            feed_users = set()
            feed_users.add(userId)
        else:
            feed_users.add(userId)
        tweets = []
        for user in feed_users:
            if user_tweets := self.tweets.get(user):
                    tweets.extend(user_tweets)
        tweets.sort(key=lambda x: -x[1])
        return [t[0] for t in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        
        following = self.following.get(followerId)
        if following == None:
            following = set()
            following.add(followeeId)
            self.following[followerId] = following
        else:
            following.add(followeeId)
            self.following[followerId] = following

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        following = self.following.get(followerId)
        if following == None:
            return None
        else:
            self.following[followerId] = following.difference(set([followeeId]))
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
