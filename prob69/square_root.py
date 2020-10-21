from math import e, log
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

# Calculator method
#         if x<2:
#             return x

#         left = int(e**(0.5*log(x)))
#         right = left + 1
#         return left if right*right > x else right

##########################
# Binary Search
#         if x < 2:
#             return x

#         left, right = 2, x//2
#         while left <= right:
#             pivot = left + (right-left)//2
#             num = pivot*pivot
#             if num > x:
#                 right = pivot - 1
#             elif num < x:
#                 left = pivot + 1
#             else:
#                 return pivot
#         return right
########################
#Recursion 
        if x < 2:
            return x
        left = self.mySqrt(x>>2)<<1
        right = left + 1
        return left if right * right > x else right
