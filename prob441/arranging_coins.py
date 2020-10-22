class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        stair = 1
        while n>0:
            n = n - stair
            stair += 1
            count += 1
        if n == 0:
            return count
        else:
            return count - 1
