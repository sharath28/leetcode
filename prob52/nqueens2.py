class Solution(object):
    def __init__(self):
        self.final_list = []


    def checkIfCorrect(self,board,n):
        queen_list = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == "Q":
                    queen_list.append((i,j))
        # print(queen_list)
        for i in range(len(queen_list)):
            for j in range(i+1,len(queen_list)):
                if (queen_list[i][0] == queen_list[j][0]) or (queen_list[i][1] == queen_list[j][1]):
                    return False
                elif abs(queen_list[i][0] - queen_list[j][0]) == abs(queen_list[i][1] - queen_list[j][1]):
                    return False
                else:
                    continue
        return True

    def backtrack(self,i,j,board,n):
        board[i][j] = "Q"
        board_consistent = self.checkIfCorrect(board,n)
        if j >= n:
            return
        if board_consistent == True and j == n-1:
            self.final_list.append(board)
        elif board_consistent == True:
            for i in range(n):
                temp_board = deepcopy(board)
                self.backtrack(i,j+1,temp_board,n)
        elif board_consistent == False:
            return

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = []
        for i in range(n):
            board.append(['.']*n)

        for i in range(n):
            j = 0
            temp_board = deepcopy(board)
            self.backtrack(i,j,temp_board,n)
        return len(self.final_list)
        
