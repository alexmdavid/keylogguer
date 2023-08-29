import random

class DiceGame:
    def __init__(self):
        self.players = []
        self.current_player_index = 0
        
    def add_player(self, name):
        self.players.append(name)
        
    def roll_dice(self):
        return random.randint(1, 6), random.randint(1, 6)
        
    def play_turn(self):
        player_name = self.players[self.current_player_index]
        dice1, dice2 = self.roll_dice()
        
        if dice1 == 1 and dice2 == 1:
            self.players.pop(self.current_player_index)
            if self.current_player_index >= len(self.players):
                self.current_player_index = 0
        else:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
            
        return player_name, dice1, dice2
        
    def get_winner(self):
        if len(self.players) == 1:
            return self.players[0]
        return None
