import math
import random
import time


class Player:
    def __init__(self, letter, print_game = True):
        self.letter = letter
        self.print_game = print_game

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter, print_game = True):
        super().__init__(letter, print_game)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        if self.print_game:
            print(self.letter + f'\'s turn. Input move (0-8): {square}')

        return square


class HumanPlayer(Player):
    def __init__(self, letter, print_game = True):
        super().__init__(letter, print_game)

    def get_move(self, game):
        while True:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            
            try:
                # Type cast
                square = int(square)

                # If not valiid move
                if square not in game.available_moves():
                    raise ValueError
                break
            except ValueError:
                print('Invalid square. Try again.')
                print()

        return square


class GeniusComputerPlayer(Player):
    def __init__(self, letter, print_game = True):
        super().__init__(letter, print_game)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # Grab some random spot
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        # Current players
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # If currently someone has won
        if state.current_winner == other_player:
            return {'position': None,
                    'score': (state.num_empty_squares() + 1) * (1 if other_player == max_player else -1)}

        # If tie
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        # Create return dictionary
        best = {'position': None,
                'score': -math.inf if player == max_player else math.inf}

        for possible_move in state.available_moves():
            # Make a move, try the spot
            state.make_move(possible_move, player)

            # Recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)

            # Undo the move
            state.board[possible_move] = ' '
            state.current_winner = None

            # Keep track of the current move
            sim_score['position'] = possible_move

            # Update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

