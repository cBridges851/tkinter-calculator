# Calculator App
from tkinter import Tk, Entry, Button, mainloop
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
        self.root = Tk()
        self.root.configure(bg="#1D1D1D")
        self.calculator = Calculator()
        self.output_box = Entry(self.root, fg="#FEFEFE", font=("Consolas 12"), readonlybackground="#555555", justify="right")

    def output_expression(self):
        '''
            The function that outputs the expression to the output box on the screen
        '''
        self.output_box.config(state="normal")
        self.output_box.delete(0, "end")
        self.output_box.insert(0, self.calculator.expression)
        self.output_box.config(state="readonly")
        self.root.after(1, self.output_expression)

    def render(self):
        '''
            The function that renders the calculator.
        '''

        # Output Box
        self.output_box.grid(row=0, column=0, columnspan=5)

        # Create number buttons
        button_0 = Button(self.root, text="0", bg="#2D2D2D", fg="#EEEEEE", width=3, height=1)
        button_0.config(command=partial(self.calculator.append_expression, button_0.cget("text")))
        button_0.grid(row=4, column=0)

        current_row = 3
        current_column = 0

        for i in range (1, 10):
            current_button = Button(self.root, text=str(i), bg="#2D2D2D", fg="#EEEEEE", width=3, height=1)
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
            current_button = Button(self.root, text=operator, bg="#2D2D2D", fg="#EEEEEE", width=3, height=1)
            current_button.config(command=partial(self.calculator.append_expression, current_button.cget("text")))
            current_button.grid(row=current_row, column=4)
            current_row += 1

        decimal_button = Button(self.root, text=".", bg="#2D2D2D", fg="#EEEEEE", width=3, height=1)
        decimal_button.config(command=partial(self.calculator.append_expression, decimal_button.cget("text")))
        decimal_button.grid(row=4, column=1)

        equals_button = Button(self.root, text="=", bg="#2D2D2D", fg="#EEEEEE", width=3, height=1)
        equals_button.config(command=lambda: [self.calculator.evaluate_expression(), self.output_expression()])
        equals_button.grid(row=4, column=2)

        self.root.after(1, self.output_expression)
        self.root.mainloop()

Renderer().render()