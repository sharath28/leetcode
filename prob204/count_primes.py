from math import sqrt
class Solution(object):
    def isPrime(self, n):
        for i in range(2,int(sqrt(n)+1)):
            # print(i)
            if n%i == 0:
                return False
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count = 1
        # if n <= 2:
        #     return 0
        # # if n == 2:
        # #     return 1
        # for i in range(3,n):
        #     if self.isPrime(i):
        #         # print(i)
        #         count += 1
        # return count
        if n<=2:
            return 0

        prime=[1]*n

        for i in range(2,n):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j]=0
        return sum(prime)-2
