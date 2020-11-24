# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low<=high:
            pivot = (low+high)//2
            if guess(pivot)==0:
                return pivot
            elif guess(pivot)==1:
                low = pivot + 1
            elif guess(pivot)==-1:
                high = pivot - 1
