import tkinter as tk
import random



questions = [
    (" Who created Python?", ["Guido van Rossum", "Dennis Ritchie", "James Gosling", "Linus Torvalds"], "Guido van Rossum"),
    (" Python is:", ["Low level launguage", "High level launguage", "Machine code", "Assembly launguage"], "High level launguage"),
    (" Which loop is not in Python?", ["for", "while", "do-while", "nested for"], "do-while"),
    (" What does an interpreter do?", ["Translates line by line", "Converts to binary", "Compiles once", "Debugs errors"], "Translates line by line"),
    (" Which data type is *immutable*?", ["List", "Set", "Tuple", "Dictionary"], "Tuple"),
    (" What symbol is used to define a function in Python?", ["function", "fun", "def", "define"], "def"),
    (" Which file mode creates a file?", ["r", "a", "x", "w"], "x"),
    (" Which data type stores key-value pairs?", ["List", "Set", "Tuple", "Dictionary"], "Dictionary"),
    (" Which module gives you access to OS-level commands?", ["math", "sys", "os", "random"], "os"),
    (" What is the correct way to start a for loop?", ["for i = 0 to 5:", "loop i in range(5):", "for i in range(5):", "repeat i to 5"], "for i in range(5):")
]


index = 0
score = 0

random.shuffle(questions[index][1])

def load_question():
    question_label.config(text=questions[index][0])
    var.set(None)
    for i in range(4):
        buttons[i].config(text=questions[index][1][i], value=questions[index][1][i])
    score_label.config(text=f"Score: {score}")
    
def next_question():
    global index, score
    if var.get() == "":
        messagebox.showinfo("Wait!", "Please choose an option.")
        return
    if var.get() == questions[index][2]:
        score += 1
    index += 1
    if index < len(questions):
        load_question()
    else:
        question_label.config(text=f"🎉 Quiz Over!\nCongratulations! You scored {score} out of {len(questions)}.")
        for b in buttons:
            b.pack_forget()
            score_label.pack_forget()
            next_btn.config(text="Close", command=window.destroy)
 
window = tk.Tk()
window.title("Quick Python Quiz")
window.geometry("400x400")

question_label = tk.Label(window, text="", font=("Arial", 14), wraplength=380)
question_label.pack(pady=20)

score_label = tk.Label(window, text="Score: 0", font=("Arial", 12), fg="green")
score_label.pack()

var = tk.StringVar()
buttons = [tk.Radiobutton(window, text="", variable=var, value="", font=("Arial", 12)) for _ in range(4)]
for b in buttons:
    b.pack(anchor='w', padx=50)

next_btn = tk.Button(window, text="Next", command=next_question,font = ("Arial",15,"bold"), bg="blue", fg="white")
next_btn.pack(pady=20)

load_question()
window.mainloop()
