import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_set = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.val_set:
            return False
        else:
            self.val_set.add(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_set:
            return False
        else:
            self.val_set.remove(val)
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        rand_int = random.randint(0,len(self.val_set)-1)
        if rand_int > len(self.val_set):
            return False
        return list(self.val_set)[rand_int]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
