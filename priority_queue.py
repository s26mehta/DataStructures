class Priority_Queue:
    def __init__(self):
        self.items =[]
        self.size = 0

    def empty(self):
        return self.size == 0

    def insert(self, num):
        if self.empty() == True:
            self.items.insert(0, None)
            self.size += 1

        last = len(self.items)
        self.items.insert(last, num)
        self.size += 1

        if self.items[last] % 2 == 0:
            while self.items[last] > self.items[last/2]:
                self.items[last], self.items[last] = self.swap(self.items[last], self.items[last])
                last = last/2

        print self.items

    def swap(self, x, y):
        x = x+y
        y = x-y
        x = x-y

        return x,y

    def removeMax(self):
        if self.empty() != True:
            self.items[1], self.items[self.size] = self.swap(self.items[1], self.items[self.size])
            del self.items[self.size]
            self.size -= 1

        current = 1
        while self.items[current] > self.items[current*2] or self.items[current] > self.items[current*2 + 1]:
            if self.items[current] > self.items[current*2] and self.items[current] > self.items[current*2 + 1]:
                if self.items[current*2] > self.items[current*2 + 1]:
                    self.items[current], self.items[current * 2] = self.swap(self.items[current],
                                                                             self.items[current * 2])

                if self.items[current*2] < self.items[current*2 + 1]:
                    self.items[current], self.items[current * 2 + 1] = self.swap(self.items[current],
                                                                                 self.items[current*2 + 1])

                #if self.items[current * 2] == self.items[current * 2 + 1]:
                    # check children to find perfect position

            if self.items[current] > self.items[current *2]:
                self.items[current], self.items[current *2] = self.swap(self.items[current],
                                                                        self.items[current *2])
                current = current * 2

            if self.items[current] > self.items[current*2 + 1]:
                self.items[current], self.items[current*2 + 1] = self.swap(self.items[current],
                                                                           self.items[current*2 +1])
                current = (current * 2) + 1

