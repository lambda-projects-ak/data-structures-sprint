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
        for i in range(len(self.storage) - 1):
            if not self.storage[i]:
                self.storage.pop(i)

        return self.storage


test = RingBuffer(10)
test.append(1)
test.append(2)
test.append(3)

print(test.get())


print(len(test.storage) - 1)
