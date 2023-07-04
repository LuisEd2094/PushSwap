import size3, size5

class Stack:
    def __init__(self, numbers=None):
        if numbers is None:
            self.stack = []
        else:
            if type(numbers[0]) == str:
                numbers = [int(x) for x in numbers]
            self.stack = self.get_index(numbers)
        self.solve_3 = self.solve_for_3
        self.solve_5 = self.solve_for_5
    
    def solve_for_3(self, movements):
        size3.solve_for_3(self.stack, movements)
    def solve_for_5(self, movements):
        size5.solve_for_5(self.stack, movements)
            
    @staticmethod
    def get_index(numbers):
        index_a = list(range(1, len(numbers) + 1))
        stack_len = len(numbers)
        
        for index, value in enumerate(numbers):
            pos = 0
            for v in numbers:
                if v > value:
                    pos += 1
            final_pos = stack_len - pos
            index_a[index] = final_pos 
        return (index_a)