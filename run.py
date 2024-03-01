from random import randint


class BattleshipsGame:
    def __init__(self, size=5, num_turns=4):
        """
        Start the battleship game with a given size
        and number of turns.
        """
        self.size = size
        self.num_turns = num_turns
        self.user_board = [['O'] * size for _ in range(size)]
        self.computer_board = [['O'] * size for _ in range(size)]
        self.ship_row = randint(0, size - 1)
        self.ship_col = randint(0, size - 1)

    def print_board(self, board):
        """
        Print the game board.
        """
        for row in board:
            print(" ".join(row))

    def validate_guess(self, row, col):
        """
        Validate if the guess is in the game board.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            return True
        else:
            print("Sorry, that's not on the board.")
            return False

    def play(self):
        """
        Main game function for user and computer guesses.
        """
        print("Time for Battleships")
        self.print_board(self.user_board)

        turn = 0
        while turn < self.num_turns:
            print("Turn", turn + 1)

            user_guess_input = input("Enter your guess (row, col) with a comma, or type 'quit': ")
            if user_guess_input.lower() == 'quit':
                print("Quitting game.")
                return

            try:
                user_guess_row, user_guess_col = map(int, user_guess_input.split(','))
                if not self.validate_guess(user_guess_row, user_guess_col):
                    print("Please enter a guess within the board range.\n")
                    continue

                if user_guess_row == self.ship_row and user_guess_col == self.ship_col:
                    print("You sunk my battleship!")
                    return

                if self.user_board[user_guess_row][user_guess_col] == "X":
                    print("You already guessed that one.")
                    continue

                print("You missed!")
                self.user_board[user_guess_row][user_guess_col] = "X"
                self.print_board(self.user_board)
            except ValueError:
                print("Please enter a guess in the board range.")
                continue

            comp_guess_row = randint(0, self.size - 1)
            comp_guess_col = randint(0, self.size - 1)
            print("Computer guesses:", comp_guess_row, comp_guess_col)

            if comp_guess_row == self.ship_row and comp_guess_col == self.ship_col:
                print("Computer sunk your battleship!")
                return

            if self.computer_board[comp_guess_row][comp_guess_col] == "X":
                print("Computer already guessed that one.")
                continue

            print("Computer missed!")
            self.computer_board[comp_guess_row][comp_guess_col] = "X"
            self.print_board(self.computer_board)
            turn += 1

        print("Game Over.")


if __name__ == "__main__":
    """
    Allows user to choose game board size, number of turns, and play again.
    """
    while True:
        try:
            print("Rules: You choose turns and grid size.")
            print("User and computer will choose starting from 0,0.")
            print("Game ends when turns end or player/computer hits ship.")
            print("You can type 'quit' to end game/start a new game.")
            size = input("Enter the size of the game board: ").lower().strip()
            if size.lower() == "quit":
                print("Thank you for playing")
                exit()
            while not size.isdigit():
                print("Size must be a number.")
                size = input("Enter the size of the game board: ").strip()
                if size.lower() == "quit":
                    print("Thank you for playing")
                    exit()
            size = int(size)
            possible_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            while size not in possible_sizes:
                print("Size must be in the range from 1 to 12.")
                size = int(input("Enter the size of the game board: ").strip())
            num_turns = input("Enter the number of turns: ").lower().strip()
            if num_turns == "quit":
                print("Thank you for playing")
                exit()
            while not num_turns.isdigit():
                print("Number of turns must be a number.")
                num_turns = input("Enter the number of turns: ").strip()
                if num_turns.lower() == "quit":
                    print("Thank you for playing")
                    exit()
            num_turns = int(num_turns)
            if num_turns not in possible_sizes:
                raise ValueError(
                    "Number of turns must be in the range from 1 to 12.")
            game = BattleshipsGame(size=size, num_turns=num_turns)
            game.play()
        except ValueError as e:
            print("Error:", e)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
