class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # set item to current location
        self.storage[self.current] = item

        # if current is in last index, move back to index 0
        if self.current == len(self.storage) - 1:
            self.current = 0
        # increment current to next position
        else:
            self.current += 1

    def get(self):
        solution = []
        for i in range(len(self.storage)):
            if self.storage[i]:
                solution.append(self.storage[i])
        return solution


test = RingBuffer(5)

print(len(test.storage))

test.append('a')
test.append('b')
test.append('c')
test.append('d')
print(len(test.storage))  # 5
print(test.get())  # ['a', 'b', 'c', 'd']

test.append('e')
print(len(test.storage))  # 5
print(test.get())  # ['a', 'b', 'c', 'd', 'e']

test.append('f')
print(len(test.storage))  # 5
print(test.get())  # ['f', 'b', 'c', 'd', 'e']

test.append('g')
test.append('h')
test.append('i')
print(len(test.storage))  # 5
print(test.get())  # ['f', 'g', 'h', 'i', 'e']
