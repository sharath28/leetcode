class Solution(object):

    def binary_search(self,matrix,target,start,vertical):
        low = start
        high = len(matrix[0])-1 if vertical else len(matrix)-1

        while high >= low:
            mid = (low+high)//2
            if vertical:
                if matrix[start][mid]<target:
                    low = mid + 1
                elif matrix[start][mid]>target:
                    high = mid - 1
                else:
                    return True
            else:
                if matrix[mid][start]<target:
                    low = mid + 1
                elif matrix[mid][start]>target:
                    high = mid - 1
                else:
                    return True
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ##################
        #Brute Force
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j]==target:
        #             return True
        # return False

        #################
        #Binary Search
#         if not matrix:
#             return False
#         for i in range(min(len(matrix),len(matrix[0]))):
#             v_found = self.binary_search(matrix,target,i,True)
#             h_found = self.binary_search(matrix,target,i,False)

#             if v_found or h_found:
#                 return True

#         return False
        ##################
        #Search Space Reduction
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        height = len(matrix)
        width = len(matrix[0])
        row = height-1
        col = 0
        while col<width and row >= 0:
            if matrix[row][col]>target:
                row -= 1
            elif matrix[row][col]<target:
                col += 1
            else:
                return True
        return False
