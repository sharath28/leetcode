class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #################
        #Linear Search after we find the column
        # i = 0
        # while i<len(matrix):
        #     if len(matrix[i])<=0:
        #         i+=1
        #         continue
        #     if target>matrix[i][len(matrix[i])-1]:
        #         i += 1
        #         continue
        #     else:
        #         j = 0
        #         while j<len(matrix[i]):
        #             if matrix[i][j]==target:
        #                 return True
        #             j += 1
        #         return False
        # return False

        ##################
        #Binary Matrix
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        left, right = 0, m*n-1
        while left<=right:
            pivot_id = (left+right)//2
            pivot_element = matrix[pivot_id//n][pivot_id%n]
            if pivot_element == target:
                return True
            else:
                if target < pivot_element:
                    right = pivot_id -1
                else:
                    left = pivot_id + 1
        return False
