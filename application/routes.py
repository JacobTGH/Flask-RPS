from flask import render_template, request, redirect, url_for, session
from .classes import Game, GameResults
from . import app, db


game = Game()


@app.route("/", methods=["GET", "POST"])
def play_game():
    result = None
    if request.method == "POST":
        player_choice = request.form["choice"]
        computer_choice = game.get_computer_choice()
        result = game.get_winner(player_choice, computer_choice)
        session["player_score"] = game.player_score
        session["computer_score"] = game.computer_score
    return render_template(
        "index.html",
        result=result,
        player_score=session.get("player_score", 0),
        computer_score=session.get("computer_score", 0),
    )


@app.route("/results", methods=["GET", "POST"])
def show_results():
    game_results = GameResults.query.all()
    return render_template("results.html", game_results=game_results)


@app.route("/clear_results", methods=["POST"])
def clear_results():
    GameResults.query.delete()
    db.session.commit()

    session["player_score"] = 0
    session["computer_score"] = 0

    return redirect(url_for("show_results"))
