import tkinter as tk
from tkinter import messagebox, simpledialog
from dice_game_logic import DiceGame

class DiceGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Game")
        
        self.dice_game = DiceGame()
        
        self.label = tk.Label(root, text="Enter number of players:")
        self.label.pack()
        
        self.entry = tk.Entry(root)
        self.entry.pack()
        
        self.button = tk.Button(root, text="Start", command=self.start_game)
        self.button.pack()
        
    def start_game(self):
        try:
            num_players = int(self.entry.get())
            for i in range(num_players):
                self.add_player_dialog(i+1)
            
            self.label.destroy()
            self.entry.destroy()
            self.button.destroy()
            
            self.play_game()
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number of players.")
    
    def add_player_dialog(self, player_number):
        player_name = simpledialog.askstring("Player Name", f"Enter name for player {player_number}:")
        if player_name:
            self.dice_game.add_player(player_name)
        
    def play_game(self):
        result = self.dice_game.play_turn()
        if result:
            player_name, dice1, dice2 = result
            messagebox.showinfo(player_name, f"Dice 1: {dice1}\nDice 2: {dice2}")
            winner = self.dice_game.get_winner()
            if winner:
                messagebox.showinfo("Winner!", f"{winner} has won the game.")
                self.root.destroy()
            else:
                self.play_game()

if __name__ == "__main__":
    root = tk.Tk()
    game_gui = DiceGameGUI(root)
    root.mainloop()
