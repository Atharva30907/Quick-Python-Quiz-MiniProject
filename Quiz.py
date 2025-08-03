import tkinter as tk
import random

# Quiz Questions
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
random.shuffle(questions)  # Randomize question order
index = 0  # Current question index
score = 0  # User score

# Functions
# Start the quiz (hide front page, show questions)
def start_quiz():
    front_frame.pack_forget()
    quiz_frame.pack()
    load_question()

# Load the current question and display options
def load_question():
    q_number_text = f" Question {index + 1} of {len(questions)}:\n\n{questions[index][0]}"
    question_label.config(text=q_number_text)
    var.set(None)  # Reset selected option
    for i in range(4):
        buttons[i].config(text=questions[index][1][i], value=questions[index][1][i])
    score_label.config(text=f"Score: {score}")

# Go to the next question and update score
def next_question():
    global index, score
    if var.get() == questions[index][2]:
        score += 1  # Correct answer
    index += 1
    if index < len(questions):
        load_question()
    else:
        # Quiz complete
        question_label.config(text=" 🎉 Quiz Completed! 🎉 ")
        result_label.config(text=f" You scored {score} out of {len(questions)}")
        for btn in buttons:
            btn.pack_forget()  # Hide buttons
        next_btn.pack_forget()
        score_label.pack_forget()

# Main Window Setup
window = tk.Tk()
window.title("Atharva's Python Quiz")
window.geometry("500x550")
window.configure(bg="#1e1e2f")  # Dark theme background

# Front Page Frame
front_frame = tk.Frame(window, bg="#1e1e2f")

# Quiz title
title_label = tk.Label(front_frame, text="Atharva's Python Quiz", font=("Segoe UI", 20, "bold"),
                       bg="#1e1e2f", fg="#00e5ff", pady=40)
title_label.pack()

# Description text
desc_label = tk.Label(front_frame, text="Test your Python skills",
                      font=("Segoe UI", 14), bg="#1e1e2f", fg="white", pady=20)
desc_label.pack()

# Start Quiz button
start_btn = tk.Button(front_frame, text="Start Quiz", font=("Segoe UI", 14, "bold"),
                      bg="#00e676", fg="black", padx=20, pady=10, command=start_quiz)
start_btn.pack()

# Show front page
front_frame.pack(expand=True)

# Quiz Frame (hidden until start)
quiz_frame = tk.Frame(window, bg="#1e1e2f")

# Question label
question_label = tk.Label(quiz_frame, text="", font=("Segoe UI", 16, "bold"),
                          bg="#ffffff", fg="#1e1e2f", wraplength=450, justify="center",
                          padx=20, pady=20, relief="groove", bd=2)
question_label.pack(pady=30)

# Score display
score_label = tk.Label(quiz_frame, text="Score: 0", font=("Segoe UI", 12, "bold"),
                       fg="#00e676", bg="#1e1e2f")
score_label.pack()

# Selected option variable
var = tk.StringVar()

# Option buttons (4 radio buttons)
buttons = [
    tk.Radiobutton(quiz_frame, text="", variable=var, value="", font=("Segoe UI", 12),
                   bg="#ffffff", fg="#1e1e2f", selectcolor="#bbdefb",
                   width=30, anchor="w", relief="ridge", padx=10)
    for _ in range(4)]

for btn in buttons:
    btn.pack(pady=5)

# Next button
next_btn = tk.Button(quiz_frame, text="Next", command=next_question,
                     font=("Segoe UI", 14, "bold"), bg="#2196f3", fg="white",
                     relief="flat", padx=20, pady=5)
next_btn.pack(pady=20)

# Final result display
result_label = tk.Label(quiz_frame, text="", font=("Segoe UI", 14, "bold"),
                        fg="#ffd600", bg="#1e1e2f")
result_label.pack(pady=10)

window.mainloop()

