class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = []
        self.index = 0
        self.history.append(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        while self.index < len(self.history)-1:
            self.history.pop()
        self.history.append(url)
        self.index += 1

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.index - steps <= 0:
            self.index = 0
        else:
            self.index -= steps
        return self.history[self.index]


    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.index + steps >= len(self.history)-1:
            self.index = len(self.history)-1
        else:
            self.index += steps
        return self.history[self.index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
