class Stack:
    def __init__(self, numbers=None):
        if numbers is None:
            self.numbers = []
        else:
            if type(numbers[0]) == int:
                self.numbers = numbers