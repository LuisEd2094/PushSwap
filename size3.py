import aux

def solve_for_3(stack, movements):
    
    while (aux.is_not_ordered(stack)):
        if (stack[0] > stack[1]) and (stack[1] < stack[2]) and (stack[2] > stack[0]):
            aux.moves_logic(stack, ["sa"],movements)
        elif (stack[0] > stack[1]) and (stack[1] > stack[2]) and (stack[2] < stack[0]):
            aux.moves_logic(stack, ["sa", "rra"],movements)
        elif (stack[0] > stack[1] and stack[1] < stack[2] and stack[2] < stack[0]):
            aux.moves_logic(stack, ["ra"],movements)
        elif (stack[0] < stack[1] and stack[1] > stack[2] and stack[2] > stack[0]):
            aux.moves_logic(stack, ["sa", "ra"],movements)
        else:
            aux.moves_logic(stack, ["rra"],movements)
            
    return (stack)
