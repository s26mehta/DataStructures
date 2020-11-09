#################################################################################
## Interview: Output the first letter in the string that doesn't repeat
#################################################################################
def find_char(str):
    length = len(str)
    dictionary = {}
    for index in range(length):
        if str[index] in dictionary:
            dictionary[str[index]] += 1
        else:
            dictionary[str[index]] = 1

    for index in range(length):
        if dictionary[str[index]] == 1:
            return str[index]





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

root_ids = []
comments_dict = {}

def print_comments(comments_list):
  for com in comments_list:
    if com.parent_comment_id == None:
      root_ids.append(com.id)
    comments_dict[com.id] = [com, {}]

  for key,value in comments_dict.items():
    if value[0].parent_comment_id != None:
      comments_dict[value[0].parent_comment_id][1][value[0].id] = value

  for id in root_ids:
    recursive_print(comments_dict, id)
  return comments_dict

def recursive_print(dict, id, indent = 0):
  print("    "*indent + dict[id][0].text)

  if len(dict[id][1]) != None:
    for i in dict[id][1].keys():
      recursive_print(dict[id][1], i, indent+1)


def print_comments2(comments):
  parents_dict = {}
  for com_obj in comments:
    if com_obj.parent_comment_id in parents_dict:
      parents_dict[com_obj.parent_comment_id].append(com_obj)
    else:
      parents_dict[com_obj.parent_comment_id] = [com_obj]

  for com in parents_dict[None]:
    print(com.text)
    print_recursive(parents_dict, com.id)


def print_recursive(dict, id, indent=1):
  if id is None:
    return

  if id in dict:
    for com in dict[id]:
      print("    "*indent + com.text)
      print_recursive(dict, com.id, indent +1)

# a = [Comments(1, None, "test1", 1), Comments(2, 1, "test2", 1), Comments(3, 2, "test3", 1)]
# a = [Comments(1, None, "test", 1), Comments(6, 2, "kk", 1), Comments(2, 1, "random shit", 1),
#      Comments(3, 4, "pure sexy", 1) ,Comments(4, 1, "I love you", 1), Comments(5, 2, "k", 1)]
# print_comments(a)
# print(result)
# print_comments2(a)
# print(result)







#################################################################################
## Interview: Find missing num in a sorted array
#################################################################################
# O(1) time
def find_missing_num_fast(input):
    if len(input) == 0 or len(input) == input[-1]:
        return None

    total_input = sum(input)
    total_expected = (len(input)+1) * (len(input)+2)  / 2

    return int(total_expected - total_input)

# log(N) time
def find_missing_num_slow(input, start = 0):
    if len(input) == 1:
        if input[0] == 1:
            return None
        else:
            return 1

    if len(input) == 0 or len(input) == input[-1]:
        return None

    if len(input) == 2:
        if start+1 != input[0]:
            return start+1
        if start+2 != input[1]:
            return start+2

    mid = int(len(input)/2)
    if input[mid] != mid + 1 + start:
        if input[mid-1] == mid + start:
            return mid+1+start
        else:
            return find_missing_num_slow(input[:mid], start)
    else:
        return find_missing_num_slow(input[mid:], start+mid)

# r = [1,3]
# print(find_missing_num_fast(r))
# print(find_missing_num_slow(r))






#####################################################################################
## Interview: Given an array of integers find the kth largest integer. No duplicates

# Ex:  [6,10,5,7,8,3,1]

# If k == 3  ==> 7
# If k == 2  ==> 8
# If k == 6  ==> 3
#####################################################################################

def find_k_largest(arr, k):
    result = float('inf')
    for i in range(k):
        cur_largest = float('-inf')
        for item in arr:
            if item > cur_largest and item < result:
                cur_largest = item
        result = cur_largest
    return result

# print(find_k_largest([6,10,5,7,8,3,1], 6))



#####################################################################################
## Interview: Given an array of integers find the kth largest integer. Has duplicates

# Ex:  [6,10,5,7,8,3,1,10]

# If k == 3  ==> 7
# If k == 2  ==> 8
# If k == 6  ==> 3
#####################################################################################

def find_k_largest(arr, k):
    result = float('inf')
    for i in range(k):
        cur_largest = float('-inf')
        for item in arr:
            if item > cur_largest and item < result:
                cur_largest = item
        result = cur_largest
    return result

# print(find_k_largest([6,10,5,7,8,3,1], 6))




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

levels_sum = []
def printSum2(root, level=0):
    if len(levels_sum)==level:
        levels_sum.append(root.data)
    else:
        levels_sum[level] += root.data

    for child in root.children:
        printSum2(child, level+1)
    return levels_sum


h = Node(5, [])
g = Node(4, [])
f = Node(1, [])
e = Node(6, [])
d = Node(10, [h])
c = Node(5, [f,g])
b = Node(1, [e])
a = Node(3, [b,c,d])

# print(printSum2(a))
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




####################################################################
### Merge two strings
####
### Ex: 'abc' + 'defedfe'
###
### Result = 'adbecfedfe
####################################################################

def mergestr(a, b):
    diff = len(a) - len(b)

    mergestr = ""
    for i in range(max(len(a), len(b))):
        print(mergestr)
        if i < len(a) and i < len(b):
            mergestr += a[i] + b[i]
        elif diff > 0:
            mergestr += a[i]
        else:
            mergestr += b[i]
    print(mergestr)



###################################################################################
### Find all combinations of two  numbers that equal to sum in unsorted array
###################################################################################
def find_combinations(arr, total_sum):
  nums_dict = {}
  result = set()
  for i in arr:
    if i in nums_dict:
      nums_dict[i] += 1
    else:
      nums_dict[i] = 1

  for k,v in nums_dict.items():
    diff = total_sum - k

    if diff == k and v > 1:
      result.add((k,k))
    elif diff in nums_dict:
      result.add(tuple(sorted([k,diff])))

  return result


###################################################################################
### Find all combinations of two numbers that equal to sum in sorted array
###################################################################################
def find_elements1(arr, total_sum):
  i = 0
  j = len(arr) - 1
  combinations = []

  while i != j:
    if total_sum - arr[i] == arr[j]:
      combinations.append(str(arr[i]) + ',' + str(arr[j]))
    if total_sum - arr[i] > arr[j]:
      i += 1
    if total_sum - arr[i] < arr[j]:
      j -= 1


###########################################################################
## Interview: Implement in-order binary tree traversal without recursion
###########################################################################
def in_order_recurse(root, result=[]):
  if root.left != None:
    in_order_recurse(root.left, result)
  result.append(root.val)
  if root.right != None:
    in_order_recurse(root.right, result)

  return result

def in_order_iter(root):
    if root == None:
        return
    output = []
    stack = [(root, False)]

    while len(stack) > 0:
        node = stack.pop()

        if node[0].left != None and node[1] is False:
            stack.append((node[0], True))
            stack.append((node[0].left, False))
            continue
        output.append(node[0].val)

        if node[0].right != None:
          stack.append((node[0].right, False))
    return output


###########################################################################
## Interview: Implement post-order binary tree traversal without recursion
###########################################################################
def postOrderTraversal(root):
  if root == None:
    return
  stack = [(root, False, False)]
  result = []

  while len(stack) != 0:
    cur_node = stack.pop()
    if cur_node[0].left != None or cur_node[0].right != None:
      if cur_node[0].left != None and cur_node[1] is False:
        stack.append((cur_node[0], True, cur_node[2]))
        stack.append((cur_node[0].left, False, False))
        continue
      if cur_node[0].right != None and cur_node[2] is False:
        stack.append((cur_node[0], cur_node[1], True))
        stack.append((cur_node[0].right, False, False))
        continue
    result.append(cur_node[0].val)

  return result



##########################################################################################
## Interview: Find the maximum profit you can make given a list of maximum stock prices.
#             Constraint: You must buy before you can sell
##########################################################################################
def max_profit(list):
    min_num = 999999
    maximum_profit = 0

    for i in range(len(list)):
        min_num = min(list[i], min_num)
        maximum_profit = max(maximum_profit, list[i]-min_num)

    return maximum_profit

# l = [2,6,4,18,12,5,10]
# print(max_profit(l))





###############################################################################################
## Facebook Interview: Given a sequence of numbers and an integer total, check if a contiguous
##                     sequence adds to the integer total
###############################################################################################
# def total_exists(arr, sum):
#     current_total = 0
#
#     for i in range(len(arr)):
#         current_total += arr[i]
#         for j in range(i + 1, len(arr)):
#             if current_total == sum:
#                 return True
#             if current_total < sum:
#                 current_total += arr[j]
#             if current_total > sum:
#                 break
#         current_total = 0
#
#     return False

def total_exists(input_arr, sum):
    leftover_sum = sum
    start = 0

    for i in input_arr:
        if i == sum:
            return True
        leftover_sum -= i

        while (leftover_sum < 0 and start < len(input_arr)):
            leftover_sum += input_arr[start]
            start += 1
        if leftover_sum == 0:
            return True

    return False

def contiguous_combinations(arr, sum):
  total_combos_found = 0

  i = 0
  cur_sum = 0
  j = 0
  while i < len(arr)-1:
    print(cur_sum)
    if i != 0:
      cur_sum -= arr[i-1]
    else:
      cur_sum = arr[i]

    while cur_sum < sum and j < len(arr)-1:
      j += 1
      cur_sum += arr[j]

    if cur_sum == sum:
      total_combos_found += 1

    i += 1


  return total_combos_found


#[6, 1 ,2, 2, 4, 23]
# arr = [6, 2 ,4, 6, 2, 6, 0, 1]
# total = 8
# print(contiguous_combinations(arr, total))



##############################################################################################
## Interview: Given an array and num find and print three numbers in the array that sum to num
##############################################################################################
values = dict()
def find_n_nums_for_sum(num, arr, total_values=2):
    if len(values) == 0:
        for i in range(len(arr)):
            if arr[i] < num:
                values[arr[i]] = 0
    print('num: %s', num)
    #print 'dict: %s', len(values)


    if total_values > 1:
        for key in values:
            if (num-key) in values and num-key != key:
                    a = find_n_nums_for_sum(key, arr, total_values-1)
                    if a == False:
                        print(key)
                        b = find_n_nums_for_sum(num-key, arr, total_values-1)

                        if b == False:
                            print('Couldn\'t find')
                    else:
                       print(num-key)


                    if values[key] < total_values-1:
                        print(key)
                        values[key] +=1
                        print(num-key)
                        values[num-key] += 1
                        return True
    else:
        return False


# a = [1,2,3,14,22,5,6,8,10,16,12]
# find_n_nums_for_sum(30, a, 3)

# a=[[3,2,1],[1,5,6,5],[2,2,2]]
#
# result = min(map(sum, a))
# print result


##############################################################################################
## Interview: Given an array and num find and print two numbers in the array that sum to num
##############################################################################################
values = dict()
def find_nums_for_sum(num, arr):
    for i in range(len(arr)):
        if arr[i] < num:
            values[arr[i]] = 0

    for key in values:
        if (num-key) in values:
            if values[key] is not 1:
                print(key, num-key)
                values[num-key] = 1

# a = [1,2,3,14,22,5,6,8,10,16,12]
# find_nums_for_sum(30, a)



#################################################################################
## Interview: Check if a string is a palindrome and if the rotation of each char
##            to end is a palindrome
#################################################################################
import math
def is_palindrome(str):
  if len(str) == 0 or len(str) == 1:
      return True

  low = 0
  high = len(str)-1
  while low != high and low-1 != high:
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
##                      Right <= Node <= left (duplicates not allowed)
#################################################################################

class Node:
    def __init__(self, data):
        self.data = data
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


#############################################################################################
# Or can do in order traversal and check if array is sorted (means BST but no duplicates)
#############################################################################################
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
def distance_to_guard(input):
  result = []
  for i in range(len(input)):
    result.append([float('inf')]*len(input[0]))
  for i in range(len(input)):
    for j in range(len(input[0])):
      if input[i][j] == 0:
        result[i][j] = 0
      elif input[i][j] == -1:
        result[i][j] = -1
      else:
        bfs(input, (i,j), (i,j), set(), 0, result)


  return result

def bfs(input, start_pos, cur_pos, visited, distance, output):

  if input[cur_pos[0]][cur_pos[1]] == 0:
    output[start_pos[0]][start_pos[1]] = min(distance, output[start_pos[0]][start_pos[1]])
    return

  visited.add(cur_pos)

  row = cur_pos[0]
  col = cur_pos[1]

  # up
  if row > 0 and input[row-1][col] is not -1 and (row-1, col) not in visited:
    bfs(input, start_pos, (row-1, col), visited, distance+1, output)

  # left
  if col > 0 and input[row][col-1] is not -1 and (row, col-1) not in visited:
    bfs(input, start_pos, (row, col-1), visited, distance+1, output)

  # down
  if row < len(input)-1 and input[row+1][col] is not -1 and (row+1, col) not in visited:
    bfs(input, start_pos, (row+1, col), visited, distance+1, output)

  # right
  if col < len(input[0])-1 and input[row][col+1] is not -1 and (row, col+1) not in visited:
    bfs(input, start_pos, (row, col+1), visited, distance+1, output)

input = [['_', '_', 0 , 0],
         [ 0 , '_', -1, '_'],
         [ '_', '_', -1, '_'],
         ['_', '_', -1, '_'],
         ['_', '_', -1, '_'],
         [0, '_', '_', '_']]
print(distance_to_guard(input))



