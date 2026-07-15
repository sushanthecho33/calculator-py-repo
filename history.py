# history utilities for the calculator project
from typing import List

def save_history(history: List[str]) -> None:
    """Persist calculator history lines by appending them to history.txt.

    Args:
        history: list of history lines (strings) to append to the file.
    """
    if not history:
        return

    with open("history.txt", "a", encoding="utf-8") as f:
        for line in history:
            # ensure each entry is on its own line
            f.write(f"{line}\n")

def save_history(history):
    file = open("history.txt", "w")

    for calculation in history:
        file.write(calculation + "\n")

    file.close()