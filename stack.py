from size3 import  solve_for_3

class Stack:
    def __init__(self, numbers=None):
        if numbers is None:
            self.numbers = []
        else:
            if type(numbers[0]) == str:
                numbers = [int(x) for x in numbers]
            self.numbers = self.get_index(numbers)
        self.solve_3 = solve_for_3
        
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
    
    