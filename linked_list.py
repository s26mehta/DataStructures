class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def display(self):
        node = self.head
        while (node!= None):
            print node.data
            node = node.next

    def search(self, value):
        node = self.head
        index = 0
        while (node!= None):
            if node.data == value:
                print "Found at index %s" % index
            node = node.next
            index += 1


    def addFirst(self, value):
        node = Node(value)

        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
            return True
        else:
            node.next = self.head
            self.head = node
            self.size += 1
            return True

        return False

    def addLast(self, value):
        node = Node(value)
        if self.size == 0:
            self.addFirst(value)
        else:
            self.tail.next = node
            self.tail = node

    def insert(self, index, value):
        if self.size == 0 and index == 0:
            self.addFirst(value)
        if self.size != 0 and self.size == index+1:
            self.addLast(value)




