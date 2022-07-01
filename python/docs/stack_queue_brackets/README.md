## Code Challenge 13
Stack queue brackets

### Challenge summary

Create a function that pops out a validates a bracket is attached to its  matching pain in matching order.

### Whiteboard Process
[Stack queue brackets](Stack_queue_brackets.jpg)

### Approach/Efficiency

Create an instance of a stack. check characters are an open bracket, if they are push to the stack.  if not, move to the next conditionals.

if the stack is empty, return false.

compare opening bracket to provided closing bracket.  if a match or pair is found, pop from the stack and repeat with the next character. if all characters have a match return true.

else stack is not empty so return false.


### Big 0

Big O
Time :0(N)
Space:0(N)

### Solution

This isnt executable code. Must be run inside pycharm
