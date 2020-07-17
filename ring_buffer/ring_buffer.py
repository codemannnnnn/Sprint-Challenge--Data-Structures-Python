class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = [None]*capacity
        self.current = 0

    def append(self, item):
        self.size[self.current] = item
        self.current += 1
        if self.current == self.capacity:
            self.current = 0

    def get(self):
         return [i for i in self.size if i is not None]
