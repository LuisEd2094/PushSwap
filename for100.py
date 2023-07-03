import aux, size3


def getDivisions(stackLen, numDiv):
    divisions = (round(stackLen / 100)) + numDiv
    if divisions % 2 == 0:
        divisions += 5
    else:
        divisions += 4
    divisionsSize = stackLen // divisions
    
    return (divisions, divisionsSize)

def getRanges(stackLen, divisions, divisionsSize):
    ranges = []
    for i in range(divisions):
        
        if i == 0:
            ranges.append([1, divisionsSize])
        elif i == divisions - 1:
            ranges.append([(divisionsSize) + (divisionsSize * (i - 1)) + 1, stackLen - 2])
        else:
            ranges.append([(divisionsSize) + (divisionsSize * (i - 1)) + 1, divisionsSize + (divisionsSize * i)])
    return (ranges)


def is_in_range(value, range_to_Check):
    if range_to_Check[0] <= value <= range_to_Check[1]:
        return True
    return False

def get_value_and_min_max(stack_b, range_to_search, i, iChanger, value_to_search):
    maxValue, minValue = stack_b[0], stack_b[0]
    place_found = None
    while  i < len(stack_b) and is_in_range(stack_b[i], range_to_search):
        if stack_b[i] > maxValue and stack_b[i] != value_to_search:
            maxValue, minValue = stack_b[i], stack_b[i]
        if stack_b[i] == value_to_search:
            if i < len(stack_b)//2:
                place_found = "top_b"
            else:
                place_found = "bot_b"
            break
        i += iChanger
    return (maxValue, minValue, place_found)

def pre_sort(ranges, stack, movements, divisions):
    count_first, count_second = 0, 0
    i, j = 0 , 1
    stack_b = list()
    stack_b_len = 0
    
    firstRangeSize = ranges[i][1] - ranges[i][0] + 1
    secondRangeSize = ranges[j][1] - ranges[j][0] + 1

    while j < divisions  or i < divisions - 1 :
        
        if count_first == firstRangeSize:
            i += 2
            firstRangeSize = ranges[i][1] - ranges[i][0] + 1
            count_first = 0


        elif count_second == secondRangeSize:
            j += 2
            if j < divisions:
                secondRangeSize = ranges[j][1] - ranges[j][0] + 1
                count_second = 0
                
        ##################################################
    
        if stack_b_len == 0 and (is_in_range(stack[0], ranges[i]) or is_in_range(stack[0], ranges[j])):
            if is_in_range(stack[0], ranges[i]):
                count_first += 1
            else:
                count_second += 1
            aux.moves_logic(stack, ["pb"], movements, stack_b)
            stack_b_len += 1

        ###########################################    
        elif i < (divisions - 1)  and is_in_range(stack[0], ranges[i]):
            aux.moves_logic(stack, ["pb"], movements, stack_b)
            count_first += 1
            if not is_in_range(stack_b[1], ranges[i]):
                aux.moves_logic(stack, ["rb"], movements, stack_b)
        elif j < (divisions)  and is_in_range(stack[0], ranges[j]):
            aux.moves_logic(stack, ["pb"], movements, stack_b)
            count_second += 1
        else:
            aux.moves_logic(stack, ["ra"], movements, stack_b)
    while len(stack) != 3:
        
        if is_in_range(stack[0], [ranges[-1][0], ranges[-1][1] - 1]):
            aux.moves_logic(stack, ["pb"], movements, stack_b)
        else:
            aux.moves_logic(stack, ["ra"], movements, stack_b) 
    size3.solve_for_3(stack, movements)
    return (movements, stack, stack_b)

def if_on_top(stack, stack_b, movements, space, minValue, maxValue, value_to_search, stackLen):
    while stack_b[0] != value_to_search:
        if is_in_range(stack_b[0], [minValue - space, maxValue]):
            if stack[0] == value_to_search + 1 and stack[-1] == stackLen:
                if stack_b[0] < minValue:
                    minValue = stack_b[0]
                aux.moves_logic(stack, ["pa"], movements, stack_b)               
            elif stack_b[0] < minValue:
                if stack[-1] != stackLen:
                    while stack[0] != minValue:
                        aux.moves_logic(stack, ["rra"], movements)
                minValue = stack_b[0]
                aux.moves_logic(stack, ["pa"], movements, stack_b)

                        
            else:
                if stack_b[0] > stack[0]:
                    while stack_b[0] > stack[0]:
                        aux.moves_logic(stack, ["ra"], movements, stack_b)
                else:
                    if stack[-1] != stackLen:
                        while not (stack[0] > stack_b[0] > stack[-1]) and stack[-1] != stackLen:
                            aux.moves_logic(stack, ["rra"], movements)
                        
                aux.moves_logic(stack, ["pa"], movements, stack_b)
        else:
            aux.moves_logic(stack, ["rb"], movements, stack_b)
    while stack[0] != value_to_search + 1:
        aux.moves_logic(stack, ["ra"], movements, stack_b)
        
        
    aux.moves_logic(stack, ["pa"], movements, stack_b)    
    return (stack, stack_b, movements)


def if_on_bot(stack, stack_b, movements, space, minValue, maxValue, value_to_search, stackLen):

    while stack_b[0] != value_to_search:
            if is_in_range(stack_b[0], [minValue - space, maxValue]):
                if stack[0] == value_to_search + 1 and stack[-1] == stackLen:
                    if stack_b[0] < minValue:
                        minValue = stack_b[0]
                    aux.moves_logic(stack, ["pa","rrb"], movements, stack_b)
                    
                        
                    
                elif stack_b[0] < minValue:
                    if stack[-1] != stackLen:
                        while stack[0] != minValue:
                            aux.moves_logic(stack, ["rra"], movements)
                    minValue = stack_b[0]
                    aux.moves_logic(stack, ["pa","rrb"], movements, stack_b)

                            
                else:
    
                    while stack_b[0] > stack[0]:
                        aux.moves_logic(stack, ["ra"], movements, stack_b)
                    while not (stack[0] > stack_b[0] > stack[-1]) and stack[-1] != stackLen:
                        aux.moves_logic(stack, ["rra"], movements)
                            
                    aux.moves_logic(stack, ["pa","rrb"], movements, stack_b)
            else:
                aux.moves_logic(stack, ["rrb"], movements, stack_b)
    while stack[0] != value_to_search + 1:
        aux.moves_logic(stack, ["ra"], movements, stack_b)
        
        
    aux.moves_logic(stack, ["pa"], movements, stack_b)        
    return (stack, stack_b, movements)

def solve_for_100(stack, movements, space, numDiv):
    stack_b = list()
    stackLen = len(stack)
    
    divisions, divisionsSize = getDivisions(stackLen, numDiv)

    ranges = getRanges(stackLen, divisions, divisionsSize)
    
    movements, stack, stack_b = pre_sort(ranges, stack, movements, divisions)
    
    
    j = len(ranges) - 1

    while stack[0] != 1:

        value_to_search = stack[0] - 1

        
        if is_in_range(value_to_search, ranges[j]):
            range_to_search = ranges[j]
        else:
            j -= 1
            range_to_search = ranges[j]
        

        place_found = None
        
        if stack[-1] == value_to_search:
            place_found = "bot_a"

      
        if place_found == None:
            i = 0
            maxValue, minValue, place_found =  get_value_and_min_max(stack_b, range_to_search, 0, 1, value_to_search)
                

        if place_found == None:
            maxValue, minValue, place_found =  get_value_and_min_max(stack_b, range_to_search, len(stack_b) - 1, -1, value_to_search)

        minValue = min(stack)
        if (stack_b):
            maxValue = max(stack_b)
        if (stack_b):
            maxValue = max(stack_b)
        if place_found == "bot_a":
            aux.moves_logic(stack, ["rra"], movements)
        
        elif place_found == "top_b":
            stack, stack_b, movements = if_on_top(stack, stack_b, movements, space, minValue, maxValue, value_to_search, stackLen)

        else:
            aux.moves_logic(stack, ["rrb"], movements, stack_b)
            stack, stack_b, movements = if_on_bot(stack, stack_b, movements, space, minValue, maxValue, value_to_search, stackLen)
    return (stack)
    