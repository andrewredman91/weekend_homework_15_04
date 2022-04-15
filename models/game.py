from models.player import *

class Game():
    
    def get_game_result(player_1, player_2):
        if player_1.choice == "rock" and player_2.choice == "scissors":
            return "Player 1 wins by playing" + player_1.choice
        
        if player_1.choice == "scissors" and player_2.choice == "paper":
            return "Player 1 wins by playing " + player_1.choice
        
        if player_1.choice == "paper" and player_2.choice == "rock":
            return "Player 1 wins by playing " + player_1.choice
        if player_1.choice == player_2.choice:
            return None

        return "Player 2 wins by playing " + player_2.choice