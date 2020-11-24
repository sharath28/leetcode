class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hit_list = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        self.hit_list.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        count = 0
        for i in range(len(self.hit_list)-1,-1,-1):
            if timestamp-self.hit_list[i]>=0 and timestamp-self.hit_list[i]<300:
                count += 1
            else:
                break
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
