class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def find_count(M,i,j):
            cells = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
            count = M[i][j]
            cell_count = 1
            for cell in cells:
                x1,y1 = i+cell[0],j+cell[1]
                if x1<0 or x1>=len(M) or y1<0 or y1>=len(M[0]):
                    continue
                else:
                    cell_count += 1
                    count += M[x1][y1]
            return count,cell_count

        final_board = [[0]*len(M[0]) for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                count,cell_count = find_count(M,i,j)
                final_board[i][j] = int(math.floor(count/cell_count))
        return final_board
