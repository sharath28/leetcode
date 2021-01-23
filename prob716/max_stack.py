class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.list = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)

    def pop(self):
        """
        :rtype: int
        """
        temp = self.list.pop()
        return temp

    def top(self):
        """
        :rtype: int
        """
        temp = self.list[len(self.list)-1]
        return temp


    def peekMax(self):
        """
        :rtype: int
        """
        temp = max(self.list)
        return temp


    def popMax(self):
        """
        :rtype: int
        """
        self.list = self.list[::-1]
        temp = max(self.list)
        self.list.remove(temp)
        self.list = self.list[::-1]
        return temp


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
