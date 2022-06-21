# Code Challenge 11
Implement a Queue using two Stacks with enqueue and dequeue

Whiteboard Process<br>
[Pseudo-queue whiteboard](Psuedoqueue.jpg)

Approach & Efficiency<br>
Algorithm:Create two instances of Stack, one in, one out. To add to the queue, or ENQUEUE we have to use the .push method.<br> passing in the value as an argument in the stack
To remove from the queue, first we check the queue to see if its empty.<br> If it is, we use a while loop to move nodes from the in stack into the out stack.<br>  We then use pop with the out stack which will return it on top of the out stack.
.

This solution is
BigO Time: O(N)
BigO Space: O(1)

Solution
This code is not executable.
