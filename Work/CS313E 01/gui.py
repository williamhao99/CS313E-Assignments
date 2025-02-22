"""
The GUI and main function have been completed for you!
Do NOT change anything below this line
This file will not be checked for PEP8
"""

import tkinter as tk
import argparse
from traversals import (
    row_zigzag_traversal,
    column_zigzag_traversal,
    main_diagonal_traversal,
    secondary_diagonal_traversal,
    spiral_traversal,
)

traversal_functions = {
    "row_zigzag": row_zigzag_traversal,
    "column_zigzag": column_zigzag_traversal,
    "main": main_diagonal_traversal,
    "secondary": secondary_diagonal_traversal,
    "spiral": spiral_traversal,
}


class GridTraversalApp:
    """Graphical User Interface for the Traversals assignment"""

    def __init__(self, master, rows, cols, speed):
        self.master = master
        self.actual_grid = [[None for _ in range(cols)] for _ in range(rows)]
        rows, cols = rows + 2, cols + 2
        self.grid_cells = [[None for _ in range(cols)] for _ in range(rows)]
        self.speed = speed

        self.current_traversal = None

        self.after_id = None

        self.create_navigation_bar()

        # Creates the grid
        grid_frame = tk.Frame(self.master)
        grid_frame.grid(row=1, column=0, padx=10, pady=10)
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                    cell = tk.Canvas(
                        grid_frame, width=50, height=50, bg="grey", highlightthickness=1
                    )
                else:
                    cell = tk.Canvas(
                        grid_frame,
                        width=50,
                        height=50,
                        bg="white",
                        highlightthickness=1,
                    )
                cell.grid(row=i, column=j)
                self.grid_cells[i][j] = cell

        for i in range(rows):
            label = tk.Label(grid_frame, text=f"Row {i - 1}")
            label.grid(row=i, column=cols, padx=(5, 0))

        for j in range(cols):
            label = tk.Label(grid_frame, text=f"Col {j - 1}")
            label.grid(row=rows, column=j)

    def create_navigation_bar(self):
        """Creates the UI for the traversals"""
        navigation_frame = tk.Frame(self.master)
        navigation_frame.grid(row=0, column=0, columnspan=len(self.grid_cells[0]))

        texts = [
            "Row Zigzag",
            "Column Zigzag",
            "Main Diagonal",
            "Secondary Diagonal",
            "Spiral",
            "Exit",
        ]

        buttons = zip(texts, [*traversal_functions.values()] + [self.master.destroy])

        for i, (text, command) in enumerate(buttons):
            if text == texts[-1]:
                btn = tk.Button(navigation_frame, text=text, command=command)
            else:
                btn = tk.Button(
                    navigation_frame,
                    text=text,
                    command=lambda cmd=command: self.start_traversal(cmd),
                )
            btn.grid(row=0, column=i, padx=5, pady=5)

    def start_traversal(self, traversal_function):
        """Performs the requested traversal"""
        self.reset_grid()
        if self.after_id is not None:
            self.master.after_cancel(self.after_id)
        self.current_traversal = iter(traversal_function(self.actual_grid))
        self.update_grid()

    def update_grid(self):
        """Updates the grid based on the provided coordinates"""
        try:
            r, c = next(self.current_traversal)
            r += 1
            c += 1
            current_color = self.grid_cells[r][c].cget("bg")
            if current_color == "orange":
                self.grid_cells[r][c].configure(bg="black")
            else:
                self.grid_cells[r][c].configure(bg="orange")
            self.after_id = self.master.after(self.speed, self.update_grid)
        except StopIteration:
            pass

    def reset_grid(self):
        """Resets the grid back to white"""
        rows, cols = len(self.grid_cells), len(self.grid_cells[0])
        for i, row in enumerate(self.grid_cells):
            for j, cell in enumerate(row):
                if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                    cell.configure(bg="grey")
                else:
                    cell.configure(bg="white")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Matrix Argument Parser")

    parser.add_argument(
        "--rows",
        type=int,
        default=5,
        choices=range(1, 11),
        help="Number of rows in the matrix (between 1 and 10)",
    )
    parser.add_argument(
        "--columns",
        type=int,
        default=5,
        choices=range(1, 11),
        help="Number of columns in the matrix (between 1 and 10)",
    )
    parser.add_argument(
        "--speed",
        type=int,
        default=100,
        choices=range(50, 1001, 50),
        help="Speed of grid updates in milliseconds",
    )

    args = parser.parse_args()

    root = tk.Tk()
    app = GridTraversalApp(root, args.rows, args.columns, args.speed)
    root.mainloop()
