# Calculator App
from tkinter import Tk, Button, mainloop
from functools import partial
from calculator import Calculator

class Renderer():
    def __init__(self):
        self.calculator = Calculator()

    def render(self):
        root = Tk()
        root.configure(bg="#1D1D1D")
        # Output Box
        # outputBox = Entry(bg="#555555")
        # outputBox.grid(row=0, column=0)

        # Create number buttons
        button_0 = Button(root, text="0", bg="#2D2D2D", fg="#EEEEEE", width=3, pady=5)
        button_0.config(command=partial(self.calculator.append_expression, button_0.cget("text")))
        button_0.grid(row=4, column=0)

        currentRow = 3
        currentCol = 0

        for i in range (1, 10):
            current_button = Button(root, text=str(i), bg="#2D2D2D", fg="#EEEEEE", width=3, pady=5)
            current_button.config(command=partial(self.calculator.append_expression, current_button.cget("text")))
            current_button.grid(row=currentRow, column=currentCol)

            currentCol += 1
            if int(current_button.cget("text")) % 3 == 0:
                currentRow -= 1
                currentCol = 0

        # Operator Buttons
        operators = ["+", "−", "×", "÷"]
        currentRow = 1

        for operator in operators:
            current_button = Button(root, text=operator, bg="#2D2D2D", fg="#EEEEEE", width=3, pady=5)
            current_button.config(command=partial(self.calculator.append_expression, current_button.cget("text")))
            current_button.grid(row=currentRow, column=4)
            currentRow += 1

        decimal_button = Button(root, text=".", bg="#2D2D2D", fg="#EEEEEE", width=3, pady=5)
        decimal_button.config(command=partial(self.calculator.append_expression, decimal_button.cget("text")))
        decimal_button.grid(row=4, column=1)

        equals_button = Button(root, text="=", bg="#2D2D2D", fg="#EEEEEE", width=3, pady=5)
        equals_button.config(command=partial(self.calculator.append_expression, equals_button.cget("text")))
        equals_button.grid(row=4, column=2)

        root.mainloop()

Renderer().render()