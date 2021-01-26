from math import sqrt
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while i*i<=num:
            if i*i==num:
                return True
            else:
                i = i + 1
        return False
