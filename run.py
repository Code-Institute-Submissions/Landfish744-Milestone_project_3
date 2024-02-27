from random import randint

class BattleshipsGame:
    def __init__(self, size=5, num_turns=4):
        self.size = size
        self.num_turns = num_turns
        self.board = [['O'] * size for _ in range(size)]
        self.ship_row = randint(0, size - 1)
        self.ship_col = randint(0, size - 1)
    
    # Prints game board
    def print_board(self):
        for row in self.board:
            print(" ".join(row))


    # Validates guess of the user
    def validate_guess(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            return True
        else:
            print("Sorry , thats not on the board.")
            return False


    def make_guess(self):
        while True:
            try:
                guess_input = input("Enter your guess (row, col) with a comma: ")
                guess_row, guess_col = map(int, guess_input.split(','))
                if self.validate_guess(guess_row, guess_col):
                    return guess_row, guess_col
            except ValueError:
                print("Please enter a guess in board range.")

    
    # Main game functions
    def play(self):
        print("Time for Battleships")
        self.print_board()

    
if __name__ == "__main__":
    game = BattleshipsGame(size=5, num_turns=4)
    game.play()