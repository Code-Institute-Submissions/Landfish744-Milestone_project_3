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

    def play(self):
        """
        Main game functions of user and computers guesses.
        """
        print("Time for Battleships")
        self.print_board()

        turn = 0
        while turn < self.num_turns:
            print("Turn", turn + 1)

            guess_input = input(
                "Enter your guess (row, col) with a comma, or type 'quit': ")
            if guess_input.lower() == 'quit':
                print("Quitting game.")
                return

            try:
                guess_row, guess_col = map(int, guess_input.split(','))
                if not self.validate_guess(guess_row, guess_col):
                    print("Please enter a guess in board range.\n")
                    continue

                if guess_row == self.ship_row and guess_col == self.ship_col:
                    print("You sunk my battleship!")
                    return

                if self.board[guess_row][guess_col] == "X":
                    print("You already guessed that one.")
                    continue

                print("You missed!")
                self.board[guess_row][guess_col] = "X"
                self.print_board()
            except ValueError:
                print("Please enter a guess in board range.")
                continue

            comp_guess_row = randint(0, self.size - 1)
            comp_guess_col = randint(0, self.size - 1)
            print("Computer guesses:", comp_guess_row, comp_guess_col)

            if comp_guess_row == self.ship_row and \
               comp_guess_col == self.ship_col:
                print("Computer sunk your battleship!")
                return

            if self.board[comp_guess_row][comp_guess_col] == "X":
                print("Computer already guessed that one.")
                continue

            print("Computer missed!")
            self.board[comp_guess_row][comp_guess_col] = "X"
            self.print_board()
            turn += 1

        print("Game Over.")


if __name__ == "__main__":
    """
    Allows user to choose game board size , number of turns and play again.
    """
    while True:
        try:
            print("Rules: You choose turns and grid size.")
            print("User and computer will choose starting from 0,0.")
            print("Game ends when turns end or player/computer hits ship.")
            print("You can type 'quit' to end game/start a new game.")
            size = input(
                "Enter the size of the game board: ").lower().strip()
            if size == "quit":
                print("thank you for playing")
                exit()
            size = int(size)
            possible_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            while int(size) not in possible_sizes:
                print("Size must be in range from 1 to 12.")
                print("That was not a quit command or a number!")
                size = input("Enter the size of the game board: ").strip()
            num_turns = int(input("Enter the number of turns: "))
            if num_turns not in possible_sizes:
                raise ValueError(
                    "Number of turns must be in range from 1 to 12.")
            game = BattleshipsGame(size=size, num_turns=num_turns)
            game.play()
        except ValueError as e:
            print("Error:", e)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
