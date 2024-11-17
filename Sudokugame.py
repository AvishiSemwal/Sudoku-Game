import tkinter as tk
from tkinter import messagebox, simpledialog

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

# Global variable to keep track of the Sudoku board
board = [row[:] for row in sudoku_puzzle]

# Check if a number can be placed in a position
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

# Check if the Sudoku puzzle is solved
def is_solved(board):
    return all(all(cell != 0 for cell in row) for row in board)

# Update the board and check if the user has solved the puzzle
def update_board(row, col, num):
    if board[row][col] == 0 and is_valid(board, row, col, num):
        board[row][col] = num
        if is_solved(board):
            messagebox.showinfo("Congratulations!", "You solved the Sudoku!")
    else:
        messagebox.showwarning("Invalid Move", "That move is invalid. Please try again.")

# GUI setup using tkinter
def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Sudoku Game")

    # Create a 9x9 grid of buttons
    buttons = [[None for _ in range(9)] for _ in range(9)]

    def on_button_click(row, col):
        # Prompt for the number to place
        num = simpledialog.askinteger("Input", f"Enter a number (1-9) for row {row+1}, column {col+1}:")
        if num is not None and 1 <= num <= 9:
            update_board(row, col, num)
            refresh_grid()

    # Create a function to refresh the grid and update button labels
    def refresh_grid():
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    buttons[i][j].config(text=str(board[i][j]), state=tk.DISABLED)
                else:
                    buttons[i][j].config(text=".", state=tk.NORMAL)

    # Create buttons for the grid
    for i in range(9):
        for j in range(9):
            button = tk.Button(root, text=".", width=4, height=2, command=lambda i=i, j=j: on_button_click(i, j))
            button.grid(row=i, column=j, padx=5, pady=5)
            buttons[i][j] = button

    # Function to confirm if the user wants to exit the game
    def on_exit():
        result = messagebox.askyesno("Exit", "Are you sure you want to exit the game?")
        if result:
            root.quit()

    # Create an Exit button at the bottom of the window
    exit_button = tk.Button(root, text="Exit", command=on_exit, width=10, height=2)
    exit_button.grid(row=9, column=0, columnspan=9, pady=10)

    # Refresh the grid initially
    refresh_grid()

    # Start the Tkinter main loop
    root.mainloop()
    

# Run the game
create_gui()
#Code Ends
