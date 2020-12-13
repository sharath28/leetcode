class Solution(object):
    def _dfs(self, i, j, g, c):
        if (i, j) in c:
            return c[(i,j)]
        pMax = 1
        c[(i,j)] = pMax
        for (iN,jN) in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if iN < 0 or iN >= len(g) or jN < 0 or jN >= len(g[iN]):
                continue
            if g[iN][jN] <= g[i][j]:
                continue
            pMax = max(pMax, 1+self._dfs(iN, jN, g, c))
        c[(i,j)] = pMax
        return pMax

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        g = matrix
        pCache = {}
        pMax = 0
        for i in range(len(g)):
            for j in range(len(g[i])):
                pMax = max(pMax, self._dfs(i, j, g, pCache))
        return pMax
