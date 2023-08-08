import random
from . import db


class GameResults(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_choice = db.Column(db.String(10), nullable=False)
    computer_choice = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(50), nullable=False)


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
            result = "It's a tie!"
        elif self.is_win(player_choice, computer_choice):
            self.player_score += 1
            result = "You won!"
        else:
            self.computer_score += 1
            result = "You lost!"

        db_result = GameResults(
            player_choice=player_choice, computer_choice=computer_choice, result=result
        )
        db.session.add(db_result)
        db.session.commit()
        return result
