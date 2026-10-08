import tkinter as tk
from tkinter import messagebox

ROWS = 6
COLS = 7

board = [[0 for _ in range(COLS)] for _ in range(ROWS)]

current_player = 1

root = tk.Tk()
root.title("Connect Four")
root.resizable(False, False)

buttons = []


def drop_piece(col):
    global current_player

    # Find the empty row from bottom
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = current_player

            if current_player == 1:
                buttons[row][col].config(
                    text="●",
                    fg="red"
                )
            else:
                buttons[row][col].config(
                    text="●",
                    fg="yellow"
                )

            if check_winner(row, col):
                player = "Player 1 (Red)" if current_player == 1 else "Player 2 (Yellow)"
                messagebox.showinfo("Game Over", player + " wins!")
                disable_buttons()
                return

            if check_draw():
                messagebox.showinfo("Game Over", "It's a Draw!")
                return

            # Change player
            current_player = 2 if current_player == 1 else 1

            if current_player == 1:
                status_label.config(text="Player 1's Turn - Red")
            else:
                status_label.config(text="Player 2's Turn - Yellow")

            return

    messagebox.showwarning("Invalid Move", "Column is full!")


def check_winner(row, col):
    player = board[row][col]

    directions = [
        (0, 1),   # Horizontal
        (1, 0),   # Vertical
        (1, 1),   # Diagonal
        (1, -1)   # Other diagonal
    ]

    for dr, dc in directions:
        count = 1

        # Check one direction
        r = row + dr
        c = col + dc

        while 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player:
                count += 1
                r += dr
                c += dc
            else:
                break

        # Check opposite direction
        r = row - dr
        c = col - dc

        while 0 <= r < ROWS and 0 <= c < COLS:
            if board[r][c] == player:
                count += 1
                r -= dr
                c -= dc
            else:
                break

        if count >= 4:
            return True

    return False


def check_draw():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                return False

    return True


def disable_buttons():
    for row in range(ROWS):
        for col in range(COLS):
            buttons[row][col].config(state="disabled")


def restart_game():
    global board, current_player

    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    current_player = 1

    for row in range(ROWS):
        for col in range(COLS):
            buttons[row][col].config(
                text="○",
                fg="black",
                state="normal"
            )

    status_label.config(text="Player 1's Turn - Red")


# Title
title_label = tk.Label(
    root,
    text="CONNECT FOUR",
    font=("Arial", 20, "bold")
)
title_label.grid(row=0, column=0, columnspan=COLS, pady=10)


# Status
status_label = tk.Label(
    root,
    text="Player 1's Turn - Red",
    font=("Arial", 14, "bold")
)
status_label.grid(row=1, column=0, columnspan=COLS, pady=5)


# Column buttons
for col in range(COLS):
    button = tk.Button(
        root,
        text="↓",
        font=("Arial", 14, "bold"),
        width=5,
        command=lambda c=col: drop_piece(c)
    )
    button.grid(row=2, column=col, padx=2, pady=2)


# Game board
for row in range(ROWS):
    button_row = []

    for col in range(COLS):
        button = tk.Button(
            root,
            text="○",
            font=("Arial", 24, "bold"),
            width=3,
            height=1,
            command=lambda c=col: drop_piece(c)
        )

        button.grid(
            row=row + 3,
            column=col,
            padx=2,
            pady=2
        )

        button_row.append(button)

    buttons.append(button_row)


# Restart button
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12, "bold"),
    command=restart_game
)
restart_button.grid(
    row=ROWS + 3,
    column=0,
    columnspan=COLS,
    pady=10
)


root.mainloop()

