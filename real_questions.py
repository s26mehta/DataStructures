#################################################################################
## Bloomberg Interview: Check if a binary tree is a binary search tree
##                      Binary tree is where each node contains a left and right
##                      reference and a data element
##                      BST is where its a binary tree but has the property
##                      Right <= Node <= left (duplicates not allowed)
#################################################################################


class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


int_max = 100000000
int_min = 0

def is_bst(node, min=int_min, max=int_max):

    if node is None:
        return True

    if node.data < min or node.data > max:
        return False

    return is_bst(node.left, min, node.data-1) and is_bst(node.right, node.data+1, max)

def in_order(root):
    if root.left is not None:
        in_order(root.left)

    print root.data

    if root.right is not None:
        in_order(root.right)



# import binary_tree as bt
# a = bt.Binary_Tree()
# a.insert(11, None)
# a.insert(7, a.root)
# a.insert(12, a.root)
# a.insert(6, a.root)
# a.insert(8, a.root)
# a.insert(15, a.root)
# a.insert(4, a.root)
# a.insert(10, a.root)
# a.insert(13, a.root)
# # a.insert(11, a.root)
#
# print is_bst(a.root)
#
# a.in_order(a.root)


#################################################################################
## Yelp Interview: Given a list of comment objects for a blog print out the
##                 hierarchial structure of the comments using spaces
##                 class Comments:
##                      self.id
##                      self.parent_comment_id
##                      self.text
##                      self.blog_id (assume all comments are for same blog
#################################################################################
class Comments:
    def __init__(self, id, parent_comment_id, text, blog_id):
        self.id = id
        self.parent_comment_id = parent_comment_id
        self.text = text
        self.blog_id = blog_id

dict = {}
def print_comments(comments):
    unassigned_childs = []
    for c in comments:
        if c.parent_comment_id == None:
            dict[c.id] = ['no_parent', c.text, []]
        else:
            dict[c.id] = [c.text, []]
            if c.parent_comment_id in dict:
                if len(dict[c.parent_comment_id]) > 2:
                    dict[c.parent_comment_id][2].append(c.id)
                else:
                    dict[c.parent_comment_id][1].append(c.id)
            else:
                unassigned_childs.append([c.id,c.parent_comment_id])
    if len(unassigned_childs) is not 0:
        for i in unassigned_childs:
            if dict[i[0]] != 'no_parent':
                dict[i[1]][1].append(i[0])
            else:
                dict[i[1]][2].append(i[0])

    for key in dict:
        if dict[key][0] is 'no_parent':
            print dict[key][1]
            recursive_child_print(dict[key][2], "  ")


def recursive_child_print(arr=[], indent=""):
    for i in arr:
        print(indent + dict[i][0])
        if len(dict[i][1]) is not 0:
            recursive_child_print(dict[i][1], indent+"  ")

# a = [Comments(1, None, "test", 1), Comments(6, 2, "kk", 1), Comments(2, 1, "random shit", 1),
#      Comments(3, 4, "pure sexy", 1) ,Comments(4, 1, "I love you", 1), Comments(5, 2, "k", 1)]
#
# print_comments(a)



#################################################################################
## Square Interview: Problem: A farmer wants to take a fox, a chicken, and a bag
# of grain across a river. He has only one boat with which he can carry one item
# across the river at once. The only issue is that if the fox and chicken are
# left unsupervised, the fox will eat the chicken. The same goes for the chicken
# and the grain.

# Goal: Print out a series of steps that the farmer could take to transport
# all three items across the river.

# One way the farmer might solve this is to:

# Take chicken over
# Return
# Take fox over
# Return with chicken
# Take grain over
# Return
# Take chicken over
#################################################################################

class State:
    def __init__(self, start=["Fox", "Chicken", "Grain"], dest=[], farmer="start"):
        self.start = start
        self.destination = dest
        self.farmer = farmer

    def is_goal(self):
        if self.farmer is not "destination":
            return False

        if "Fox" not in self.destination:
            return False

        if "Chicken" not in self.destination:
            return False

        if "Grain" not in self.destination:
            return False

        return True

    def is_valid(self):
        if self.farmer == "destination":
            if "Chicken" not in self.destination and "Grain" not in self.destination:
                return False
            if "Fox" not in self.destination and "Chicken" not in self.destination:
                return False
        else:
            if "Chicken" not in self.start and "Grain" not in self.start:
                return False
            if "Fox" not in self.start and "Chicken" not in self.start:
                return False
        return True

    def next_states(self):
        next_states = []

        if self.farmer == "start":
            for item in self.start:
                new_state = State(self.start[:], self.destination[:], self.farmer)
                new_state.start.remove(item)
                new_state.destination.append(item)
                new_state.farmer = "destination"
                next_states.append(new_state)
        else:
            for item in self.destination:
                new_state = State(self.start[:], self.destination[:], self.farmer)
                new_state.destination.remove(item)
                new_state.start.append(item)
                new_state.farmer = "start"
                next_states.append(new_state)

        if self.farmer == "start":
            new_state = State(self.start[:], self.destination[:], self.farmer)
            new_state.farmer = "destination"
            next_states.append(new_state)
        else:
            new_state = State(self.start[:], self.destination[:], self.farmer)
            new_state.farmer = "start"
            next_states.append(new_state)

        return next_states

    def print_state(self):
        print("Farmer is %s" % self.farmer)
        print("Start is %s" % self.start)
        print("Destination is %s" % self.destination)
        print("\n")


# b = State()
# for state in b.next_states():
#     state.print_state()

#################################################################################
## Google Interview: Sum up the levels of a tree Given:
#          3
#        / | \
#       1  5  10  # depth = 1
#      /  / \ \
#     6  1  4  5  # depth = 2
#
# Expect:
# [3, 16, 16]
#################################################################################


class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children  # Array

sum = []
def printSum(root, depth=0):
    if depth == 0:
        b = root.data
        sum.append(root.data)
        printSum(root.children, depth+1)
    else:
        curSum = 0
        children = []
        for c in root:
            curSum += c.data
            if len(c.children) != 0:
                for i in c.children:
                    children.append(i)
        sum.append(curSum)
        if len(children) != 0:
            printSum(children, depth+1)


h = Node(5, [])
g = Node(4, [])
f = Node(1, [])
e = Node(6, [])
d = Node(10, [h])
c = Node(5, [f,g])
b = Node(1, [e])
a = Node(3, [b,c,d])

# printSum(a)
# print(sum)

#################################################################################
## Google Interview: Remove every other node from a circular linked list:
#################################################################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class C_Linked_List:
    def __init__(self, head):
        self.head = head
        self.size = 0

    def size(self):
        return self.size


ls = C_Linked_List(Node(2))


def remove_every_other(c_list):
    if c_list.size == 0 or c_list.size == 1:
        return False
    else:
        cur_node = c_list.head
        iteration_started = False
        while cur_node.next != c_list.head and (iteration_started == False and cur_node != c_list.head):
            remove_next(cur_node)
            c_list.size -= 1
            cur_node = cur_node.next
            iteration_started = True


def remove_next(node):
    temp = node.next
    node.next = temp.next
    del temp





