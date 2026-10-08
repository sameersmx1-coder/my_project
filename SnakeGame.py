import tkinter as tk
import random

# Game settings
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
SPEED = 100

# Create window
root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

# Score
score = 0
direction = "Right"
game_over = False

score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 16, "bold")
)
score_label.pack()

# Game canvas
canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="black"
)
canvas.pack()

# Snake
snake = [
    [100, 100],
    [80, 100],
    [60, 100]
]

# Create food
food = [
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
]


def draw_game():
    canvas.delete("all")

    # Draw snake
    for i, segment in enumerate(snake):
        x, y = segment

        if i == 0:
            canvas.create_rectangle(
                x, y,
                x + CELL_SIZE,
                y + CELL_SIZE,
                fill="lime",
                outline="white"
            )
        else:
            canvas.create_rectangle(
                x, y,
                x + CELL_SIZE,
                y + CELL_SIZE,
                fill="green",
                outline="black"
            )

    # Draw food
    x, y = food
    canvas.create_oval(
        x, y,
        x + CELL_SIZE,
        y + CELL_SIZE,
        fill="red",
        outline="white"
    )


def change_direction(new_direction):
    global direction

    # Prevent the snake from moving directly backwards
    if new_direction == "Up" and direction != "Down":
        direction = "Up"

    elif new_direction == "Down" and direction != "Up":
        direction = "Down"

    elif new_direction == "Left" and direction != "Right":
        direction = "Left"

    elif new_direction == "Right" and direction != "Left":
        direction = "Right"


def move_snake():
    global score, game_over

    if game_over:
        return

    head_x, head_y = snake[0]

    if direction == "Up":
        head_y -= CELL_SIZE

    elif direction == "Down":
        head_y += CELL_SIZE

    elif direction == "Left":
        head_x -= CELL_SIZE

    elif direction == "Right":
        head_x += CELL_SIZE

    new_head = [head_x, head_y]

    # Wall collision
    if (
        head_x < 0 or
        head_x >= WIDTH or
        head_y < 0 or
        head_y >= HEIGHT
    ):
        end_game()
        return

    # Self collision
    if new_head in snake:
        end_game()
        return

    # Add new head
    snake.insert(0, new_head)

    # Food collision
    if new_head == food:
        score += 10
        score_label.config(text=f"Score: {score}")

        # Generate new food
        while True:
            food[0] = random.randrange(0, WIDTH, CELL_SIZE)
            food[1] = random.randrange(0, HEIGHT, CELL_SIZE)

            if food not in snake:
                break
    else:
        # Remove tail
        snake.pop()

    draw_game()

    root.after(SPEED, move_snake)


def end_game():
    global game_over

    game_over = True

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text="GAME OVER",
        fill="red",
        font=("Arial", 32, "bold")
    )

    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 + 45,
        text=f"Final Score: {score}",
        fill="white",
        font=("Arial", 18)
    )


def restart_game():
    global snake, food, score, direction, game_over

    snake = [
        [100, 100],
        [80, 100],
        [60, 100]
    ]

    food = [
        random.randrange(0, WIDTH, CELL_SIZE),
        random.randrange(0, HEIGHT, CELL_SIZE)
    ]

    score = 0
    direction = "Right"
    game_over = False

    score_label.config(text="Score: 0")

    draw_game()
    move_snake()


# Keyboard controls
root.bind("<Up>", lambda event: change_direction("Up"))
root.bind("<Down>", lambda event: change_direction("Down"))
root.bind("<Left>", lambda event: change_direction("Left"))
root.bind("<Right>", lambda event: change_direction("Right"))

# Restart button
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12, "bold"),
    command=restart_game
)
restart_button.pack(pady=8)

# Start game
draw_game()
move_snake()

root.mainloop()