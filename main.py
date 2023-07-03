import size3, size5, morethan_5, sys, for100, random 
from flask import Flask, request, jsonify
import json
import logging

app = Flask(__name__)

def get_indexed_a(stack_a):
        
    index_a = list(range(1, len(stack_a) + 1))
    stack_len= len(stack_a)
    
    for index, value in enumerate(stack_a):
        pos = 0
        for v in stack_a:
            if v > value:
                pos += 1
        final_pos = stack_len - pos
        index_a[index] = final_pos 
    return (index_a)

def get_stack_a(numbers):
    
    #should first use merge sort? to order the OG array. Then use BTree to get index for each value. It's a bit faster than checking the full array updating the POS 
    stack_a = [int (x) for x in numbers]
    index_a = get_indexed_a(stack_a)
    return (index_a)

def print_logic(movements):
    for idx, move in enumerate(movements):
        #if (move == "sa" and movements[idx + 1] == "sb") or (move =="sb" and movements[idx + 1] == "sa"):
           # print("double")
        if move == "pb" or move == "pa":
            continue
        else:
            j = idx + 1
            char = move[-1]
            if char == "b":
                pair = move.replace("b", "a")
            else:
                pair = move.replace("a", "b")
            while (j < len(movements)):
                if movements[j][-1] == char or movements[j][0] == "p":
                    break
                    
                else:
                    if movements[j] == pair:
                        new = list(movements[j])
                        new[-1] = new[0]
                        new = "".join(new)
                        movements.pop(idx)
                        movements.pop(j - 1)
                        movements.insert(j - 1, new)
                        
                        break
                j += 1


def randomGen(n):
    
    newList = random.sample(range(n), n)
    
    return newList
         
def work(numbers):
    values= []
    maxScore = 0
    maxList = list()
    failedSorts = list()
    space = 0
    numDiv = 2
    stack_a = get_stack_a(numbers)
    copy_a = stack_a.copy()
    movements = list()
    if len(stack_a) == 3:
        stack_a = size3.solve_for_3(stack_a, movements)
    elif len(stack_a) == 5:
        stack_a = size5.solve_for_5(stack_a, movements)
    elif len(stack_a)>= 100:
        #print(", ".join(['"{}"'.format(str(x)) for x in stack_a]))
        stack_a = for100.solve_for_100(stack_a,movements, space, numDiv)
        print_logic(movements)
        minLen = len(movements)
        minMovements = movements.copy()

        while space < 5:
            space += 1
            numDiv = 0
            while numDiv < 5:
                numDiv +=  1
                movements = list()
                stack_a = copy_a.copy()
                stack_a = for100.solve_for_100(stack_a, movements, space, numDiv)
                print_logic(movements)
                if len(movements) < minLen:
                    minLen = len(movements)
                    minMovements = movements.copy()
    else:
        stack_a = morethan_5.more_than5(stack_a, movements)
    if len(stack_a) < 100:
        return (movements)
    else:
        return (minMovements)


@app.route('/receive_numbers', methods=['POST'])
def receive_json():
    try:
        data = request.get_json()
        print((data))
        message = data.get('input')
        print(type(message))
        result = work(message)
        #with open('input.json') as f:
        #    data = json.load(f)
        
       # message = data.get('numbers2')
        
        #result = main(message)
        return jsonify({'success': True, 'result': result})
    except:
        return jsonify({'success': False, 'error': 'Invalid JSON data'})

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run()