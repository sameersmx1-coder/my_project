import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("500x650")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = [""] * 9

        self.x_score = 0
        self.o_score = 0
        self.draw_score = 0

        self.create_interface()

    def create_interface(self):
        title = tk.Label(
            self.root,
            text="TIC TAC TOE",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        self.turn_label = tk.Label(
            self.root,
            text="Player X's Turn",
            font=("Arial", 18, "bold")
        )
        self.turn_label.pack(pady=10)

        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=20)

        self.buttons = []

        for i in range(9):
            button = tk.Button(
                self.board_frame,
                text="",
                font=("Arial", 32, "bold"),
                width=5,
                height=2,
                command=lambda index=i: self.make_move(index)
            )

            button.grid(
                row=i // 3,
                column=i % 3,
                padx=5,
                pady=5
            )

            self.buttons.append(button)

        self.score_label = tk.Label(
            self.root,
            text="X: 0    O: 0    Draws: 0",
            font=("Arial", 16, "bold")
        )
        self.score_label.pack(pady=20)

        new_game_button = tk.Button(
            self.root,
            text="New Game",
            font=("Arial", 15, "bold"),
            command=self.new_game,
            padx=20,
            pady=10
        )
        new_game_button.pack()

    def make_move(self, index):
        if self.board[index] != "":
            return

        self.board[index] = self.current_player

        self.buttons[index].config(
            text=self.current_player
        )

        if self.check_winner():
            self.show_winner()
            return

        if "" not in self.board:
            self.draw_score += 1
            self.update_score()

            messagebox.showinfo(
                "Game Over",
                "The game is a draw!"
            )

            self.disable_buttons()
            return

        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

        self.turn_label.config(
            text="Player " + self.current_player + "'s Turn"
        )

    def check_winner(self):
        winning_patterns = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winning_patterns:
            if (
                self.board[a] != ""
                and self.board[a] == self.board[b]
                and self.board[b] == self.board[c]
            ):
                self.buttons[a].config(relief="sunken")
                self.buttons[b].config(relief="sunken")
                self.buttons[c].config(relief="sunken")
                return True

        return False

    def show_winner(self):
        winner = self.current_player

        if winner == "X":
            self.x_score += 1
        else:
            self.o_score += 1

        self.update_score()
        self.disable_buttons()

        messagebox.showinfo(
            "Game Over",
            "Player " + winner + " wins!"
        )

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def update_score(self):
        self.score_label.config(
            text=f"X: {self.x_score}    O: {self.o_score}    Draws: {self.draw_score}"
        )

    def new_game(self):
        self.board = [""] * 9
        self.current_player = "X"

        self.turn_label.config(
            text="Player X's Turn"
        )

        for button in self.buttons:
            button.config(
                text="",
                state="normal",
                relief="raised"
            )


root = tk.Tk()
game = TicTacToe(root)
root.mainloop()