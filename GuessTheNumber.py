import random

class GuessTheNumber:
    def get_user_choice(self):
        user_choice = input("Enter a number between 1 and 10: ")
        return user_choice

    def get_random_number(self):
       computer_choice = random.randint(1, 10)
       return computer_choice

    def determine_winner(self, user_choice, computer_choice):
       if user_choice == computer_choice:
           return ("You win! Computer chose: {}".format(computer_choice))
       else:
           return ("You lose! Computer chose: {}".format(computer_choice))

    def play_game(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_random_number()
        result = self.determine_winner(user_choice, computer_choice)
        print(result)
        return result