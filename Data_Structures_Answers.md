Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
   my append method has a runtime of O(1)
   this is because I am using indexing and assignment,
   the length of the list remains static, no elements need to be shifted

2. What is the space complexity of your ring buffer's `append` function?
   I believe the space complexity of my append method is O(1)
   It does not take additional space because the list has already been initialized

3. What is the runtime complexity of your ring buffer's `get` method?
   the runtime of my get method is O(n), this is because it needs to loop over the entire ring buffer to check for None type values. This was my solution for returning the ring buffer only including the values.

4. What is the space complexity of your ring buffer's `get` method?
   the space complexity of my get method is O(n)
   it initializes a new list to store values so it can return a list without None included

5. What is the runtime complexity of the provided code in `names.py`?
   runtime complexity of the code provided is O(n^2)
   the outer loop checks every name on the list, it is O(n)
   the inner loop checks every name on the list, it is O(n)
   because the inner loop is nested inside of the outer loop, it is O(n^2)

6. What is the space complexity of the provided code in `names.py`?
   the original name lists have a space complexity of O(n)
   the solution code creates a new array to store values, which I believe is O(n)

7. What is the runtime complexity of your optimized code in `names.py`?
   binary search tree solution runtime: O(2n 2log(n)) -> O(n log(n))
   O(n) to loop over names_1 and insert every element into binary search tree
   O(log(n)) to insert into binary search tree, it checks to see if it can insert element once per level
   O(n) to loop over names_2 to check for matches
   O(log(n)) to check for match inside of binary search tree
   O(1) to append to the end of solution list
   runtime: 0.1812 seconds

8. What is the space complexity of your optimized code in `names.py`?
   my solution takes a list and creates a binary search tree, which is O(n)
   and the original code creates a solutions array, which is also O(n)
   this does increase the total space used, but increases the time complexity dramatically
   I believe the space complexity is O(2n) though which should evaluate down to O(n)
