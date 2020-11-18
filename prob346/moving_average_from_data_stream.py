class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.temp_list = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.temp_list.append(val)
        if len(self.temp_list)<self.size:
            temp = sum(self.temp_list)
            return float(temp)/float(len(self.temp_list))
        else:
            temp = self.temp_list[len(self.temp_list)-self.size:]
            return float(sum(temp))/float(self.size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
