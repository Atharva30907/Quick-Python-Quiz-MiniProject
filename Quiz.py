import tkinter as tk
import random

questions = [
    ("Who created Python?", ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Linus Torvalds"], "Guido van Rossum"),
    ("Python is:", ["Low level language", "High level language", "Machine code", "Assembly language"], "High level language"),
    ("Which loop is not in Python?", ["for", "while", "do-while", "nested for"], "do-while"),
    ("What does an interpreter do?", ["Translates line by line", "Converts to binary", "Compiles once", "Debugs errors"], "Translates line by line"),
    ("Which data type is immutable?", ["List", "Set", "Tuple", "Dictionary"], "Tuple"),
    ("What symbol is used to define a function in Python?", ["function", "fun", "def", "define"], "def"),
    ("Which file mode creates a file?", ["r", "a", "x", "w"], "x"),
    ("Which data type stores key-value pairs?", ["List", "Set", "Tuple", "Dictionary"], "Dictionary"),
    ("Which module gives you access to OS-level commands?", ["math", "sys", "os", "random"], "os"),
    ("What is the correct way to start a for loop?", ["for i = 0 to 5:", "loop i in range(5):", "for i in range(5):", "repeat i to 5"], "for i in range(5):")
]

# Shuffle the questions for randomness
random.shuffle(questions)

# Initialize index and score
index = 0  # Current question index
score = 0  # Total correct answers

def start_quiz():
    # Hide the welcome screen and show quiz frame
    front_frame.pack_forget()
    quiz_frame.pack()
    load_question()  # Load the first question

def load_question():
    # Display current question and options
    q_number_text = f"Question {index + 1} of {len(questions)}:\n\n{questions[index][0]}"
    question_label.config(text=q_number_text)  # Set question text
    var.set(None)  # Reset radio button selection
    for i in range(4):
        # Update each radio button's text and value
        buttons[i].config(text=questions[index][1][i], value=questions[index][1][i])
    score_label.config(text=f"Score: {score}")  # Update score label

def next_question():
    # Go to next question or end quiz
    global index, score
    if var.get() == questions[index][2]:
        score += 1  # Increase score if answer is correct
    index += 1  # Move to next question
    if index < len(questions):
        load_question()  # Load next question
    else:
        # Quiz is over, show final result
        question_label.config(text=" Quiz Completed! ")
        result_label.config(text=f"You scored {score} out of {len(questions)} ")
        for btn in buttons:
            btn.pack_forget()  # Hide options
        next_btn.pack_forget()  # Hide next button
        score_label.pack_forget()  # Hide score label

window = tk.Tk()  # Create main window
window.title("Atharva's Python Quiz")  # Window title
window.geometry("550x600")  # Window size
window.config(bg="#1e1b2e")  # Background color

main_bg = "#1e1b2e"       # Background color
card_bg = "#2b2540"       # Inner card color
accent_green = "#00ffab"  # Selection and button highlight
accent_purple = "#c792ea" # Lavender color for theme
default_text = "#ffffff"   # White text color

front_frame = tk.Frame(window, bg=main_bg)  # Frame for front screen

# Quiz title label
tk.Label(front_frame, text="Atharva's Python Quiz", font=("Segoe UI", 22, "bold"),
         bg=main_bg, fg=accent_green, pady=30).pack()

# Subtitle
tk.Label(front_frame, text="Ready to test your Python skills?",
         font=("Segoe UI", 14), bg=main_bg, fg=default_text).pack(pady=10)

# Start quiz button
tk.Button(front_frame, text="Start Quiz", font=("Segoe UI", 14, "bold"),
          bg=accent_purple, fg="black", padx=25, pady=10,
          activebackground="#d1aaff", relief="flat", command=start_quiz).pack(pady=20)

front_frame.pack(expand=True)  # Show front frame

quiz_frame = tk.Frame(window, bg=main_bg)  # Frame for quiz questions

# Label to show question text
question_label = tk.Label(quiz_frame, text="", font=("Segoe UI", 15, "bold"),
                          bg=card_bg, fg=default_text, wraplength=480,
                          justify="left", padx=15, pady=20, bd=1, relief="solid")
question_label.pack(pady=25)

# Score display
score_label = tk.Label(quiz_frame, text="Score: 0", font=("Segoe UI", 12, "bold"),
                       fg=accent_green, bg=main_bg)
score_label.pack()

# Create radio button options
var = tk.StringVar()  # Variable to hold selected value
buttons = []  # List to hold radio buttons

# Create 4 options
for _ in range(4):
    rb = tk.Radiobutton(
        quiz_frame, text="", variable=var, value="",
        font=("Segoe UI", 12), bg=card_bg, fg=default_text,
        selectcolor=accent_green, anchor="w", width=40, padx=15,
        indicatoron=0, relief="raised", bd=2  # Flat styled buttons with selection
    )
    rb.pack(pady=5)
    buttons.append(rb)  # Add button to list

# Next button
next_btn = tk.Button(quiz_frame, text="Next", font=("Segoe UI", 13, "bold"),
                     bg=accent_green, fg="black", padx=20, pady=7,
                     activebackground="#00e6a4", relief="flat", command=next_question)
next_btn.pack(pady=20)

# Result label shown at the end
result_label = tk.Label(quiz_frame, text="", font=("Segoe UI", 13, "bold"),
                        fg=accent_purple, bg=main_bg)
result_label.pack(pady=10)

# Start the GUI loop
window.mainloop()
