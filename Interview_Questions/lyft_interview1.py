"""
    Let's say a binary tree is excellent if:
      1) all its non-leaf nodes have two children
      2) all its leaves have the same depth from the root

    For example here is an excellent binary tree (its vertices are labeled 0 through 6):

                 6
               /   \
             2      0
            / \    / \
           1   5  3   4
                       \
                        7

    Imagine a tree with N vertices, labeled 0, 1, ..., N-1. Write a function which does the following:
    Input: Adjacency list of the tree. In other words, a list of N lists, with the i-th list being a
           list of vertex i's neighbors. For example the above tree could be described as:
           [[3, 4, 6], [2], [1, 5, 6], [0], [7, 0], [2], [2, 0], [4]]
           [     0      1        2      3     4      5      6     7 ]

    Output: Boolean. True if the input tree qualifies as an excellent binary tree for some choice of the root; False otherwise

    Don't worry about efficiency at first. Focus first on writing a correct function, then worry about optimizations later.
"""

input_list = [[3, 4, 6], [2], [1, 5, 6], [0], [0], [2], [2, 0]]
input_list_1 = [[3, 4, 6], [2], [1, 5, 6], [0], [7, 0], [2], [2, 0], [4]]

def process_item(item):
    child1, child2, parent = [None, None, None]
    if len(item) == 3:
        child1, child2, parent = item
    if len(item) == 2:
        child1, parent = item
    if len(item) == 1:
        parent = item[0]
    
    return child1,child2,parent


def check_if_tree_excellent(input_list):
    nodes_set = set([i for i in range(len(input_list))])

    parent_child_map = {}

    for node, item in enumerate(input_list):

        if node not in parent_child_map:
            parent_child_map[node] = set()

        child1,child2,parent = process_item(item)
        if child1:
            parent_child_map[node].add(child1)
            if child1 in nodes_set:
                nodes_set.remove(child1)
        if child2:
            parent_child_map[node].add(child2)
            if child2 in nodes_set:
                nodes_set.remove(child2)
        if parent:
            if parent not in parent_child_map:
                parent_child_map[parent] = set()
            parent_child_map[parent].add(node)
            if node in nodes_set:
                nodes_set.remove(node)
    
    print(parent_child_map)

    return validate_tree(nodes_set.pop(), parent_child_map, 0, [None])

def validate_tree(cur_node, parent_child_map, distance, leaf_distance):
    children = parent_child_map[cur_node]

    if len(children) == 1:
        return False

    if len(children) == 0:
        if leaf_distance[0] == None:
            leaf_distance[0] = distance
        elif leaf_distance[0] != distance:
            return False

    res = True
    for child in children:
        res = res and validate_tree(child, parent_child_map, distance+1, leaf_distance)

    return res


print(check_if_tree_excellent(input_list))
print(check_if_tree_excellent(input_list_1))




















# def find_root_node(input_list, node, root_node):
#     if len(input_list[node]) == 3:
#         root_node = find_root_node(input_list, input_list[node][2], root_node)
#     else:
#         root_node = node
#     return root_node

# def validate_excellent_binary_tree(input_list):
#     root_node = None

#     # Find root node:
#     for node, node_list in enumerate(input_list):
#         if len(node_list) == 3:
#             found_node = find_root_node(input_list, node_list[2], root_node)
#             if root_node == None:
#                 root_node = found_node
#             else:
#                 if root_node != found_node:
#                     return False

#     # Validate excellent binary tree
#     return validate_tree(root_node, input_list, 1, [None])

# def validate_tree(node, input_list, cur_leaf_length, max_leaf_node_length):
#     if len(input_list[node]) == 1:
#         if max_leaf_node_length[0] == None:
#             max_leaf_node_length[0] = cur_leaf_length
#         else:
#             if max_leaf_node_length[0] != cur_leaf_length:
#                 return False

#     res = True
#     for idx, child in enumerate(input_list[node]):
#         # prevent recursive loop
#         if idx == 2:
#             break

#         # non leaf node
#         elif len(input_list[child]) == 3:
#             if input_list[child][2] == node:
#                 res = validate_tree(child, input_list, cur_leaf_length + 1, max_leaf_node_length) and res
#         # leaf node
#         elif len(input_list[child]) == 1:
#             res = validate_tree(child, input_list, cur_leaf_length + 1, max_leaf_node_length) and res
#         # invalid node
#         if len(input_list[child]) == 2:
#             res = False and res
#     return res


# print("input_list", validate_excellent_binary_tree(input_list))
# print("input_list_1", validate_excellent_binary_tree(input_list_1))