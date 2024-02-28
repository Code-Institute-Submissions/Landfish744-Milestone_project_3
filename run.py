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
            print("Sorry , thats not on the board.\n")
            return False


    def play(self):
        """
        Main game functions of user and computers guesses.
        """
        print("Time for Battleships\n")
        self.print_board()
        
        turn = 0
        while turn < self.num_turns:
            print("Turn", turn + 1)
            
            guess_input = input("Enter your guess (row, col) with a comma, or type 'quit' to end the game: \n")
            if guess_input.lower() == 'quit':
                print("Quitting game.\n")
                return
            
            try:
                guess_row, guess_col = map(int, guess_input.split(','))
                if self.validate_guess(guess_row, guess_col):
                    if guess_row == self.ship_row and guess_col == self.ship_col:
                        print("You sunk my battleship!\n")
                        return

                    if self.board[guess_row][guess_col] == "X":
                        print("You already guessed that one.\n")
                        continue

                    print("You missed!")
                    self.board[guess_row][guess_col] = "X"
                    self.print_board()
                    turn += 1
            except ValueError:
                print("Please enter a guess in board range.\n")
        
        print("Game Over.")


    
if __name__ == "__main__":
    """
    Allows user to choose game board size , number of turns and play again.
    """
    while True:
        try:
            print("Rules: You choose turns and grid size.")
            print("User and computer will choose starting from 0,0.")
            print("Game will end at end of turns or when player or computer hits a ship.")
            print("You can also type 'quit' to end game or start a new game.\n")
            size = int(input("Enter the size of the game board: \n"))
            if size < 1:
                raise ValueError("Size must be a 1 or above.\n")
            num_turns = int(input("Enter the number of turns: \n"))
            if num_turns < 1:
                raise ValueError("Number of turns must be 1 or above.\n")
            game = BattleshipsGame(size=size, num_turns=num_turns)
            game.play()
        except ValueError as e:
            print("Error:", e)
        
        play_again = input("Do you want to play again? (yes/no): \n").lower()
        if play_again != 'yes':
            break