class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = 1
        count = 0
        while True:
            if temp == n:
                return True
            elif temp > n:
                return False
            else:
                temp = temp*3
                count += 1
        
