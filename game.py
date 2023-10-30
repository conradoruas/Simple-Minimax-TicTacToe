import random
from ai import AI

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player_turn = random.choice(['X', 'O'])
        self.ai = AI()

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def play(self):
        while True:
            self.print_board()
            if self.player_turn == 'X':
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if self.board[row][col] == ' ':
                    self.board[row][col] = 'X'
                    self.player_turn = 'O'  # Troca o turno do jogador
            else:
                print("AI's turn (O)")
                row, col = self.ai.best_move(self.board)
                if row == -1 or col == -1:
                    print("It's a tie!")
                    self.print_board()
                    break
                self.board[row][col] = 'O'
                self.player_turn = 'X'  # Troca o turno do jogador

            if self.check_winner('X'):
                self.print_board()
                print("You win!")
                break
            elif self.check_winner('O'):
                self.print_board()
                print("AI wins!")
                break
            elif self.is_full():
                self.print_board()
                print("It's a tie!")
                break

