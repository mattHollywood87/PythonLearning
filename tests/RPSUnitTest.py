import unittest
from unittest.mock import patch
from RockPaperScissors import RPS
from unittest.mock import MagicMock

class RpsTests(unittest.TestCase):
    @patch('builtins.input', return_value='rock')
    def test_get_user_choice(self, mock_input):
        obj_rps = RPS()
        result = obj_rps.get_user_choice()
        self.assertEqual(result,'rock')


    def test_get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        obj_rps = RPS()
        result = obj_rps.get_computer_choice()
        self.assertTrue(result in choices)

    def test_determine_winner(self):
        test_cases = [
            ('rock', 'scissors', 'You win!'),
            ('paper', 'paper', "It's a tie!"),
            ('scissors', 'rock', 'You lose!'),
        ]
        obj_rps = RPS()
        for user_choice, computer_choice, answer in test_cases:
            self.assertEqual(obj_rps.determine_winner(user_choice, computer_choice),answer)

    def test_play_game(self):
        obj_rps = RPS()
        RPS.get_user_choice = MagicMock(return_value='rock')
        RPS.get_computer_choice = MagicMock(return_value='scissors')
        self.assertEqual(obj_rps.play_game(), 'You win!')

if __name__ == '__main__':
    unittest.main()