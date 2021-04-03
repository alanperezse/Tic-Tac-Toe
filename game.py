from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count('-')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + (i * 3)] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game = True):
    # Print instructions.
    if print_game:
        game.print_board_nums()
        print()

    letter = 'X'
    # Iterate while the game still has empty squares.
    while game.empty_squares():
        # Make a player make a move.
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        # Place the letter in the spot chosen by the player
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to {square}')

            # Print board
            if print_game:
                game.print_board()

        # If someone has won
        if game.winner(square, letter):
            if print_game:
                print()

            return letter

        letter = 'X' if letter == 'O' else 'O'

        if print_game:
            print()

        # Wait before asking for next input
        if print_game:
            time.sleep(1.5)

    # Tie
    return None


if __name__ == '__main__':
    p1 = input('Press (h) for human, (m) for machine. Player 1 will be:')
    p2 = input('Press (h) for human, (m) for machine. Player 2 will be:')
    print()

    player1 = HumanPlayer('X') if p1 == 'h' else GeniusComputerPlayer('X')
    player2 = HumanPlayer('O') if p2 == 'h' else GeniusComputerPlayer('O')

    t = TicTacToe()

    winner = play(t, player1, player2)

    t.print_board()

    if winner == 'X' or winner == 'O':
        print(winner + ' player is the winner!!!')
    else:
        print('Tie!!!')
