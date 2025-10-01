# Basic Calculator Desktop Application
# CPSC 8740 - Assignment 1

import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")
        self.root.geometry("300x400")

        # Current calculation
        self.current = "0"
        self.total = 0
        self.operation = None
        self.new_number = True

        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display = tk.Entry(
            self.root, font=("Arial", 16), justify="right", state="readonly"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

        # Button layout
        buttons = [
            ("C", 1, 0),
            ("±", 1, 1),
            ("%", 1, 2),
            ("÷", 1, 3),
            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
            ("×", 2, 3),
            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),
            ("-", 3, 3),
            ("1", 4, 0),
            ("2", 4, 1),
            ("3", 4, 2),
            ("+", 4, 3),
            ("0", 5, 0),
            (".", 5, 2),
            ("=", 5, 3),
        ]

        for text, row, col in buttons:
            if text == "0":
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=("Arial", 14),
                    command=lambda t=text: self.button_click(t),
                )
                btn.grid(row=row, column=col, columnspan=2, padx=2, pady=2, sticky="ew")
            else:
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=("Arial", 14),
                    command=lambda t=text: self.button_click(t),
                )
                btn.grid(row=row, column=col, padx=2, pady=2, sticky="ew")

        # Configure grid weights
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)

        self.update_display()

    def button_click(self, char):
        if char.isdigit():
            self.number_click(char)
        elif char == ".":
            self.decimal_click()
        elif char in "+-×÷":
            self.operation_click(char)
        elif char == "=":
            self.equals_click()
        elif char == "C":
            self.clear_click()
        elif char == "±":
            self.sign_click()
        elif char == "%":
            self.percent_click()

    def number_click(self, number):
        if self.new_number:
            self.current = number
            self.new_number = False
        else:
            if self.current == "0":
                self.current = number
            else:
                self.current += number
        self.update_display()

    def decimal_click(self):
        if self.new_number:
            self.current = "0."
            self.new_number = False
        elif "." not in self.current:
            self.current += "."
        self.update_display()

    def operation_click(self, op):
        if not self.new_number:
            self.equals_click()

        self.operation = op
        self.total = float(self.current)
        self.new_number = True

    def equals_click(self):
        if self.operation and not self.new_number:
            current_num = float(self.current)

            if self.operation == "+":
                self.total += current_num
            elif self.operation == "-":
                self.total -= current_num
            elif self.operation == "×":
                self.total *= current_num
            elif self.operation == "÷":
                if current_num != 0:
                    self.total /= current_num
                else:
                    self.current = "Error"
                    self.update_display()
                    return

            self.current = str(self.total)
            self.operation = None
            self.new_number = True

        self.update_display()

    def clear_click(self):
        self.current = "0"
        self.total = 0
        self.operation = None
        self.new_number = True
        self.update_display()

    def sign_click(self):
        if self.current != "0":
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
        self.update_display()

    def percent_click(self):
        self.current = str(float(self.current) / 100)
        self.update_display()

    def update_display(self):
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current)
        self.display.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
