import tkinter as tk
import random

# List of words for the Hangman game
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Initialize variables
word_to_guess = random.choice(word_list)
guessed_letters = []
attempts_left = 6

# Function to update the display of the word with underscores for unguessed letters
def update_display():
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    word_label.config(text=display_word)

# Function to handle a guessed letter
def guess_letter():
    global attempts_left
    letter = letter_entry.get().lower()
    if len(letter) == 1 and letter.isalpha():
        if letter not in guessed_letters:
            guessed_letters.append(letter)
            if letter not in word_to_guess:
                attempts_left -= 1
                update_hangman_image()
            update_display()
            letter_entry.delete(0, tk.END)
            check_win()
        else:
            status_label.config(text="You already guessed that letter.")
    else:
        status_label.config(text="Please enter a valid single letter.")

# Function to update the hangman image
def update_hangman_image():
    hangman_canvas.delete("all")
    parts = 6 - attempts_left
    if parts >= 1:
        hangman_canvas.create_line(20, 190, 70, 190)
    if parts >= 2:
        hangman_canvas.create_line(45, 190, 45, 20)
    if parts >= 3:
        hangman_canvas.create_line(45, 20, 95, 20)
    if parts >= 4:
        hangman_canvas.create_line(95, 20, 95, 40)
    if parts >= 5:
        hangman_canvas.create_oval(85, 40, 105, 60)
    if parts >= 6:
        hangman_canvas.create_line(95, 60, 95, 120)

# Function to check if the player has won or lost
def check_win():
    if "_" not in word_label.cget("text"):
        status_label.config(text="Congratulations! You've won!")
    elif attempts_left == 0:
        status_label.config(text=f"Game over! The word was '{word_to_guess}'.")
    else:
        status_label.config(text=f"Attempts left: {attempts_left}")

# Create a tkinter window
window = tk.Tk()
window.title("devCharis Hangman Game")

# Create widgets
hangman_canvas = tk.Canvas(window, width=200, height=200)
word_label = tk.Label(window, text="", font=("Arial", 24))
letter_label = tk.Label(window, text="Enter a letter:")
letter_entry = tk.Entry(window, width=5)
guess_button = tk.Button(window, text="Guess", command=guess_letter)
status_label = tk.Label(window, text="")

# Place widgets on the grid
hangman_canvas.grid(row=0, column=0, columnspan=4)
word_label.grid(row=1, column=0, columnspan=4)
letter_label.grid(row=2, column=0, columnspan=2)
letter_entry.grid(row=2, column=2)
guess_button.grid(row=2, column=3)
status_label.grid(row=3, column=0, columnspan=4)

# Initialize the display
update_display()
update_hangman_image()

# Start the tkinter main loop
window.mainloop()
