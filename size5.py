import aux, size3

def prepare_b(stack, movements):
    
    stack_b = list()
    
    for i in stack[3:]:
        aux.moves_logic(stack,["pb"], movements, stack_b)
        
    return stack_b

def solve_3_with_2(stack_a, stack_b, movements):
    min_b = min(stack_b)
    max_b = max(stack_b)
    

    stack_a = size3.solve_for_3(stack_a, movements)
    if stack_b[0] < stack_b[1]:
        aux.moves_logic(stack_a, ["sb"], movements, stack_b)
    while (stack_b):
        if stack_b[0] == 5 :
            index = stack_a.index(min(stack_a)) 
            if index < (len(stack_a)//2):     
                while (stack_a[0] != min(stack_a)):
                    aux.moves_logic(stack_a, ["ra"], movements,stack_b)
            else:
                while (stack_a[-1] != max(stack_a)):
                    aux.moves_logic(stack_a, ["rra"], movements,stack_b)
            aux.moves_logic(stack_a, ["pa"], movements,stack_b)
        elif stack_b[0] == 1:
            index = stack_a. index(2)
            if index < (len(stack_a)//2):
                while (stack_a[0] != 2):
                    aux.moves_logic(stack_a, ["ra"], movements,stack_b)
            else:
                while (stack_a[0] != 2):
                    aux.moves_logic(stack_a, ["rra"], movements,stack_b)
            aux.moves_logic(stack_a, ["pa"], movements,stack_b)
        else:
            index = stack_a.index(stack_b[0] + 1)
            if index < (len(stack_a)//2):
                while stack_a [0] != stack_b[0] + 1:
                    aux.moves_logic(stack_a, ["ra"], movements) 
            else:
                while stack_a [0] != stack_b[0] + 1:
                    aux.moves_logic(stack_a, ["rra"], movements) 
            aux.moves_logic(stack_a, ["pa"], movements,stack_b)

    if stack_a[0] != 1:
        index = stack_a.index(1)
        if index > (len(stack_a)//2):
            while (stack_a[0] != 1):
                aux.moves_logic(stack_a,["rra"], movements)
        else:
            while (stack_a[0] != 1):
                aux.moves_logic(stack_a,["ra"], movements)



def solve_for_5(stack, movements):
    if aux.is_not_ordered(stack):
        stack_b = prepare_b(stack, movements)
        solve_3_with_2(stack, stack_b, movements)

    return (stack)