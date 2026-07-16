import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Calculator")
window.geometry("360x440")
window.resizable(False, False)

entry = tk.Entry(window, font=("Segoe UI", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('C',4,0),('0',4,1),('=',4,2),('+',4,3)
]

for (text, row, col) in buttons:
    if text == "C":
        command = clear
    elif text == "=":
        command = calculate
    else:
        command = lambda t=text: click(t)

    button = tk.Button(
        window,
        text=text,
        font=("Segoe UI", 18),
        command=command,
        width=5,
        height=2
    )
    button.grid(row=row, column=col, padx=5, pady=5)

window.mainloop()
