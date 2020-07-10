class Queue:
    def __init__(self, maxSize):
        self.items = []
        self.maxSize = maxSize
        self.startIndex = 0
        self.endIndex = 0
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        if self.size <= self.maxSize:
            if self.endIndex == self.maxSize-1:
                self.endIndex = 0
                self.items[self.endIndex] = item
                self.size += 1
            else:
                self.items.append(item)
                self.size += 1
                if (self.size != 1 and self.size != 0):
                    self.endIndex += 1
            return True
        else:
            return False

    def dequeue(self):
        if self.size == 0:
            return False
        else:
            temp = self.startIndex
            self.items[self.startIndex] = None
            if self.startIndex == self.maxSize-1:
                self.startIndex = 0
            else:
                self.startIndex += 1
            self.size -= 1
            return temp

    def peek(self):
        if self.size() == 0:
            print("Queue is empty")
        else:
            return self.items[self.startIndex]

q = Queue(5)
q.enqueue(1)
print(q.items)
q.enqueue(1)
print(q.items)
q.enqueue(2)
print(q.items)
q.enqueue(1)
print(q.items)
q.enqueue(1)
print(q.items)
q.enqueue(3)
q.enqueue(4)
q.enqueue(4)
print(q.items)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.items)
q.enqueue(12)
q.enqueue(13)
q.enqueue(14)
q.enqueue(15)
print(q.items)
