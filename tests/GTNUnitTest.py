import random
import unittest
from unittest.mock import patch
from GuessTheNumber import GuessTheNumber
from unittest.mock import MagicMock

class GtnTests(unittest.TestCase):
    @patch('builtins.input', return_value='1')
    def test_user_input(self, mock_input):
        obj_gtn = GuessTheNumber()
        result = obj_gtn.get_user_choice()
        self.assertEqual(result, "1")  # add assertion here

    def test_random_number(self):
        obj_gtn = GuessTheNumber()
        random.randint = MagicMock(return_value=1)
        result = obj_gtn.get_random_number()
        self.assertEqual(result, 1)

    def test_determine_winner(self):
        test_cases = [
            (1,1,"You win! Computer chose: 1"),
            (4, 1, "You lose! Computer chose: 1")
        ]
        for user_choice, computer_choice, result in test_cases:
            obj_gtn = GuessTheNumber()
            self.assertEqual(obj_gtn.determine_winner(user_choice, computer_choice), result)

    def test_play_game(self):
        obj_gtn = GuessTheNumber()
        obj_gtn.get_user_choice = MagicMock(return_value=1)
        obj_gtn.get_random_number = MagicMock(return_value=1)
        self.assertEqual(obj_gtn.play_game(), "You win! Computer chose: 1")

if __name__ == '__main__':
    unittest.main()
