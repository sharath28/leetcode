class RecentCounter(object):

    def __init__(self):
        self.temp_list = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.temp_list.append(t)
        while self.temp_list[0]<t-3000:
            self.temp_list.pop(0)

        return len(self.temp_list)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
