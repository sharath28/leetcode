class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxint


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        x = val
        if not self.stack:
            self.stack.append((x,x))
            return
        current_min = self.stack[-1][1]
        self.stack.append((x,min(x,current_min)))
        # if self.min > val:
        #     self.min = val


    def pop(self):
        """
        :rtype: None
        """
        # print(self.stack)
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
