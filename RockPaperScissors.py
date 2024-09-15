import random

class RPS:
    def get_user_choice(self):
        user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
        return user_choice
    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        return computer_choice
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "You lose!"

    def play_game(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")
        result = self.determine_winner(user_choice, computer_choice)
        print(result)
        return result