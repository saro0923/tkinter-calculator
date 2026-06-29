import tkinter as tk
# Functions
def click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# Main Window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Display Screen
display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10
)

display.pack(fill="both", padx=10, pady=10)

# Button Frame
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "C", "/", "*", "-",
    "7", "8", "9", "+",
    "4", "5", "6", "=",
    "1", "2", "3", ".",
    "0"
]

row = 0
col = 0

for button in buttons:

    if button == "=":
        btn = tk.Button(
            button_frame,
            text=button,
            font=("Arial", 18),
            width=5,
            height=2,
            command=calculate
        )

    elif button == "C":
        btn = tk.Button(
            button_frame,
            text=button,
            font=("Arial", 18),
            width=5,
            height=2,
            command=clear
        )

    else:
        btn = tk.Button(
            button_frame,
            text=button,
            font=("Arial", 18),
            width=5,
            height=2,
            command=lambda b=button: click(b)
        )

    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1

    if col > 3:
        col = 0
        row += 1

# Run Application
root.mainloop()