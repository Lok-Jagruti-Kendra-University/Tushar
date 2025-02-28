
import tkinter as tk
import random


# List of possible colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'Purple', 'Brown', 'White']

score = 0
time_left = 60

def start_game(event):
    if time_left == 60:
        countdown()
    next_color()

def next_color():
    global score
    global time_left

    # Check if time is still left
    if time_left > 0:
        # Make the text entry box active
        e.focus_set()

        # If the typed color matches the displayed color's text
        if e.get().lower() == colors[1].lower():
            score += 1

        # Clear the entry box
        e.delete(0, tk.END)

        # Randomly choose colors
        random.shuffle(colors)

        # Display the color name in a different color
        label.config(fg=str(colors[1]), text=str(colors[0]))

        # Update the score
        score_label.config(text="Score: " + str(score))

def countdown():
    global time_left

    if time_left > 0:
        time_left -= 1

        time_label.config(text="Time left: " + str(time_left))

        # Call countdown function after 1 second
        time_label.after(1000, countdown)

# Create the window
root = tk.Tk()
root.title("Color Game")
root.geometry("400x300")

# Instructions label
instructions = tk.Label(root, text="Type the color of the text, not the word!", font=('Helvetica', 12))
instructions.pack()

# Time left label
time_label = tk.Label(root, text="Time left: " + str(time_left), font=('Helvetica', 12))
time_label.pack()

# Score label
score_label = tk.Label(root, text="Score: " + str(score), font=('Helvetica', 12))
score_label.pack()

# Display color text
label = tk.Label(root, font=('Helvetica', 60))
label.pack()

# Entry box for typing color
e = tk.Entry(root)
e.pack()

# Bind the enter key to start the game
root.bind('<Return>', start_game)

# Start the GUI loop
root.mainloop()
