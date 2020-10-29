class Solution(object):
    def setcol(self,matrix,col):
        for i in range(len(matrix)):
            matrix[i][col]=0

    def findColRow(self,matrix):
        return_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    return_list.append([i,j])
        return return_list

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ###############
        #Set col and rows to 0 based on extra memory
        zero_list = self.findColRow(matrix)
        for zeros in zero_list:
            temp = [0]*len(matrix[zeros[0]])
            matrix[zeros[0]] = temp
            self.setcol(matrix,zeros[1])
