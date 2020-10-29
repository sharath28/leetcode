class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 1
        y = 2
        if n == 1:
            return 1
        elif n == 2:
            return 2
        for i in range(2,n):
            x,y = y,x+y
        return y
