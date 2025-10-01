# Basic Calculator Desktop Application
# CPSC 8740 - Assignment 1

import tkinter as tk


class Calculator:
    def __init__(self, root):
        """
        Initialize the Calculator UI and its internal state.
        
        Sets the window title and size, initializes display and computation state variables
        (`current`, `total`, `operation`, `new_number`), and constructs the widget layout by
        calling create_widgets().
        
        Parameters:
            root (tk.Tk): The main Tkinter window used as the parent for the calculator UI.
        """
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
        """
        Create and arrange the calculator's display and buttons, wire button events, and configure the window grid.
        
        This initializes the read-only numeric display, creates calculator buttons laid out in a 4x6 grid (with the "0" button spanning two columns), binds each button to the instance's button_click handler, sets column and row weights for responsive resizing, and updates the display to reflect the initial state.
        """
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
        """
        Route a calculator button press to the appropriate action handler.
        
        Parameters:
            char (str): The label of the pressed button. Expected values:
                - digits '0'–'9' to input or append a digit
                - '.' to insert a decimal point
                - '+', '-', '×', '÷' to set a binary operation
                - '=' to evaluate the current operation
                - 'C' to clear the calculator state
                - '±' to toggle the sign of the current value
                - '%' to convert the current value to a percentage
        """
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
        """
        Handle a digit button press by updating the current input value.
        
        Parameters:
            number (str): The digit character to enter (e.g., "0"–"9"). If a new number is being started, this sets the display to `number`; otherwise it appends `number` to the existing input, replacing a lone "0".
        """
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
        """
        Begin or append a decimal point to the current numeric entry and refresh the display.
        
        If starting a new number, initializes the entry to "0." and marks input as ongoing; otherwise, appends a decimal point only if the current entry does not already contain one. Updates the calculator display to reflect the change.
        """
        if self.new_number:
            self.current = "0."
            self.new_number = False
        elif "." not in self.current:
            self.current += "."
        self.update_display()

    def operation_click(self, op):
        """
        Set the pending arithmetic operation and prepare the calculator to receive the next operand.
        
        If a number entry was just completed, apply any previously pending operation first. Store the current display value as the running total, record the new operation symbol, and mark that the next digit input should start a new number.
        
        Parameters:
            op (str): Arithmetic operator to apply for the next calculation ("+", "-", "×", or "÷").
        """
        if not self.new_number:
            self.equals_click()

        self.operation = op
        self.total = float(self.current)
        self.new_number = True

    def equals_click(self):
        """
        Apply the pending arithmetic operation between the stored total and the current display value and update the calculator state.
        
        If an operation is pending and a new number has been entered, performs that operation using the stored total and the current input. On division by zero sets the display to "Error" and aborts applying the result. After a successful computation, updates the display value to the result, clears the pending operation, and marks the next input as a new number. Always refreshes the display.
        """
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
        """
        Toggle the sign of the current display value and refresh the display.
        
        If the current value is "0", no change is made; otherwise the sign is flipped between positive and negative. The display is updated to reflect the new value.
        """
        if self.current != "0":
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
        self.update_display()

    def percent_click(self):
        """
        Convert the current displayed number to its percentage value and refresh the display.
        
        Divides the current value by 100 and updates the calculator display to reflect the new value.
        """
        self.current = str(float(self.current) / 100)
        self.update_display()

    def update_display(self):
        """
        Update the calculator's display widget to show the current value.
        
        This replaces the display contents with the value of `self.current` and restores the display to read-only.
        """
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current)
        self.display.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
