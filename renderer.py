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
        button0 = Button(root, text="0", bg="#2D2D2D", fg="#EEEEEE", padx=5, pady=5)
        button0.config(command=partial(self.calculator.append_expression, button0.cget("text")))
        button0.grid(row=4, column=1)

        currentRow = 3
        currentCol = 0

        for i in range (1, 10):
            currentButton = Button(root, text=str(i), bg="#2D2D2D", fg="#EEEEEE", padx=5, pady=5)
            currentButton.config(command=partial(self.calculator.append_expression, currentButton.cget("text")))
            currentButton.grid(row=currentRow, column=currentCol)

            currentCol += 1
            if int(currentButton.cget("text")) % 3 == 0:
                currentRow -= 1
                currentCol = 0

        root.mainloop()

Renderer().render()