class Calculator():
    '''
        The class that manages the input of the expression and processes it to create a final answer.
    '''
    def __init__(self):
        '''
            Initialises the calculator by setting a starting value to the expression.
        '''
        self.expression = ""

    def append_expression(self, value):
        '''
            Appends values to the expression.
        '''
        self.expression += value
        print(self.expression)