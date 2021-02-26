class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(mat, visited,i):
            for j in range(len(mat)):
                if mat[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(mat,visited,j)

        visited = [0]*len(isConnected)
        count = 0
        for i in range(len(isConnected)):
            if visited[i] == 0:
                dfs(isConnected,visited,i)
                count += 1
        return count
