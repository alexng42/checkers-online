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
            return piece_choice, select_row, select_col

    def render(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def play(self):
        while True:
            self.render()
            self.process_input()
        print("GG")


test1 = Checkers()

test1.play()
