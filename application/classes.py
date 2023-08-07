import random


class Game:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0

    def is_win(self, player, opponent):
        if (
            (player == "rock" and opponent == "scissors")
            or (player == "scissors" and opponent == "paper")
            or (player == "paper" and opponent == "rock")
        ):
            return True

    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)

    def get_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif self.is_win(player_choice, computer_choice):
            self.player_score += 1
            return "You won!"
        else:
            self.computer_score += 1
            return "You lost!"
