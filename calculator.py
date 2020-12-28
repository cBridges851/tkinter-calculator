class Calculator():
    def __init__(self):
        self.expression = ""

    def append_expression(self, value):
        self.expression += value
        print(self.expression)