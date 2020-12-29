class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        seen = [[0]*len(mat[0]) for _ in range(len(mat))]
        # print(seen)
        i, j = 0, 0
        ans = 0
        while i <= len(mat)-1:
            ans += mat[i][i]
            seen[i][i] = 1
            i += 1
        i = 0
        j = len(mat)-1
        while i <= len(mat)-1 and j >= 0:
            if seen[i][j] == 0:
                seen[i][j] = 1
                ans += mat[i][j]
            i += 1
            j -= 1
        return ans
                
