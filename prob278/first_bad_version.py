# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low<=high:
            pivot = (low+high)//2
            if (isBadVersion(pivot)==True) and (isBadVersion(pivot-1)==False):
                return pivot
            elif isBadVersion(pivot)==True:
                high = pivot - 1
            else:
                low = pivot + 1
