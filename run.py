from random import randint


class BattleshipsGame:
    def __init__(self, size=5, num_turns=4):
        """
        Start the battleship game with a given size 
        and number of turns.
        """
        self.size = size
        self.num_turns = num_turns
        self.board = [['O'] * size for _ in range(size)]
        self.ship_row = randint(0, size - 1)
        self.ship_col = randint(0, size - 1)
    
    
    def print_board(self):
        """
        Print the game board.
        """
        for row in self.board:
            print(" ".join(row))


    
    def validate_guess(self, row, col):
        """
        Validate if the guess is in the game board.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            return True
        else:
            print("Sorry , thats not on the board.")
            return False


    
    def make_guess(self):
        """
        Gets user to enter guess and validates if its in range.
        """
        while True:
            try:
                guess_input = input("Enter your guess (row, col) with a comma: ")
                guess_row, guess_col = map(int, guess_input.split(','))
                if self.validate_guess(guess_row, guess_col):
                    return guess_row, guess_col
            except ValueError:
                print("Please enter a guess in board range.")

    
    
    def play(self):
        """
        Main game functions of user and computers guesses.
        """
        print("Time for Battleships")
        self.print_board()
        
        turn = 0
        while turn < self.num_turns:
            print("Turn", turn + 1)
            guess_row, guess_col = self.make_guess()

            if guess_row == self.ship_row and guess_col == self.ship_col:
                print("You sunk my battleship!")
                return

            if self.board[guess_row][guess_col] == "X":
                print("You already guessed that one.")
                continue

            print("You missed!")
            self.board[guess_row][guess_col] = "X"
            self.print_board()
            turn += 1

        print("Game Over.")

    
if __name__ == "__main__":
    """
    Allows user yo play again.
    """
    while True:
        game = BattleshipsGame(size=5, num_turns=4)
        game.play()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break