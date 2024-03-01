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
                    self.computer_ships.remove((user_guess_row, user_guess_col))
                    if not self.computer_ships:
                        print("You sunk all computer ships! You win!")
                        return
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
            else:
                print("Computer missed!")
                self.computer_board[comp_guess_row][comp_guess_col] = "M"

            self.print_board(self.computer_board)
            turn += 1

        print("Game Over.")


if __name__ == "__main__":
    """
    Allows user to choose game board size, number of turns,
    quit and play again. Also 
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
                    "Number of turns must be in the range from 1 to 12."
                )
            num_ships = input("Enter the number of ships: ").lower().strip()
            if num_ships == "quit":
                print("Thank you for playing")
                exit()
            possible_ships = [1, 2, 3]
            while not num_ships.isdigit():
                print("Number of ships must be a number.")
                num_ships = input("Enter the number of ships: ").strip()
                if num_ships.lower() == "quit":
                    print("Thank you for playing")
                    exit()
            num_ships = int(num_ships)
            if num_ships not in possible_ships:
                raise ValueError(
                        "Number of ships must be in the range from 1 to 3."
                )
            game = BattleshipsGame(size=size, num_turns=num_turns, num_ships=num_ships)
            game.play()
        except ValueError as e:
            print("Error:", e)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
