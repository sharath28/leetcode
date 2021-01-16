class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        def check_winner(board):
            for i in range(3):
                count_row_1,count_row_2 = 0,0
                count_col_1,count_col_2 = 0,0
                for j in range(3):
                    if board[i][j] == 'O':
                        count_row_1 += 1
                    if board[j][i] == 'O':
                        count_col_1 += 1
                    if board[i][j] == 'X':
                        count_row_2 += 1
                    if board[j][i] == 'X':
                        count_col_2 += 1
                if count_row_1 == 3 or count_col_1 == 3:
                    return 'A'
                elif count_row_2 == 3 or count_col_2 == 3:
                    return 'B'
                # print(count_row_2,count_col_2)
            if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
                return 'A'
            elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
                return 'B'
            if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
                return 'A'
            elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
                return 'B'
            return False

        board = [['']*3 for _ in range(3)]
        flag = 0
        for move in moves:
            if flag == 0:
                board[move[0]][move[1]] = 'O'
                result = check_winner(board)
                if result != False:
                    return result
                flag = 1
            elif flag == 1:
                board[move[0]][move[1]] = 'X'
                result = check_winner(board)
                if result != False:
                    return result
                flag = 0

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
