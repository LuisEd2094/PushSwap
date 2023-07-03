import aux, size3

def prepare_b(stack, movements):
    
    stack_b = list()
    
    for i in stack[3:]:
        aux.moves_logic(stack,["pb"], movements, stack_b)
        
    return stack_b

def insert_b_value(stack, stack_b, movements, max_value):
    
    stack_len = len(stack)
    #for biggest value
    
    if (stack_b[0] == max_value):
        #get max value in stack A and move it to the top
        value_index = aux.get_index(stack, "max")
        aux.get_max_to_bot(stack, value_index, movements)
        aux.moves_logic(stack, ["pa"], movements, stack_b)        
    #for smallest value
    elif (stack_b[0] == 1):
        #get min value in stack A and move it to the top
        value_index = aux.get_index(stack, "min")
        aux.get_min_to_top(stack, value_index, movements)
        aux.moves_logic(stack, ["pa"], movements, stack_b)    
    else:
        #for every other number, get value that is 
        found, value_index = aux.get_values_for_else(stack, stack_b, max_value)

        if found == False:
            aux.get_min_to_top(stack, value_index, movements)
            aux.moves_logic(stack, ["pa"], movements,stack_b )   
                
        else:
            aux.get_max_to_bot(stack, value_index, movements)
            aux.moves_logic(stack, ["pa"], movements,stack_b)    
        return
    
def more_than5(stack, movements):
    max_value = len(stack)
    stack_b = prepare_b(stack, movements)
    size3.solve_for_3(stack, movements)

    while stack_b:

        insert_b_value(stack, stack_b, movements, max_value)
    while (stack[0] != 1):
        aux.moves_logic(stack,['ra'], movements)
    return stack
        