def is_not_ordered(stack):
    if sorted(stack) == stack:
        return False
    return True

def moves_logic(stack, orders, movements, stack_b = None):
    
    for order in orders:
        movements.append(order)
        if (order == "sa"):
            stack.insert(0, stack.pop(1))
        elif (order == "rra"):
            stack.insert(0, stack.pop(len(stack) - 1))
        elif (order == "ra"):
            stack.insert(len(stack) - 1, stack.pop(0))
        elif (order == "pb"):
            stack_b.insert(0, stack.pop(0))
        elif (order == "pa"):
            stack.insert(0, stack_b.pop(0))
        elif (order == "sb"):
            stack_b.insert(0, stack_b.pop(1))
        elif (order == "rb"):
            stack_b.insert(len(stack_b) - 1, stack_b.pop(0))
        elif (order == "rrb"):
            stack_b.insert(0, stack_b.pop(len(stack_b) - 1))
            


def get_index(stack, order):
    stack_len = len(stack)
    i = 0
    value_index = 0
    value = stack[0]
    if order == "max":
        while i < stack_len:
            if stack[i] > value:
                value = stack[i]
                value_index = i
            i +=1
    elif order == "min":
        while i < stack_len:
            if stack[i] < value:
                value = stack[i]
                value_index = i
            i +=1
    return (value_index)
    
        
    

def get_max_to_bot(stack, value_index, movements):
    stack_len = len(stack)
   
    while value_index != stack_len - 1:
        if value_index < (stack_len // 2):
            moves_logic(stack, ["ra"],movements)
            if value_index == 0:
                value_index = stack_len - 1
            else:
                value_index -= 1
        else:
            moves_logic(stack, ["rra"], movements)
            if value_index == stack_len -1:
                value_index = 0
            else:
                value_index +=1


def get_min_to_top(stack, value_index, movements):

    stack_len = len(stack)
    while value_index != 0:
        if value_index < (stack_len // 2):
            moves_logic(stack, ["ra"],movements)
            value_index -= 1
        else:
            moves_logic(stack, ["rra"], movements)
            if value_index == stack_len -1:
                value_index = 0
            else:
                value_index +=1
                
def get_values_for_else(stack, stack_b, max_value):
    stack_len = len(stack)
    found = False
    i = 0
    value_to_move = 0
    index_of_value_to_move = 0
    min_value = max_value
    min_value_index = 0
    while i < stack_len:
        if stack[i] < min_value:
            min_value = stack[i]
            min_value_index = i
        if stack[i] < stack_b[0] and found == False:
            value_to_move = stack[i]
            index_of_value_to_move = i
            found = True
        elif (stack[i] < stack_b[0]) and (stack[i] > value_to_move) and (found == True):
            value_to_move = stack[i]
            index_of_value_to_move = i
        i += 1
    if found == False:
        value_to_move = min_value
        index_of_value_to_move = min_value_index
        
    return (found, index_of_value_to_move)



        
