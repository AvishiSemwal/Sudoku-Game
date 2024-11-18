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

# Solve Sudoku using backtracking with MRV heuristic
def solve_sudoku(board):
    empty_cell = find_mrv_cell(board)
    if not empty_cell:  # No empty cells left; puzzle solved
        return True
    
    row, col = empty_cell
    for num in range(1, 10):  # Try numbers 1-9
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Undo move
    return False  # No valid number found for this cell

# Find the cell with the minimum remaining values (MRV)
def find_mrv_cell(board):
    min_options = 10  # More than the maximum options (1-9)
    best_cell = None
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                options = count_valid_numbers(board, row, col)
                if options < min_options:
                    min_options = options
                    best_cell = (row, col)
    return best_cell

# Count the number of valid numbers for a cell
def count_valid_numbers(board, row, col):
    valid_count = 0
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            valid_count += 1
    return valid_count

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
    root = tk.Tk()
    root.title("Sudoku Solver")

    buttons = [[None for _ in range(9)] for _ in range(9)]

    def refresh_grid():
        for i in range(9):
            for j in range(9):
                text = str(board[i][j]) if board[i][j] != 0 else "."
                buttons[i][j].config(text=text, state=tk.DISABLED if board[i][j] != 0 else tk.NORMAL)

    def solve_and_update():
        if solve_sudoku(board):
            refresh_grid()
            messagebox.showinfo("Success", "Sudoku solved!")
        else:
            messagebox.showerror("Error", "Sudoku puzzle cannot be solved.")

    for i in range(9):
        for j in range(9):
            button = tk.Button(root, text=".", width=4, height=2, font=("Arial", 14))
            button.grid(row=i, column=j, padx=2, pady=2)
            buttons[i][j] = button

    solve_button = tk.Button(root, text="Solve", command=solve_and_update, font=("Arial", 14), bg="green", fg="white")
    solve_button.grid(row=9, column=0, columnspan=9, pady=10)

    refresh_grid()
    root.mainloop()

# Main execution
if __name__ == "__main__":
    board = [row[:] for row in sudoku_puzzle]
    create_gui()
