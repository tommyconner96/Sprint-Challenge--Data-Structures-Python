class RingBuffer:
    # class that implements a new buffer
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity
        # keep track of current node
        self.cur = 0

    def append(self, item):
        # if not at capacity, just append normally
        if len(self.data) < self.capacity:
            self.data.append(item)
        elif self.cur == self.capacity:
            self.cur = 0
            self.data[self.cur] = item
        elif len(self.data) >= self.capacity:
            self.data[self.cur] = item
        else:
            return "an error occured"
        self.cur += 1

    def get(self):
        return self.data
