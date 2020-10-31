class Solution(object):
    def divisorGameUtil(self,N,A,dp):
        if N==1 or N ==3:
            return False
        if N == 2:
            return True

        if dp[N][A]!=-1:
            return dp[N][A]

        if A==1:
            ans = 0
        else:
            ans = 1

        for i in range(1,int(sqrt(N))+1,1):
            if N%i==0:
                if A:
                    ans |= self.divisorGameUtil(N-i,0,dp)
                else:
                    ans &= self.divisorGameUtil(N-i,1,dp)
        dp[N][A] = ans

        return dp[N][A]

    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp = [[-1 for i in range(2)] for j in range(N+1)]

        if self.divisorGameUtil(N,1,dp):
            return True
        else:
            return False
