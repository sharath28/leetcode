class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.temp_dict = {}


    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.temp_dict:
            self.temp_dict[message]=timestamp
            return True

        if timestamp - self.temp_dict[message] >=10:
            self.temp_dict[message]=timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)