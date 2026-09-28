import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.resizable(False, False)

# Function to update time
def update_time():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Clock label
clock_label = tk.Label(
    root,
    font=("Arial", 60, "bold"),
    bg="black",
    fg="white"
)
clock_label.pack(expand=True, fill="both")

# Start clock
update_time()

# Run the application
root.mainloop()