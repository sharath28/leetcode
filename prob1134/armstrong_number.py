class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        k = len(str(N))
        count = 0
        for num in str(N):
            count += int(num)**k
        if count == N:
            return True
        else:
            return False
