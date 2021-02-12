class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        # if K % 2 == 0:
        #     return -1
        # n = 1
        # count = 0
        # while count < pow(10,5):
        #     # print(n)
        #     if n % K == 0:
        #         return len(str(n))
        #     else:
        #         n = (n*10)+1
        #     count += 1
        # return -1
        remainder = 0
        for len_n in range(1,K+1):
            remainder = (remainder*10+1)%K
            if remainder == 0:
                return len_n
        return -1
