import random
import tkinter as tk

# Define function to generate a random number and display it
def generate_number():
    number = random.randint(1, 99)  # Generate a random integer between 1 and 100
    label.config(text=f"Random number is: {number}")  # Update label text with the random number

# Create a tkinter window and widgets
window = tk.Tk()
window.title("Random Number Lottery")

label = tk.Label(window, text="Click the button to generate a random number lottery.")
label.pack()

button = tk.Button(window, text="Generate number", command=generate_number)
button.pack()

# Center the tkinter window both horizontally and vertically on the screen
window_width = 400
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
