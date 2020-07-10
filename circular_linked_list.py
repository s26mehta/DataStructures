class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class Circular_Linked_List:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def size(self):
    return self.size

  def display(self):
    if self.size == 0:
      print("None")
      return
    if self.size == 1:
      print(self.head.data)
      return

    cur_node = self.head
    while cur_node != self.tail:
      print(cur_node.data)
      cur_node = cur_node.next
    print(self.tail.data)
    print("\n")
    return

  def addFirst(self, data):
    node = Node(data)

    if self.size == 0:
      self.head = node
      self.tail = node
      node.next = None
      node.prev = None
    else:
      node.next = self.head
      node.prev = self.tail

      node.next.prev = node
      node.prev.next = node

      self.head = node

    self.size +=1
    return True

  def removeFirst(self):
    if self.size == 0:
      return True
    elif self.size == 1:
      cur_head = self.head
      self.head = None
      self.tail = None
      del cur_head
    elif self.size == 2:
      cur_head = self.head
      self.head = self.tail
      self.head.next = None
      self.head.prev = None
      del cur_head
    else:
      cur_head = self.head
      self.head = cur_head.next
      self.head.prev = cur_head.prev
      self.tail.next = self.head
      del cur_head

    self.size -= 1
    return True

  def addLast(self, data):
    node = Node(data)

    if self.size == 0:
      self.head = node
      self.tail = node
      node.next = None
      node.prev = None
    else:
      node.next = self.head
      node.prev = self.tail

      node.next.prev = node
      node.prev.next = node

      self.tail = node

    self.size +=1
    return True

  def removeLast(self):
    if self.size == 0:
      return True
    elif self.size == 1:
      cur_tail = self.tail
      self.head = None
      self.tail = None
      del cur_tail
    elif self.size == 2:
      cur_tail = self.tail
      self.tail = self.head
      self.tail.next = None
      self.tail.prev = None
      del cur_tail
    else:
      cur_tail = self.tail
      self.tail = cur_tail.prev
      self.head.prev = self.tail
      self.tail.next = self.head
      del cur_tail

    self.size -= 1
    return True

  def iterate(self, index):
    start_index = 0
    cur_node = self.head
    while start_index != index:
      cur_node = cur_node.next
      start_index += 1

    return cur_node

  def insert(self, data, index):
    if index > self.size or index < 0:
      return False
    if index == 0:
      return self.addFirst(data)
    if index == self.size:
      return self.addLast(data)

    node = Node(data)
    cur_node_at_index = self.iterate(index)
    node.prev = cur_node_at_index.prev
    node.next = cur_node_at_index

    node.prev.next = node
    node.next.prev = node

    self.size += 1
    return True

  def remove(self, data, index):
    if index > self.size or index < 0:
      return False
    if index == 0:
      return self.removeFirst(data)
    if index == self.size:
      return self.removeLast(data)

    cur_node_at_index = self.iterate(index)

    cur_node_at_index.prev.next = cur_node_at_index.next
    cur_node_at_index.next.prev = cur_node_at_index.prev

    self.size -= 1
    return True

my_list = Circular_Linked_List()
my_list.display()
my_list.addFirst(1)
my_list.display()
my_list.addFirst(2)
my_list.display()
my_list.addFirst(10)
my_list.display()
my_list.removeFirst()
my_list.display()
my_list.addLast(10)
my_list.display()
my_list.removeLast()
my_list.display()
my_list.removeLast()
my_list.display()
print('\n')
my_list.removeLast()
my_list.display()
print('\n')
my_list.addLast(10)
my_list.display()
print(my_list.size)
print('\n')
my_list.insert(11, 0)
my_list.display()
my_list.insert(1, 6)
my_list.display()
my_list.insert(1, 2)
my_list.display()
my_list.insert(3, 2)
my_list.display()
print(my_list.size)
print('\n')