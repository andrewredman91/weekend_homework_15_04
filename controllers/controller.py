from flask import render_template, request, redirect
from app import app
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/<player1_choice>/<player2_choice>')
def a(player1_choice, player2_choice):
    player1 = Player("player1", player1_choice)
    player2 = Player("player2", player2_choice)
    result = Game.get_game_result(player1, player2)

    
    return render_template('results.html', title='results', result=result)

