from random import randint


class BattleshipsGame:
    def __init__(self, size=5, num_turns=4, num_ships=3):
        """
        Start the battleship game with a given size,
        number of turns, and number of ships.
        """
        self.size = size
        self.num_turns = num_turns
        self.num_ships = num_ships
        self.user_board = [['O'] * size for _ in range(size)]
        self.computer_board = [['O'] * size for _ in range(size)]
        self.user_ships = self.place_ships()
        self.computer_ships = self.place_ships()

    def place_ships(self):
        """
        Place ships randomly on the game board.
        """
        ships = []
        for _ in range(self.num_ships):
            ship_row = randint(0, self.size - 1)
            ship_col = randint(0, self.size - 1)
            while (ship_row, ship_col) in ships:
                ship_row = randint(0, self.size - 1)
                ship_col = randint(0, self.size - 1)
            ships.append((ship_row, ship_col))
        return ships

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

            user_guess_input = input(
                "Enter your guess (row, col) with a comma, or type 'quit': "
            )
            if user_guess_input.lower() == 'quit':
                print("Quitting game.")
                return

            try:
                user_guess_row, user_guess_col = map(
                    int, user_guess_input.split(','))
                if not self.validate_guess(user_guess_row, user_guess_col):
                    print("Please enter a guess within the board range.\n")
                    continue

                if (user_guess_row, user_guess_col) in self.computer_ships:
                    print("You hit a ship!")
                    self.user_board[user_guess_row][user_guess_col] = "X"
                    self.computer_ships.remove(
                        (user_guess_row, user_guess_col))
                    if not self.computer_ships:
                        print("You sunk all computer ships! You win!")
                        return
                elif (self.user_board[user_guess_row][user_guess_col] == "X" or
                      self.user_board[user_guess_row][user_guess_col] == "M"):
                    print("You already hit a ship here. Please choose again.")
                    continue
                else:
                    print("You missed!")
                    self.user_board[user_guess_row][user_guess_col] = "M"

                self.print_board(self.user_board)
            except ValueError:
                print("Please enter a guess in the board range.")
                continue

            comp_guess_row = randint(0, self.size - 1)
            comp_guess_col = randint(0, self.size - 1)
            print("Computer guesses:", comp_guess_row, comp_guess_col)

            if (comp_guess_row, comp_guess_col) in self.user_ships:
                print("Computer hit your ship!")
                self.computer_board[comp_guess_row][comp_guess_col] = "X"
                self.user_ships.remove((comp_guess_row, comp_guess_col))
                if not self.user_ships:
                    print("All your ships sunk! Computer wins!")
                    return
            elif (self.computer_board[comp_guess_row][comp_guess_col] == "X" or
                  self.computer_board[comp_guess_row][comp_guess_col] == "M"):
                print("Computer already hit a ship here. "
                      "Computer chooses again.")
                continue
            else:
                print("Computer missed!")
                self.computer_board[comp_guess_row][comp_guess_col] = "M"

            self.print_board(self.computer_board)
            turn += 1

        print("Game Over.")


if __name__ == "__main__":
    """
    Allows user to choose game board size, number of turns,
    quit and play again. Also choose number of ships.
    """
    while True:
        print("Rules: You choose turns, grid size and ships.")
        print("Grid = 1-12 , turns = 1-12 , ships = 1-3")
        print("User and computer will choose starting from 1,1.")
        print("Game ends when turns end "
              "or player/computer hits all chosen ships.")
        print("You can type 'quit' to end game/start a new game.")
        size = input("Enter the size of the game board: ").lower().strip()
        if size == "quit":
            print("Thank you for playing")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
            continue
        try:
            size = int(size)
            if size not in range(1, 13):
                print("Size must be in the range from 1 to 12.")
                continue
        except ValueError:
            print("Input must be a valid integer.")
            continue

        num_turns = input("Enter the turns "
                          "of the game board: ").lower().strip()
        if num_turns == "quit":
            print("Thank you for playing")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
            continue
        try:
            num_turns = int(num_turns)
            if num_turns not in range(1, 13):
                print("Turns must be in the range from 1 to 12.")
                continue
        except ValueError:
            print("Input must be a valid integer.")
            continue

        num_ships = input("Enter the ships "
                          "of the game board: ").lower().strip()
        if num_ships == "quit":
            print("Thank you for playing")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
            continue
        try:
            num_ships = int(num_ships)
            if num_ships not in range(1, 4):
                print("Ships must be in the range from 1 to 3.")
                continue
        except ValueError:
            print("Input must be a valid integer.")
            continue

        game = BattleshipsGame(
            size=size, num_turns=num_turns, num_ships=num_ships)
        game.play()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing")
            break
