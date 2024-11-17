import tkinter as tk
from tkinter import messagebox

# Sample Sudoku puzzle with 0 representing empty cells
sudoku_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve Sudoku using backtracking
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Undo move
                return False  # No valid number found
    return True  # Solved

# Check if placing a number is valid
def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

# GUI setup
def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Sudoku Solver")

    # Create a 9x9 grid of buttons
    buttons = [[None for _ in range(9)] for _ in range(9)]

    def refresh_grid():
        """Update the GUI to reflect the board state."""
        for i in range(9):
            for j in range(9):
                text = str(board[i][j]) if board[i][j] != 0 else "."
                buttons[i][j].config(text=text, state=tk.DISABLED if board[i][j] != 0 else tk.NORMAL)

    def solve_and_update():
        """Solve the puzzle and update the GUI."""
        if solve_sudoku(board):
            refresh_grid()
            messagebox.showinfo("Success", "Sudoku solved!")
        else:
            messagebox.showerror("Error", "Sudoku puzzle cannot be solved.")

    # Initialize the buttons
    for i in range(9):
        for j in range(9):
            button = tk.Button(root, text=".", width=4, height=2, font=("Arial", 14))
            button.grid(row=i, column=j, padx=2, pady=2)
            buttons[i][j] = button

    # Add Solve button
    solve_button = tk.Button(root, text="Solve", command=solve_and_update, font=("Arial", 14), bg="green", fg="white")
    solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    # Refresh the grid initially
    refresh_grid()

    # Start the Tkinter main loop
    root.mainloop()

# Main execution
if __name__ == "__main__":
    # Initialize board from the sample puzzle
    board = [row[:] for row in sudoku_puzzle]
    create_gui()
#code ends
