class Solution(object):


    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def check_board(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 'R':
                        return [i,j]

        [i,j] = check_board(board)
        temp = i-1
        count = 0
        while temp>0:
            if board[temp][j] == 'B':
                break
            elif board[temp][j] == 'p':
                count += 1
                # print("hi1")
                break
            temp -= 1
        temp = i + 1
        while temp<8:
            if board[temp][j] == 'B':
                break
            elif board[temp][j] == 'p':
                count += 1
                # print("hi2")
                break
            temp += 1
        temp = j + 1
        while temp<8:
            if board[i][temp] == 'B':
                break
            elif board[i][temp] == 'p':
                count += 1
                # print("hi3")
                break
            temp += 1
        temp = j - 1
        while temp>0:
            if board[i][temp] == 'B':
                break
            elif board[i][temp] == 'p':
                count += 1
                # print("hi4")
                break
            temp -= 1
        return count
                
