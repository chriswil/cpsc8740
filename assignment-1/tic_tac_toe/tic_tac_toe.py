# Tic-Tac-Toe Desktop Application
# CPSC 8740 - Assignment 1

import tkinter as tk
from tkinter import ttk, messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game")
        self.root.geometry("400x500")

        # Game state
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.scores = {"X": 0, "O": 0, "Tie": 0}

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title
        title_label = ttk.Label(main_frame, text="Tic-Tac-Toe", font=("Arial", 20, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # Current player display
        self.player_label = ttk.Label(main_frame, text=f"Current Player: {self.current_player}",
                                     font=("Arial", 14))
        self.player_label.grid(row=1, column=0, columnspan=3, pady=5)

        # Game board frame
        board_frame = ttk.Frame(main_frame)
        board_frame.grid(row=2, column=0, columnspan=3, pady=10)

        # Create game board buttons
        self.buttons = []
        for i in range(3):
            button_row = []
            for j in range(3):
                btn = tk.Button(board_frame, text="", font=("Arial", 24, "bold"),
                               width=4, height=2, bg="lightblue",
                               command=lambda r=i, c=j: self.make_move(r, c))
                btn.grid(row=i, column=j, padx=2, pady=2)
                button_row.append(btn)
            self.buttons.append(button_row)

        # Game status
        self.status_label = ttk.Label(main_frame, text="Game in progress...",
                                     font=("Arial", 12))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Control buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=4, column=0, columnspan=3, pady=10)

        ttk.Button(control_frame, text="New Game", command=self.new_game).grid(row=0, column=0, padx=5)
        ttk.Button(control_frame, text="Reset Scores", command=self.reset_scores).grid(row=0, column=1, padx=5)

        # Score display
        score_frame = ttk.LabelFrame(main_frame, text="Scores", padding="10")
        score_frame.grid(row=5, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

        self.score_label = ttk.Label(score_frame, text="", font=("Arial", 11))
        self.score_label.grid(row=0, column=0)

        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1)
        for i in range(3):
            main_frame.grid_columnconfigure(i, weight=1)
        score_frame.grid_columnconfigure(0, weight=1)

        self.update_score_display()

    def make_move(self, row, col):
        if not self.game_over and self.board[row][col] == "":
            # Make the move
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player,
                                         fg="red" if self.current_player == "X" else "blue",
                                         state="disabled")

            # Check for win or tie
            winner = self.check_winner()
            if winner:
                self.game_over = True
                if winner == "Tie":
                    self.status_label.config(text="It's a tie!")
                    self.scores["Tie"] += 1
                else:
                    self.status_label.config(text=f"Player {winner} wins!")
                    self.scores[winner] += 1

                self.disable_all_buttons()
                self.update_score_display()
                messagebox.showinfo("Game Over", self.status_label.cget("text"))
            else:
                # Switch players
                self.current_player = "O" if self.current_player == "X" else "X"
                self.player_label.config(text=f"Current Player: {self.current_player}")

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]

        # Check for tie
        if all(self.board[i][j] != "" for i in range(3) for j in range(3)):
            return "Tie"

        return None

    def disable_all_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

    def new_game(self):
        # Reset board
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_over = False

        # Reset buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal", bg="lightblue")

        # Update display
        self.player_label.config(text=f"Current Player: {self.current_player}")
        self.status_label.config(text="Game in progress...")

    def reset_scores(self):
        if messagebox.askyesno("Reset Scores", "Are you sure you want to reset all scores?"):
            self.scores = {"X": 0, "O": 0, "Tie": 0}
            self.update_score_display()

    def update_score_display(self):
        score_text = f"Player X: {self.scores['X']}  |  Player O: {self.scores['O']}  |  Ties: {self.scores['Tie']}"
        self.score_label.config(text=score_text)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()