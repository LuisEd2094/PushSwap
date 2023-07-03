# PushSwap
Python program for 42 Barcelona's PushSwap Project

My Python implementation of the Push_Swap sorting algorithm from the 42 Programming School.

The program takes a Json file as a parameter, with an 'input' key which will contain a non-ordered, non-repeated set of ints.

The program uses two stacks, stack-a and stack-b, for the sorting. 

At the start all numbers will be stored in stack-a, the first number of the list being at the top of the stack.

For example, if the input is  3, 2, 1, then stack-a would look something like:

Stack-a     Stack-b

3           Empty
2
1

Afterwards, it'd look for the least amount of moves needed to order the numbers from smallest to highest, leaving them all in stack-a at the end, and returning a json file containing:
{'success': True, 'result': result} if it succesfully ordered the numbers, with result containing the list of moves used to order the stack.

The allowed moves are the following: 

sa (swap a): Swap the first 2 elements at the top of stack a.
Do nothing if there is only one or no elements.

sb (swap b): Swap the first 2 elements at the top of stack b.
Do nothing if there is only one or no elements.

ss : sa and sb at the same time.

pa (push a): Take the first element at the top of b and put it at the top of a.
Do nothing if b is empty.

pb (push b): Take the first element at the top of a and put it at the top of b.
Do nothing if a is empty.

ra (rotate a): Shift up all elements of stack a by 1.
The first element becomes the last one.

rb (rotate b): Shift up all elements of stack b by 1.
The first element becomes the last one.

rr : ra and rb at the same time.

rra (reverse rotate a): Shift down all elements of stack a by 1.
The last element becomes the first one.

rrb (reverse rotate b): Shift down all elements of stack b by 1.
The last element becomes the first one.

rrr : rra and rrb at the same time

Logic:

It first checks the numbers and assigns them their final index relative to the other numbers.

For example,

Stack-a,

5
3
1

Becomes

3
2
1

This way, we know where each number will end up in.

It essentially look for the size of the stack first before deciding what to do. 

Size 3: there are only 5 possible combinations that we have to look for, so it simply checks which one is true and returns the corresponding moves.

Size 5: it moves the first 2 numbers from stack a  to stack b, then applies size 3 rules, and then it looks into inserting the 2 numbers in stack b in their corresponding order.

Size >5: at this point it looks to create different ranges that will be sent to stack b until only 3 numbers remain at stack-a, orders them using Size 3 rules, and the proceeds to send back the numbers
from stack-b to stack-a. It looks at the smallest number at stack-a, and if the first number in stack-b is within certain range of it, it will move it to the bottom of stack-a for later usage. 

If there are already a "semi" stack at the bottom of a, it'd make sure they are ordered, so you could end up having something like this:

Stack-a     stack-b

97          93
98          96
99          ... Rest of the numbers
100
92
94
95

In this example, it'd look to place 93 between 92 and 94, it'd then move 96 (who is now at the top of stack-b) to the top of stack-a. Then it'd look for the next number, 95, see that's at the bottom of 
Stack-A, and move it to the top, then againt with 94, 93, and 92. It'd then look for 91 and the rest of the numbers

Once we have the index 1 at the top of the stack-a, it's considered to be ordered and it now checks the moves made.


When ever it finds to matching moves next to each other, it'd change them with their "double move" match.

For example, if at some point it has ra and rb as two moves, it'd change them to rr, 

Likewise for rra and rrb or rrb and rra, whatever order it finds them in.