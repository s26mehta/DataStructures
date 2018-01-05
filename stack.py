class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        del self.items[-1]

    def peek(self):
        if self.size() == 0:
            print("Stack is empty")
        else:
            return self.items[self.size()-1]
