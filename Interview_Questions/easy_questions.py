from collections import deque
import math

#################################################################################
## Interview: Given an array of positive integers and a number k. Find the 
##            number of pairs of integers for which the difference between the
##            two numbers is equal to a given number k
##            k = 3, arr = [1,6,8,1,2,4,6,9]
## 
#################################################################################
def find_num_pairs(arr, k):
    arr_set = set(arr)
    pairs = set()

    for i in arr:
        if i+k in arr_set:
            pairs.add(tuple(sorted([i, i+k])))
        if i-k in arr_set:
            pairs.add(tuple(sorted([i, i-k])))
    
    return pairs
    

#################################################################################s
## Interview: Output the first letter in the string that doesn't repeat
#################################################################################

def find_first_non_repeating_letter(input_string):
    letter_map = {}

    for letter in input_string:
        if letter not in letter_map:
            letter_map[letter] = 0
        letter_map[letter] += 1

    for letter in input_string:
        if letter_map[letter] == 1:
            return letter

    return None


#################################################################################
## Yelp Interview: Given a list of comment objects for a blog print out the
##                 hierarchial structure of the comments using spaces
##                 class Comment:
##                      self.id
##                      self.parent_comment_id
##                      self.text
##                      self.blog_id (assume all comments are for same blog
#################################################################################

class Comment:
    def __init__(self, id, parent_comment_id, text, blog_id):
        self.id = id
        self.parent_comment_id = parent_comment_id
        self.text = text
        self.blog_id = blog_id

def print_comments_structure(comments):
    no_parent_comments = []
    comments_map = {}
    for comment in comments:
        if comment.parent_comment_id == None:
            no_parent_comments.append(comment)
        else:
            if comment.parent_comment_id not in comments_map:
                comments_map[comment.parent_comment_id] = []
            comments_map[comment.parent_comment_id].append(comment)
            if comment.id not in comments_map:
                comments_map[comment.id] = []

    print("Print comments recursively")
    for comment in no_parent_comments:
        print(comment.text)
        comment_dfs(comment.id, comments_map)
    
    print("Print comments iteratively")
    for comment in no_parent_comments:
        comment_bfs(comment, comments_map)


def comment_dfs(comment_id, comments_map, spaces=2):
    for child_comment in comments_map[comment_id]:
        print(" "*spaces + child_comment.text)
        comment_dfs(child_comment.id, comments_map, spaces+2)

def comment_bfs(comment, comments_map):
    stack = [[comment, 0]]

    while stack:
        cur_comment, spaces = stack.pop()
        print(" "*spaces, cur_comment.text)
        for comment in comments_map[cur_comment.id]:
            stack.append([comment, spaces+2])


all_comments = [
    Comment(1, None, "Comment1", 1),
    Comment(6, 2, "Comment3", 1),
    Comment(2, 1, "Comment2", 1),
    Comment(3, 4, "Comment3", 1),
    Comment(4, 1, "Comment4", 1),
    Comment(5, 2, "Comment3", 1)
]
# print(print_comments_structure(all_comments))


#################################################################################
## Interview: Find missing num in a sorted array (1 to n)
#################################################################################

def find_missing_num(input_arr):
        start = 0
        end = len(input_arr) - 1

        while end-start > 1:
            mid = math.floor((end-start)/2) + start
            if nums[mid] != mid:
                end = mid
            else:
                start = mid+1
        
        if nums[start] != start:
            return start
        elif end == nums[end]:
            return end + 1
        else:
            return end


def missing_num_in_sorted_array(input_arr):
    if len(input_arr) == input_arr[-1]:
        print("No missing number")
        return
    
    # Iterative
    print("Finding missing num in sorted array iteratively:")
    start = 0
    end = len(input_arr)-1
    while end - start > 1:
        mid = math.floor((end-start)/2) + start
        if input_arr[mid] != mid+1:
            end = mid
        else:
            start = mid
    if input_arr[start] != start+1:
        print("    Missing num is: " + str(start+1))
    else:
         print("    Missing num is: " + str(end+1))


    # Recursive 
    print("Finding missing num in sorted array recursively:")
    def binary_search(input_arr, start, end, test=4):
        if test == 0:
            return 0
        if end-start == 1:
            if input_arr[start] != start+1:
                return start+1
            else:
                return end+1
        mid = math.floor((end-start)/2)
        if input_arr[mid+start] != start+mid+1:
            return binary_search(input_arr, start, start+mid, test-1)
        else:
            return binary_search(input_arr, start+mid, end, test -1)
    missing_num = binary_search(input_arr, 0, len(input_arr)-1)
    print("    Missing num is:" + str(missing_num))

# print(missing_num_in_sorted_array([1, 2, 3, 4, 6, 7]))
# print(missing_num_in_sorted_array([1, 3, 4, 5]))
# print(missing_num_in_sorted_array([1, 2, 3, 4, 5]))
# print(missing_num_in_sorted_array([1, 2]))

#####################################################################################
# Given an array of integers find the kth largest integer. You can assume there
# are no duplicates

# Ex:  [6,10,5,7,8,3,1]

# If k == 3  ans ==> 7
# If k == 2  ans ==> 8
# If k == 6  ans ==> 3
#####################################################################################
from heapq import heappop, heappush

def find_k_largest_int(input_arr, k):
    min_heap = []
    for val in input_arr:
        if len(min_heap) < k:
            heappush(min_heap, val)
        elif val > min_heap[0]:
            heappush(min_heap, val)
            heappop(min_heap)
    return min_heap[0]

# print(find_k_largest_int([6, 10, 5, 7, 8, 3, 1], 6))

#####################################################################################
## Interview: Given an array of integers find the kth largest integer. Has duplicates
# Ex:  [6,10,5,7,8,3,1,10]

# If k == 3  ==> 7
# If k == 2  ==> 8
# If k == 6  ==> 3
#####################################################################################
def find_k_largest_int_duplicates(input_arr, k):
    input_arr_dedupe = set(input_arr)
    return find_k_largest_int(input_arr_dedupe, k)

# print(find_k_largest_int_duplicates([6, 10, 5, 10, 7, 8, 3, 1], 6))

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

    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


def level_sum_iterative(root):
    result = []
    stack = [(root, 0)]
    while len(stack) > 0:
        cur_node, cur_level = stack.pop()
        if len(result) < cur_level + 1:
            result.append(cur_node.value)
        else:
            result[cur_level] += cur_node.value
        for child in cur_node.children:
            stack.append((child, cur_level + 1))
    return result


def level_sum_recursive(root):
    result = []

    def dfs(node, result, level=0):
        if len(result) < level + 1:
            result.append(node.value)
        else:
            result[level] += node.value
        for child in node.children:
            dfs(child, result, level + 1)

    dfs(root, result)
    return result

h = Node(5, [])
g = Node(4, [])
f = Node(1, [])
e = Node(6, [])
d = Node(10, [h])
c = Node(5, [f, g])
b = Node(1, [e])
a = Node(3, [b, c, d])

# print(level_sum_iterative(a))
# print("--------------")
# print(level_sum_recursive(a))

#################################################################################
## Google Interview: Remove every other node from a circular linked list:
#################################################################################
class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Circular_Linked_List:

    def __init__(self, head: LinkedListNode):
        self.head = head

    def print(self):
        result = [self.head.data]
        node = self.head.next
        while node != self.head:
            result.append(node.data)
            node = node.next
        print(result)

def remove_every_other_node(head):
    prev_node = head
    cur_node = head.next

    while cur_node != head:
        prev_node.next = cur_node.next
        del cur_node
        prev_node = prev_node.next
        cur_node = prev_node.next
        if prev_node == head:
            break
        print(prev_node.data, cur_node.data)

    return head

# head = LinkedListNode(1)
# second = LinkedListNode(2)
# third = LinkedListNode(3)
# fourth = LinkedListNode(4)
# fifth = LinkedListNode(5)
# sixth = LinkedListNode(6)
# seventh = LinkedListNode(7)
# head.next = second
# second.next = third
# third.next = fourth
# fourth.next = fifth
# fifth.next = sixth
# sixth.next = seventh
# seventh.next = head
# circular_ll = Circular_Linked_List(head)
# circular_ll.print()
# print("_________")
# remove_every_other_node(head)
# circular_ll.print()

####################################################################
### Merge two strings
####
### Ex: 'abc' + 'defedfe'
###
### Result = 'adbecfedfe
####################################################################
def merge_two_string(str_1, str_2):
    end = max(len(str_1), len(str_2))
    start = 0
    result = ""
    while start < end:
        if start < len(str_1):
            result += str_1[start]
        if start < len(str_2):
            result += str_2[start]
        start += 1
    return result

# print(merge_two_string('abc', 'defedfe'))

###################################################################################
### Find all combinations of two  numbers that equal to sum in unsorted array
###################################################################################
def find_combinations(input_arr, total_sum):
    nums_dict = {}
    for val in input_arr:
        if val not in nums_dict:
            nums_dict[val] = 0
        nums_dict[val] += 1
    result = set()
    for val in input_arr:
        diff = total_sum - val
        if val == diff:
            if nums_dict[val] > 1:
                result.add((val, val))
        else:
            if diff in nums_dict:
                if diff > val:
                    result.add((diff, val))
                else:
                    result.add((val, diff))
    return result

###################################################################################
### Find all combinations of two numbers that equal to sum in sorted array
###################################################################################
def find_combinations_sorted(input_arr, total_sum):
    start = 0
    end = len(input_arr) - 1
    result = []
    while start != end:
        diff = total_sum - (input_arr[end] + input_arr[start])
        if diff == 0:
            result.append((input_arr[start], input_arr[end]))
            end -= 1
        elif diff > 0:
            start += 1
        else:
            end -= 1
    return result

###########################################################################
## Interview: Implement in-order binary tree traversal without recursion
###########################################################################
def inorder_iterative_traversal(root, result = []):
    if root == None:
        return []
    stack = []
    stack.append([root, False, False])

    while stack:
        cur_node, left_checked, right_checked = stack.pop()

        if cur_node.left != None and left_checked == False:
            stack.append([cur_node, True, False])
            stack.append([cur_node.left, False, False])
            continue
        else:
            result.append(cur_node.val)
        
        if cur_node.right != None and right_checked == False:
            stack.append([cur_node.right, False, False])
    
    return result

def inorder_recursive_traversal(node, result =[]):
    if node == None:
        return []
    if node.left != None:
        inorder_recursive_traversal(node.left, result)
    result.append(node.val)
    if node.right != None:
        inorder_recursive_traversal(node.right, result)
    
    return result

###########################################################################
## Interview: Implement post-order binary tree traversal without recursion
###########################################################################
def post_order_recursive(node, result=[]):
    if node == None:
        return result
    if node.left:
        post_order_recursive(node.left, result)
    if node.right:
        post_order_recursive(node.right, result)
    result.append(node.value)

def post_order_iterative(node):
    if node == None:
        return []
    result = []
    stack = [(node, False, False)]
    while len(stack) > 0:
        cur_node, check_left, check_right = stack.pop()
        if not check_left and cur_node.left:
            stack.append((cur_node, True, check_right))
            stack.append(cur_node.left, False, False)
            continue
        if not check_right and cur_node.right:
            stack.append((cur_node, check_left, True))
            stack.append(cur_node.right(False, False))
            continue
        result.append(cur_node.val)
    return result

##########################################################################################
## Interview: Find the maximum profit you can make given a list of maximum stock prices.
#             Constraint: You must buy before you can sell
##########################################################################################
def find_max_profit(prices):
    absolute_min = prices[0]
    max_profit = 0

    for idx in range(1, len(prices)):
        absolute_min = min(absolute_min, prices[idx])
        max_profit = max(max_profit, prices[idx]-absolute_min)
    return max_profit

# input = [2, 6, 4, 18, 12, 5, 10, 1, 22]
# print(max_profit(input))

###############################################################################################
## Facebook Interview: Given a sequence of numbers and an integer total, check if a contiguous
##                     sequence adds to the integer total
###############################################################################################

def check_contiguous_sequence_sum(input, sum):
    start = 0
    end = 0
    cur_sum = input[start]

    while True:
        print(start,end, cur_sum)
        if cur_sum == sum:
            return True
        elif cur_sum > sum:
            cur_sum -= input[start]
            start += 1
            if end < start:
                end = start
                cur_sum = input[start]
            if end > len(input)-1:
                return False
        else:
            end += 1
            if end > len(input)-1:
                return False
            cur_sum += input[end]
    return False
        
arr = [6, 1, 4, 16, 2, 6, 0, 1]
total = 8
# print(check_contiguous_sequence_sum(arr, total))


##############################################################################################
## Interview: Given an array and num find and print three numbers in the array that sum to num
##############################################################################################
def find_n_nums_for_sum(num, arr, total_values=2, values={}):
    if len(values) == 0:
        for i in range(len(arr)):
            if arr[i] < num:
                values[arr[i]] = 0
    if total_values > 1:
        for key in values:
            if (num - key) in values and num - key != key:
                a = find_n_nums_for_sum(key, arr, total_values - 1)
                if a == False:
                    print(key)
                    b = find_n_nums_for_sum(num - key, arr, total_values - 1)

                    if b == False:
                        print('Couldn\'t find')
                else:
                    print(num - key)

                if values[key] < total_values - 1:
                    print(key)
                    values[key] += 1
                    print(num - key)
                    values[num - key] += 1
                    return True
    else:
        return False


# a = [1,2,3,14,22,5,6,8,10,16,12]
# find_n_nums_for_sum(30, a, 3)
# a = [[3,2,1],[1,5,6,5],[2,2,2]]
# result = min(map(sum, a))
# print(result)


#################################################################################
## Interview: Check if a string is a palindrome and if the rotation of each char
##            to end is a palindrome
#################################################################################
def is_palindrome(str):
    if len(str) == 0 or len(str) == 1:
        return True
    low = 0
    high = len(str) - 1
    while low != high and low - 1 != high:
        if str[low] != str[high]:
            return False
        low += 1
        high -= 1
    return True


# print(is_palindrome("racefcar"))


#################################################################################
## Bloomberg Interview: Check if a binary tree is a binary search tree
##                      Binary tree is where each node contains a left and right
##                      reference and a data element
##                      BST is where its a binary tree but has the property
##                      Right < Node < left (duplicates not allowed)
#################################################################################
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(node, min=float('-inf'), max=float('inf')):
    if node is None:
        return True
    if node.data <= min or node.data >= max:
        return False
    return is_bst(node.left, min, node.data) and is_bst(
        node.right, node.data, max)


# Or can do in order traversal and check if array is sorted (means BST but no duplicates)

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
# a.insert(11, a.root)
#
# print is_bst(a.root)

#################################################################################
## Interview: Given a matrix that consits of open spaces, represented by '_'
## guards represented by 0 and walls represented by -1. Return a matrix that
## has the distance from each empty space to its closest guard.

# Ex:  [['_', '_', 0 , -1],
#       [ 0 , '_', -1, '_'],
#       [ '_', '_', -1, '_']]


# Output: [[ 1,  1,  0,  -1],
#          [ 0 , 1, -1, '_'],
#          [ 1,  2, -1, '_']]
#################################################################################

from collections import deque
def compute_guard_distance_matrix(matrix):
    queue = deque()
    directions = [(0,1), (1,0), (-1,0), (0,-1)]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                queue.appendleft([(row,col), 0])
    
    while queue:
        node, distance = queue.pop()

        matrix[node[0]][node[1]] = distance

        for dir in directions:
            row = node[0] + dir[0]
            col = node[1] + dir[1]

            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                continue
            if matrix[row][col] == 0 or matrix[row][col] == -1:
                continue
            # Don't traverse backwards
            if isinstance(matrix[node[0]][node[1]], int) and distance+1 >= matrix[row][col]:
                continue

            queue.appendleft([(row,col), distance+1])

    return matrix


input = [['_', '_', 0, 0], 
         [0, '_', -1, '_'], 
         ['_', '_', -1, '_'],
         ['_', '_', -1, '_'], 
         ['_', '_', -1, '_'], 
         [0, '_', '_', '_']
         ]

# print(compute_guard_distance_matrix(input))

#################################################################################
## Interview: Given a matrix that consits of open spaces, represented by '_'
## cheese represented by 0 and walls represented by -1 and exit represented by 'E'.
# Return the shortest path available to pick up cheese and exit
#################################################################################
from collections import deque

def shortest_path_to_exit(input, start):
    path_to_cheese = compute_shortest_path(input, start, 0)
    path_to_exit = compute_shortest_path(input, (1, 0), 'E')
    return path_to_cheese + path_to_exit[1:]

def compute_shortest_path(input, start_pos, end):
    queue = deque()
    directions = [(0,1), (1,0), (-1,0), (0,-1)]

    queue.append((start_pos, [start_pos], set(start_pos)))
    shortest_path = None

    while queue:
        cur_pos, path, path_set = queue.pop()

        if input[cur_pos[0]][cur_pos[1]] == end:
            if shortest_path == None or len(path) < len(shortest_path):
                shortest_path = path
            continue

        for dir in directions:
            row = cur_pos[0] + dir[0]
            col = cur_pos[1] + dir[1]

            if row < 0 or row >= len(input) or col < 0 or col >= len(input[0]) or input[row][col] == -1:
                continue
            
            if (row,col) in path_set:
                continue

            cur_path_set = path_set.copy()
            cur_path_set.add((row,col))
            cur_path = path.copy()
            cur_path.append((row,col))

            if shortest_path != None and len(cur_path) > len(shortest_path):
                continue

            queue.appendleft(((row,col), cur_path, cur_path_set))
    return shortest_path


input = [['_', '_', '_', '_'], 
         [ 0, '_', -1, '_'], 
         [-1, -1, '_', '_'],
         ['_', '_', '_', '_'], 
         ['_', '_', '_', '_'], 
         ['_', '_', 'E', '_']
         ]
# print(shortest_path_to_exit(input, (4, 2)))

###############################################################################################
## There are a total of tasks that need to be scheduled, labeled from 0 to n.
# You are given an array tasks where tasks[i] = [ai, bi] indicates that you must
# complete task ai before you can complete bi.
#
# For example, the pair [0, 1], indicates that to complete task 0 first complete task 1.
# Return sequence of tasks that can be completed. Otherwise, return raise exception.
#
# Input: numCourses = 2, prerequisites = [[1, 0]]
# Output: [1,0]
################################################################################################

from collections import deque


def task_scheduler(n, tasks):
    tasks_id_to_children = {}
    tasks_num_parents = [0] * n

    for task in tasks:
        parent, child = task
        if parent in tasks_id_to_children:
            tasks_id_to_children[parent].append(child)
        else:
            tasks_id_to_children[parent] = [child]

        tasks_num_parents[child] += 1

    q = deque()
    for idx, value in enumerate(tasks_num_parents):
        if value == 0:
            q.append(idx)

    output = []
    print(tasks_id_to_children, tasks_num_parents)

    while len(q) > 0:
        cur_parent = q.pop()
        if cur_parent not in tasks_id_to_children:
            output.append(cur_parent)
            continue
        output.append(cur_parent)
        for child in tasks_id_to_children[cur_parent]:
            tasks_num_parents[child] -= 1
            if tasks_num_parents[child] == 0:
                q.append(child)
    if len(output) < n - 1:
        raise Exception("All tasks are not able to be completed")
    return output


# print(task_scheduler(6, [[2, 3], [2, 5], [3, 5], [1,2], [0,1]]))
# print(task_scheduler(6, [[2, 3], [2, 5], [3, 5], [1,2]]))
# print(task_scheduler(6, [[2, 3], [2, 5], [1,2]]))
# print(task_scheduler(6, [[2, 3], [2, 5], [3, 5], [5,3], [1,2]]))


###############################################################################################
###  Given an array of meeting time intervals consisting of start and end times [
### [s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.)
###############################################################################################
def find_min_conference_rooms_required(intervals):
    start_times = [] 
    end_times = []

    for interval in intervals:
        start_times.append(interval[0])
        end_times.appned(interval[1])
    
    start_times.sort()
    end_times.sort()

    max_conference_rooms = 0
    cur_meeting_rooms = 0

    start = 0
    end = 0

    while start < len(intervals)-1 or end < len(intervals):
        if start_times[start] < end_times[end] or end >= len(intervals)-1:
            start += 1
            if start != len(intervals):
                cur_meeting_rooms += 1
        else:
            if end < len(intervals):
                end += 1
                cur_meeting_rooms -= 1

        max_conference_rooms = max(max_conference_rooms, cur_meeting_rooms)


# print(min_meeting_rooms([(2, 7), (6, 7), (1, 5), (1, 3)]))

###############################################################################################
# Given a list of airport routes, return all possible routes from a start to end destination
# A ----> B
# B ----> A
# A ----> C
# C ----> A
# A ----> D
# D ----> A
# B ----> C
# C ----> B
# B ----> D
# D ----> B
# X ----> Y

# Input: [(A','B'), ('B','A'), ('A','C'), ('C','A'), ('A','D'), ('D','A'), ('B','C'), ('C','B'), ('B','D'), ('D','B'), ('X','Y')]
# start: C     dest: D
# Output:
# C,A,B,D,
# C,A,D,
# C,B,A,D,
# C,B,D,

# Time Complexity: O(N!)
###############################################################################################

class AirportRoutes:
    def __init__(self, data):
        self.routes = {}
        self.compute_routes(data)

    def compute_routes(self, data):
        for airport_start, airport_end in data:
            if airport_start not in self.routes:
                self.routes[airport_start] = []
            self.routes[airport_start].append(airport_end)
            if airport_end not in self.routes:
                self.routes[airport_end] = []
    
    def find_all_possible_routes(self, start, destination):
        result = []
        self.helper_dfs(start, destination, [start], set(start), result)
        return result
    
    def helper_dfs(self, cur_airport, destination, cur_path, visited, result):
        print(cur_path)
        if cur_airport not in self.routes:
            raise Exception("Invalid airport")

        for airport in self.routes[cur_airport]:
            new_path = cur_path+[airport]
            if airport == destination:
                result.append(new_path)
            else:
                if airport not in visited and len(self.routes[airport]) > 0:
                    new_visited = visited.copy()
                    new_visited.add(airport)
                    self.helper_dfs(airport, destination, new_path, new_visited, result)


# data = [('A','B'), ('B','A'), ('A','C'), ('C','A'), ('A','D'), ('D','A'), ('B','C'), ('C','B'), ('B','D'), ('D','B'), ('X','Y')]
# sol = AirportRoutes(data)
# print(sol.routes)
# print(sol.find_all_possible_routes('C', 'A'))

###############################################################################################
## Given a binary tree of integers, prune all the subtrees that recursively sum to zero.
##
## Example:
## Input:
##     4
##    / \
##  -3  -4
##  / \   \
## 1   2   2

## Output:
##    4
##     \
##     -4
##       \
##        2
###############################################################################################

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def prune_subtrees_with_zero_sum(root):
    if root == None:
        return None
        
    cur_root_value = root.value 

    left_subtree_sum = 0 if root.left == None else prune_subtrees_with_zero_sum(root.left)
    if left_subtree_sum == 0:
        root.left = None
    
    right_subtree_sum = 0 if root.right == None else prune_subtrees_with_zero_sum(root.right)
    if right_subtree_sum == 0:
        root.right = None
    
    total_value_at_current_root = cur_root_value + left_subtree_sum + right_subtree_sum 
    if total_value_at_current_root == 0:
        root = None
    
    return total_value_at_current_root

#left 
input2 = Node(1, None, None) # return 1
input3 = Node (2, None, None) # return 2
input1 = Node(-3, input2, input3)

#right
input5 = Node(2, None, None)
input4 = Node (-4, None, input5)

root = Node(4, input1, input4)

###############################################################################################
# Shift 3
# HELLO    --->    KHOOR

#   +3
# H -> K
# E -> H
# L -> O
# L -> O
# O -> R

# Given a list of strings, group the strings such that each string in a group is a Caesar Cipher of every other string in the group.

# Input: [ABC,BCD,JKL,DOG]
# Output:[[ABC,BCD,JKL],[DOG]]
###############################################################################################

def check_ceaser_cipher_pairs(input_arr):
    data_map = {}

    for item in input_arr:
        item_as_diff = '0'
        idx = 1
        while idx < len(item):
            print(item[idx], item[idx-1], ord(item[idx]), ord(item[idx-1]), ord(item[idx]) - ord(item[idx-1]))
            item_as_diff += str(ord(item[idx]) - ord(item[idx-1]))
            idx += 1
        
        if item_as_diff not in data_map:
            data_map[item_as_diff] = []
        data_map[item_as_diff].append(item)
    
    return data_map

# print(check_ceaser_cipher_pairs(['ABC','BCD','JKL','DOG', 'EPH', 'DOW']))


