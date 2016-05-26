class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return False
        else:
            num = -1 * self.size()
            del self.items[num]

    def peek(self):
        if self.size() == 0:
            print("Queue is empty")
        else:
            return self.items[0]
