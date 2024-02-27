from random import randint

class BattleshipsGame:
    def __init__(self, size=5, num_turns=4):
        self.size = size
        self.num_turns = num_turns
        self.board = [['O'] * size for _ in range(size)]

    
    # Prints game board
    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    
    # Main game functions
    def play(self):
        print("Time for Battleships")
        self.print_board()

    
if __name__ == "__main__":
    game = BattleshipsGame(size=5, num_turns=4)
    game.play()