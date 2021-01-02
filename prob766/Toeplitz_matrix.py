class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        i, j = 0,0
        val = matrix[0][0]
        for i in range(len(matrix[0])):
            j = 0
            k = i
            val = matrix[j][k]
            while True:
                if j >= len(matrix) or k >= len(matrix[0]):
                    break
                if matrix[j][k] != val:
                    return False
                k += 1
                j += 1
        for i in range(len(matrix)):
            j = 0
            k = i
            val = matrix[k][j]
            while True:
                if j >= len(matrix[0]) or k >= len(matrix):
                    break
                if matrix[k][j] != val:
                    return False
                k += 1
                j += 1
        return True
        # return True
        
