from flask import render_template, request
from .classes import Game
from . import app

game = Game()


@app.route("/", methods=["GET", "POST"])
def play_game():
    result = None
    player_score = game.player_score
    computer_score = game.computer_score
    if request.method == "POST":
        player_choice = request.form["choice"]
        computer_choice = game.get_computer_choice()
        result = game.get_winner(player_choice, computer_choice)
    return render_template(
        "index.html",
        result = result,
        player_score = player_score,
        computer_score = computer_score
    )
