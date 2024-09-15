import pprint
import inquirer
from RockPaperScissors import RPS
from GuessTheNumber import GuessTheNumber

class CLIGames:
    def __init__(self):
        self.questions = [
            inquirer.List(
                "game",
                message="What game do you want to play?",
                choices=["Rock Paper Scissors", "Guess the Number"],
            ),
        ]

    def start_game(self):
        answers = inquirer.prompt(self.questions)
        if answers["game"] == "Rock Paper Scissors":
            obj_rps = RPS()
            obj_rps.play_game()
        elif answers["game"] == "Guess the Number":
            obj_gtn = GuessTheNumber()
            obj_gtn.play_game()

obj_games = CLIGames()
obj_games.start_game()

