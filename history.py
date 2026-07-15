# history utilities for the calculator project
def save_history(history):
    file = open("history.txt", "w")

    for calculation in history: 
        file.write(calculation + "\n")

    file.close()
def load_history():
    file = open("history.txt", "r")
    
    data = file.read()
    history = data.split("\n")
    file.close()
    return history