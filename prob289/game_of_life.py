class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def find_count(board,i,j):
            cells = [(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
            one_count = 0
            for cell in cells:
                x1,y1 = i+cell[0],j+cell[1]
                if x1<0 or x1>= len(board) or y1<0 or y1>=len(board[0]):
                    continue
                else:
                    if board[x1][y1] == 1:
                        one_count += 1
            return one_count


        final_board = [[2]*len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                one_count = find_count(board,i,j)
                if board[i][j] == 0:
                    if one_count == 3:
                        final_board[i][j] = 1
                    else:
                        final_board[i][j] = 0
                elif board[i][j] == 1:
                    if one_count <2:
                        final_board[i][j] = 0
                    if one_count == 2 or one_count == 3:
                        final_board[i][j] = 1
                    if one_count > 3:
                        final_board[i][j] = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = final_board[i][j]
