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
            self.size += 1
            return True

    def insert(self, value, index=None):
        if self.size == 0 and index == 0:
            self.addFirst(value)
        if self.size != 0 and self.size == index+1:
            self.addLast(value)
        if index is None:
            self.addLast()
        if index > (self.size-1):
            print "Not a valid index"
            return False

        node = Node(value)
        temp = self.head
        for i in range(index-1):
            temp = temp.next

        node.next = temp.next
        temp.next = node
        self.size +=1

    def removeFirst(self):
        if self.size == 0:
            return False
        else:
            temp = self.head
            self.head = self.head.next
            del temp
            self.size -= 1
            return True

    def removeLast(self, value):
        if self.size == 0:
            return False
        else:
            temp = self.head
            for i in range(self.size-2):
                temp = temp.next

            if temp.next == self.tail:
                del self.tail
                self.tail = temp
                self.size -= 1
                return True
            else:
                return False

    def remove(self, index):
        if self.size == 0:
            print "Linked List is empty"
            return False
        if index == 0:
            self.removeFirst()
        if index == self.size-1:
            self.removeLast()
        if index > (self.size-1):
            print "Not a valid index"
            return False

        temp = self.head
        for i in range(index-1):
            temp = temp.next
        delnode= temp.next
        temp.next = temp.next.next
        del delnode
        self.size -=1