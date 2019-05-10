
import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# binary search tree solution runtime: O(2n 2log(n)) -> O(n log(n))
# O(n) to loop over names_1 and insert every element into binary search tree
# O(log(n)) to insert into binary search tree, it checks to see if it can insert element once per level
# O(n) to loop over names_2 to check for matches
# O(log(n)) to check for match inside of binary search tree
# O(1) to append to the end of solution list
# runtime: 0.1812 seconds

search_tree = BinarySearchTree("str")
duplicates = []

for name_1 in names_1:
    search_tree.insert(name_1)

for name_2 in names_2:
    # search tree for match
    if search_tree.contains(name_2):
        duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
