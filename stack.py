import aux

class Stack:
    def __init__(self, numbers=None):
        if numbers is None:
            self.stack = []
        else:
            if type(numbers[0]) == str:
                numbers = [int(x) for x in numbers]
            self.stack = self.get_index(numbers)
        self.solve_3 = self.solve_for_3
        
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
    
    def solve_for_3(self, movements):
        while (aux.is_not_ordered(self.stack)):
            if (self.stack[0] > self.stack[1]) and (self.stack[1] < self.stack[2]) and (self.stack[2] > self.stack[0]):
                aux.moves_logic(self.stack, ["sa"], movements)
            elif (self.stack[0] > self.stack[1]) and (self.stack[1] > self.stack[2]) and (self.stack[2] < self.stack[0]):
                aux.moves_logic(self.stack, ["sa", "rra"],movements)
            elif (self.stack[0] > self.stack[1] and self.stack[1] < self.stack[2] and self.stack[2] < self.stack[0]):
                aux.moves_logic(self.stack, ["ra"],movements)
            elif (self.stack[0] < self.stack[1] and self.stack[1] > self.stack[2] and self.stack[2] > self.stack[0]):
                aux.moves_logic(self.stack, ["sa", "ra"],movements)
            else:
                aux.moves_logic(self.stack, ["rra"],movements)
        return (self.stack)
        
    