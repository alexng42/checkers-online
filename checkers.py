"""
todo:
- forced jumps
- king
- game over

"""


class Checkers:
    def __init__(self):
        self.board = [
            ["#", "R4", "#", "R3", "#", "R2", "#", "R1"],
            ["R8", "#", "R7", "#", "R6", "#", "R5", "#"],
            ["#", "R12", "#", "R11", "#", "R10", "#", "R9"],
            ["_", "#", "_", "#", "_", "#", "_", "#"],
            ["#", "_", "#", "_", "#", "_", "#", "_"],
            ["B9", "#", "B10", "#", "B11", "#", "B12", "#"],
            ["#", "B5", "#", "B6", "#", "B7", "#", "B8"],
            ["B1", "#", "B2", "#", "B3", "#", "B4", "#"],
        ]

        self.playerBlack = "B"
        self.playerRed = "R"
        self.current_turn = "B"  # Black goes first

    def find_piece(self, piece):
        for r_idx, row in enumerate(self.board):
            for c_idx, cell in enumerate(row):
                if cell == piece:
                    return r_idx, c_idx
        return None

    def get_available_moves(self, piece_choice, select_row, select_col):
            valid_moves = []
            # check for forced jumps
            if piece_choice.startswith("B"):
                # left forced jump
                if self.board[select_row - 1][select_col - 1].startswith("R") and self.board[select_row - 2][select_col - 2] == "_":
                    valid_moves.append("JL")
                # right forced jump
                if self.board[select_row - 1][select_col + 1].startswith("R") and self.board[select_row - 2][select_col + 2] == "_":
                    valid_moves.append("JR")
                if not valid_moves:
                    # left
                    if self.board[select_row - 1][select_col - 1] == "_":
                        valid_moves.append("L")
                    # right
                    if self.board[select_row - 1][select_col + 1] == "_":
                        valid_moves.append("R")
                return valid_moves
            else:
                # left forced jump
                if self.board[select_row + 1][select_col - 1].startswith("B") and self.board[select_row + 2][select_col - 2] == "_":
                    valid_moves.append("JL")
                # right forced jump
                if self.board[select_row + 1][select_col + 1].startswith("B") and self.board[select_row + 2][select_col + 2] == "_":
                    valid_moves.append("JR")
                if not valid_moves:
                    # left
                    if self.board[select_row + 1][select_col - 1] == "_":
                        valid_moves.append("L")
                    # right
                    if self.board[select_row + 1][select_col + 1] == "_":
                        valid_moves.append("R")
                return valid_moves

    def process_input(self):
        print(f"{self.current_turn}'s Turn")

        while True:
            piece_choice = (
                input(f"{self.current_turn}: Type the piece you want to move: ")
                .strip()
                .upper()
            )

            if not piece_choice.startswith(self.current_turn):
                print(f"INVALID MOVE. Select a {self.current_turn} piece")
                continue

            coords = self.find_piece(piece_choice)
            if coords is None:
                print(f"{piece_choice} NOT FOUND. Select a different piece: ")
                continue

            select_row, select_col = coords

            print(f"Selected {piece_choice} at row {select_row}, col {select_col}")

            piece_moves = self.get_available_moves(piece_choice, select_row, select_col)

            direction = (
                input(f"Moving {piece_choice}. Choose an option: {piece_moves} ").strip().upper()
            )
            return piece_choice, select_row, select_col, direction, piece_moves
        

    def make_move(self, piece_choice, select_row, select_col, direction, piece_moves):
        if not piece_moves:
            print(f"{piece_choice} has no valid moves.")
            return
        if piece_choice.startswith("B"):
            if "JL" in piece_moves and direction == "JL":
                self.board[select_row][select_col] = "_"
                self.board[select_row - 1][select_col - 1] = "_"
                self.board[select_row - 2][select_col - 2] = piece_choice
            if "JR" in piece_moves and direction == "JR":
                self.board[select_row][select_col] = "_"
                self.board[select_row - 1][select_col + 1] = "_"
                self.board[select_row - 2][select_col + 2] = piece_choice

            if "L" in piece_moves and direction == "L":
                self.board[select_row][select_col] = "_"
                self.board[select_row - 1][select_col - 1] = piece_choice
            if "R" in piece_moves and direction == "R":
                self.board[select_row][select_col] = "_"
                self.board[select_row - 1][select_col + 1] = piece_choice
            self.current_turn = "R"
        else:
            if "JL" in piece_moves and direction == "JL":
                self.board[select_row][select_col] = "_"
                self.board[select_row + 1][select_col - 1] = "_"
                self.board[select_row + 2][select_col - 2] = piece_choice
            if "JR" in piece_moves and direction == "JR":
                self.board[select_row][select_col] = "_"
                self.board[select_row + 1][select_col + 1] = "_"
                self.board[select_row + 2][select_col + 2] = piece_choice
            if "L" in piece_moves and direction == "L":
                self.board[select_row][select_col] = "_"
                self.board[select_row + 1][select_col - 1] = piece_choice
            if "R" in piece_moves and direction == "R":
                self.board[select_row][select_col] = "_"
                self.board[select_row + 1][select_col + 1] = piece_choice
            self.current_turn = "B"

    def render(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def play(self):
        while True:
            self.render()
            piece_choice, select_row, select_col, direction, piece_moves = self.process_input()
            self.make_move(piece_choice, select_row, select_col, direction, piece_moves)
        print("GG")


test1 = Checkers()

test1.play()
