
import tkinter as tk
import random
def check_guess():
  """Checks the user's guess against the random number."""
  try:
    guess = int(entry.get())
    if guess < number:
      result_label.config(text="Too low! Try again.")
    elif guess > number:
      result_label.config(text="Too high! Try again.")
    else:
      result_label.config(text=f"Congratulations! You guessed it in {guesses_left} tries!")
      convert_button.config(state=tk.DISABLED)  # Disable button after winning

    guesses_left -= 1
    guesses_label.config(text=f"Guesses left: {guesses_left}")

    if guesses_left == 0:
      result_label.config(text=f"You ran out of guesses! The number was {number}.")
      convert_button.config(state=tk.DISABLED)  # Disable button after losing

  except ValueError:
    result_label.config(text="Invalid input. Please enter a number.")

# Create main window
window = tk.Tk()
window.title("Guess the Number")

# Generate random number
number = random.randint(1, 100)
guesses_left = 7

# Input label and entry
input_label = tk.Label(window, text="Enter your guess:")
input_label.grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(window)
entry.grid(row=0, column=1, padx=5, pady=5)

# Convert button
convert_button = tk.Button(window, text="Check Guess", command=check_guess)
convert_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Result label
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Guesses label
guesses_label = tk.Label(window, text=f"Guesses left: {guesses_left}")
guesses_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()