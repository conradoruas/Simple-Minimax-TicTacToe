class AI:
    def best_move(self, board):
        best_eval = float('-inf')
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = self.minimax(board, 0, False)
                    board[i][j] = ' '
                    if eval > best_eval:
                        best_eval = eval
                        best_move = (i, j)
        return best_move

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(board, 'X'):
            return -1
        if self.check_winner(board, 'O'):
            return 1
        if self.is_full(board):
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        eval = self.minimax(board, depth + 1, False)
                        board[i][j] = ' '
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        eval = self.minimax(board, depth + 1, True)
                        board[i][j] = ' '
                        min_eval = min(min_eval, eval)
            return min_eval

    def check_winner(self, board, player):
        for row in board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_full(self, board):
        return all(cell != ' ' for row in board for cell in row)