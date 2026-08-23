"""
Game Logic:

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

            direction = (
                input(f"Move {piece_choice}: Left or Right? (L/R) ").strip().upper()
            )
            if direction == "L":
                print(f"Moving {piece_choice} {direction}")
                break
            if direction == "R":
                print(f"Moving {piece_choice} {direction}")
                break
            print("INVALID DIRECTION. Try again.")
            continue
        return piece_choice, select_row, select_col, direction

    def make_move(self, piece_choice, select_row, select_col, direction):
        if piece_choice.startswith("B"):
            if direction == "L":
                if select_row - 1 < 0 or select_col - 1 < 0:
                    print("INVALID MOVE. Try again")
                    return
                if self.board[select_row - 1][select_col - 1] != "_":
                    print("INVALID MOVE. Try again")
                    return
                else:
                    self.board[select_row][select_col] = "_"
                    self.board[select_row - 1][select_col - 1] = piece_choice
            if direction == "R":
                if select_col + 1 > 7 or select_row - 1 < 0:
                    print("INVALID MOVE. Try again")
                    return
                if self.board[select_row - 1][select_col + 1] != "_":
                    print("INVALID MOVE. Try again")
                    return
                else:
                    self.board[select_row][select_col] = "_"
                    self.board[select_row - 1][select_col + 1] = piece_choice
            self.current_turn = "R"
        else:
            if direction == "L":
                if select_row + 1 < 0 or select_col - 1 < 0:
                    print("INVALID MOVE. Try again")
                    return
                if self.board[select_row + 1][select_col - 1] != "_":
                    print("INVALID MOVE. Try again")
                    return
                else:
                    self.board[select_row][select_col] = "_"
                    self.board[select_row + 1][select_col - 1] = piece_choice
            if direction == "R":
                if select_col + 1 > 7 or select_row + 1 < 0:
                    print("INVALID MOVE. Try again")
                    return
                if self.board[select_row + 1][select_col + 1] != "_":
                    print("INVALID MOVE. Try again")
                    return
                else:
                    self.board[select_row][select_col] = "_"
                    self.board[select_row + 1][select_col + 1] = piece_choice
            self.current_turn = "B"

    def render(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def play(self):
        while True:
            self.render()
            piece_choice, select_row, select_col, direction = self.process_input()
            self.make_move(piece_choice, select_row, select_col, direction)
        print("GG")


test1 = Checkers()

test1.play()
