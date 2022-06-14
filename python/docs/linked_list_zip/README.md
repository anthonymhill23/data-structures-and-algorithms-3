# Code Challenge 08

## Zipped Linked Lists

### White Board

Brian and Anthony's whiteboard<br>
![Whiteboard](Linked_List_Zip%20(1).jpg)

## Link to code
[Code Link] (../data-structures-and-algorithms-3/python/code_challenges/linked_list_zip.py)


### Approach and Efficiency

1. Take two lists, a and b<br>
2. start at a.head and insert b.head after<br>
3. set a.head to a.next -> On the new list<br>
4. set b.head to b.next so you can get the new value from the b list.<br>
5. if there is an a.next then advance one more so that you are off the newly added B and back on the next node of the A-list.







