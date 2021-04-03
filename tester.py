import unittest
import game


class MyTestCase(unittest.TestCase):
    # Genius starts
    def test_genius_vs_random(self):
        # Random should never win
        genius_win = 0
        tie = 0

        num_of_repetitions = 3000
        for i in range(num_of_repetitions):
            ttc = game.TicTacToe()
            genius_player = game.GeniusComputerPlayer('X', False)
            random_player = game.RandomComputerPlayer('O', False)

            # Get the winner letter
            winner = game.play(ttc, genius_player, random_player, False)

            # Update variables, or fail if necessary
            if winner == 'X':
                genius_win += 1
            elif winner == 'O':
                self.fail('Random player won.')
            elif winner is None:
                tie += 1

        self.assertEqual(num_of_repetitions, genius_win + tie, f'{num_of_repetitions} games should have been played. Instead, {genius_win + tie} were played.')

    # Random starts
    def test_random_vs_genius(self):
        # Random should never win
        genius_win = 0
        tie = 0

        num_of_repetitions = 3000
        for i in range(num_of_repetitions):
            ttc = game.TicTacToe()
            random_player = game.RandomComputerPlayer('X', False)
            genius_player = game.GeniusComputerPlayer('O', False)

            # Get the winner letter
            winner = game.play(ttc, random_player, genius_player, False)

            # Update variables, or fail if necessary
            if winner == 'O':
                genius_win += 1
            elif winner == 'X':
                self.fail('Random player won.')
            elif winner is None:
                tie += 1

        self.assertEqual(num_of_repetitions, genius_win + tie, f'{num_of_repetitions} games should have been played. Instead, {genius_win + tie} were played.')

    def test_genius_vs_genius(self):
        # No one should ever win
        tie = 0

        num_of_repetitions = 300
        for i in range(num_of_repetitions):
            ttc = game.TicTacToe()
            genius_player1 = game.GeniusComputerPlayer('X', False)
            genius_player2 = game.GeniusComputerPlayer('O', False)

            # Get the winner letter
            winner = game.play(ttc, genius_player1, genius_player2, False)

            # Update variables, or fail if necessary
            if winner is None:
                tie += 1
            else:
                self.fail('Someone has won.')

        self.assertEqual(num_of_repetitions, tie, f'{num_of_repetitions} games should have been played. Instead, {tie} were played.')


if __name__ == '__main__':
    unittest.main()
