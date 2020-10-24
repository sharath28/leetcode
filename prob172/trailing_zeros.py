class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
#Time Limit Exceeded
#         n_fact = 1
#         for i in range(2,n+1):
#             n_fact *= i

#         z_count = 0
#         while n_fact % 10 == 0:
#             z_count += 1
#             n_fact //= 10
#         return z_count
#################
# #5 factor
#         z_count = 0
#         for i in range(5,n+1,5):
#             curr = i
#             while curr%5==0:
#                 z_count += 1
#                 curr //= 5
#         return z_count
##################
# 5 power
        z_count = 0
        for i in range(5,n+1,5):
            power = 5
            while i%power==0:
                z_count += 1
                power *= 5
        return z_count
