# Calculator App
from tkinter import Tk, Button, mainloop
from functools import partial
from calculator import Calculator

class Renderer():
    '''
        Renders the appearance of the calculator by generating and stying the widgets.
    '''
    def __init__(self):
        '''
            Initialises the renderer by creating a new single instance of the calculator class,
            so operands and operators are appended to one expression, not having their own.
        '''
        self.calculator = Calculator()

    def render(self):
        '''
            The function that renders the calculator.
        '''
        root = Tk()
        root.configure(bg="#1D1D1D")
        # Output Box
        # outputBox = Entry(bg="#555555")
        # outputBox.grid(row=0, column=0)

        # Create number buttons
        button_0 = Button(root, text="0", bg="#2D2D2D", fg="#EEEEEE", width=3, height=1)
        button_0.config(command=partial(self.calculator.append_expression, button_0.cget("text")))
        button_0.grid(row=4, column=0)

        current_row = 3
        current_column = 0

        for i in range (1, 10):
            current_button = Button(root, text=str(i), bg="#2D2D2D", fg="#EEEEEE", width=3, height=1)
            current_button.config(command=partial(self.calculator.append_expression, current_button.cget("text")))
            current_button.grid(row=current_row, column=current_column)

            current_column += 1
            if int(current_button.cget("text")) % 3 == 0:
                current_row -= 1
                current_column = 0

        # Operator Buttons
        operators = ["+", "−", "×", "÷"]
        current_row = 1

        for operator in operators:
            current_button = Button(root, text=operator, bg="#2D2D2D", fg="#EEEEEE", width=3, height=1)
            current_button.config(command=partial(self.calculator.append_expression, current_button.cget("text")))
            current_button.grid(row=current_row, column=4)
            current_row += 1

        decimal_button = Button(root, text=".", bg="#2D2D2D", fg="#EEEEEE", width=3, height=1)
        decimal_button.config(command=partial(self.calculator.append_expression, decimal_button.cget("text")))
        decimal_button.grid(row=4, column=1)

        equals_button = Button(root, text="=", bg="#2D2D2D", fg="#EEEEEE", width=3, height=1)
        equals_button.config(command=self.calculator.evaluate_expression)
        equals_button.grid(row=4, column=2)

        root.mainloop()

Renderer().render()