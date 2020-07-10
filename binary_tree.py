class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Binary_Tree:
    def __init__(self):
        self.root = None

    def insert(self, num, root):
        if self.root is None:
            self.root = Node(num)
            root = self.root

        elif num <= root.data:
            if root.left is not None:
                self.insert(num,root.left)
            else:
                root.left = Node(num)

        else:
            if root.right is not None:
                self.insert(num,root.right)
            else:
                root.right = Node(num)

    def pre_order(self, root):
        if root is not None:
            print(root.data)

        if root.left is not None:
            self.pre_order(root.left)

        if root.right is not None:
            self.pre_order(root.right)

    def in_order(self, root):
        if root is not None:
            if root.left is not None:
                self.in_order(root.left)

            print(root.data)

            if root.right is not None:
                self.in_order(root.right)

    def post_order(self, root):
        if root is not None:
            if root.left is not None:
                self.post_order(root.left)

            if root.right is not None:
                self.post_order(root.right)

            print(root.data)

    def insert2(self, num, root):
        if self.root is None:
            self.root = Node(num)
            return True

        if num <= root.data:
            if root.left != None:
                self.insert2(num, root.left)
                return True
            else:
                root.left = Node(num)
        else:
            if root.right != None:
                self.insert2(num, root.right)
                return True
            else:
                root.right = Node(num)



########
## TEST
########
a = Binary_Tree()
a.insert2(11, None)
a.insert2(7, a.root)
a.insert2(12, a.root)
# a.insert(6, a.root)
# a.insert(8, a.root)
# a.insert(15, a.root)
# a.insert(4, a.root)
# a.insert(10, a.root)
# a.insert(13, a.root)
# a.insert(11, a.root)
a.pre_order(a.root)
print(a.root.right)
# a.in_order(a.root)
# # a.post_order(a.root)