# history utilities for the calculator project
def save_history(history): #type: ignore
    file = open("history.txt", "w")

    for calculation in history: #type: ignore
        file.write(calculation + "\n") #type: ignore

    file.close()
def load_history():
    file = open("history.txt", "r")
    
    data = file.read()
    history = data.split("\n")
    file.close()
    return history