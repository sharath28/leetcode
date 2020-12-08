class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)

        if n*m == 0:
            return n + m

        d = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            d[i][0] = i
        for j in range(m+1):
            d[0][j] = j

        for i in range(1,n+1):
            for j in range(1,m+1):
                left = d[i-1][j] +1
                right = d[i][j-1] + 1
                left_down = d[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    left_down += 1
                d[i][j] = min(left,right,left_down)

        return d[n][m]
