from collections import defaultdict
from random import choice

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.idx = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.idx[val].add(len(self.list))
        self.list.append(val)
        return len(self.idx[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.idx[val]: return False
        remove, last = self.idx[val].pop(), self.list[-1]
        self.list[remove] = last
        self.idx[last].add(remove)
        self.idx[last].discard(len(self.list)-1)
        self.list.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
