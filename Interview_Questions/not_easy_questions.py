
######################################################################
#### Given a sentence without spaces and a list of words
#### find the least number of words required from the
#### list to form a sentece with spaces.
####
#### Ex:
#### sentece = s = "bedbathandbeyond"
#### dict = ["bed", "bath", "bat", "and", "hand", "bey", "beyond"]
#### result = "bed bath and beyond"
#####################################################################


def getMinWords(s, word_dict):
  if len(s) == 0:
    return 0
  words = set(word_dict)
  if s in words:
    return 1
  return recurse(s, words, {})

def recurse(s, words, memo):
  if s in memo:
    return memo[s]

  min_words = float('inf')
  cur_word = ""
  for i in range(len(s)):
    cur_word += s[i]
    if cur_word in words:
      if i == len(s)-1:
        memo[cur_word] = 1
        return 1
      else:
        result = recurse(s[i+1:], words, memo)
        memo[s[i+1:]] = result
        min_words = min(min_words, result+1)

  return min_words


s = "bedbathandbeyond"
dict = ["bed", "bath", "bat", "and", "hand", "be" , "yond", "beyond", "bedbath"]
s = "aaaaaaaa"
dict = ["aa", "a", "aaa"]
# print(getMinWords(s, dict))


###############################################################################################
# Given a string, reduce the string by removing 3 or more consecutive identical characters.
# You should greedily remove characters from left to right.
#
# Example 1:
#
# Input: "aaabbbc"
# Output: "c"
# Explanation:
# 1. Remove 3 'a': "aaabbbc" => "bbbc"
# 2. Remove 3 'b': "bbbc" => "c"
# Example 2:
#
# Input: "aabbbacd"
# Output: "cd"
# Explanation:
# 1. Remove 3 'b': "aabbbacd" => "aaacd"
# 2. Remove 3 'a': "aaacd" => "cd"
# Example 3:
#
# Input: "aabbccddeeedcba"
# Output: ""
# Explanation:
# 1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
# 2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
# 3. Remove 3 'c': "aabbcccba" => "aabbba"
# 4. Remove 3 'b': "aabbba" => "aaa"
# 5. Remove 3 'a': "aaa" => ""

###############################################################################################

def reduce_string(str):
  i = 0
  while i<len(str):
    cur_rep = 1
    j = i+1
    while j< len(str) and str[j] == str[i]:
      cur_rep += 1
      j+= 1
    if cur_rep >= 3:
      return reduce_string(str[:i]+str[i+cur_rep:])
    i += cur_rep
  return str


def reduce_string_2(input_str):
  if len(input_str) < 2:
    return input_str

  cur_char = input_str[0]
  appearances = 1
  new_str = ""

  idx = 1
  while (idx < len(input_str)):
    if input_str[idx] == cur_char:
      appearances += 1
    else:
      if appearances >= 3:
        return reduce_string_2(new_str + input_str[idx:])
      else:
        new_str += cur_char * appearances
        cur_char = input_str[idx]
        appearances = 1
    idx += 1

  return new_str if appearances >=3 else new_str + cur_char*appearances


# print(reduce_string_2('dddabbbbaccccaax'))
# print(reduce_string_2('aaabbbc'))


#########################################################
#### Given 2 integers, find the total number
#### of carry operations that exist when adding
#### them. Ex:
####            45
####           +55
#### has (5+5) = 10 (1 is carried over)
#### 4+5+1 = 10 (1 is carried over)
#### Total carry operations: 1+1 = 2
###########################################################
def numCarryOperations(num_1, num_2):
  num_1_str = str(num_1)[::-1]
  num_2_str = str(num_2)[::-1]
  diff = len(num_1_str) - len(num_2_str)
  num_carries = 0
  cur_carry = 0
  for i in range(max(len(num_1_str), len(num_2_str))):
    if i < min(len(num_1_str),len(num_2_str)):
      sum = int(num_1_str[i]) + int(num_2_str[i]) + cur_carry
    else:
      if diff > 0:
        sum = int(num_1_str[i]) + cur_carry
      else:
        sum = int(num_2_str[i]) + cur_carry
    # print(sum)
    if sum > 9:
      cur_carry = 1
      num_carries += 1
    else:
      cur_carry = 0
  return num_carries

# print(numCarryOperations(55, 65)) # 2
# print(numCarryOperations(123, 456)) # 0
# print(numCarryOperations(555, 555)) # 3
# print(numCarryOperations(900, 11)) # 0
# print(numCarryOperations(145, 55)) # 2
# print(numCarryOperations(0, 0)) # 0
# print(numCarryOperations(1, 99999)) # 5
# print(numCarryOperations(999045, 1055)) # 5
# print(numCarryOperations(101, 809)) # 1
# print(numCarryOperations(189, 209)) # 1



#########################################################
#### Given 2 lists, find the size of the largest
#### contiguous sub list that exists in both lists.
#### them. Ex:
####            [1,2,3,5,6,7,8,9]
####            [0,1,11,4,3,2,13,14,5,6,7,8]
###########################################################
def findLargestContiguous(list_1, list_2):
  longest_sequence = []
  map = {}
  for i in range(len(list_1)):
    if list_1[i] in map:
      map[list_1[i]].append(i)
    else:
      map[list_1[i]] = [i]

  i = 0
  while i < len(list_2):
    if list_2[i] in map:
      for idx in map[list_2[i]]:
        j = i
        cur_sequence = [list_2[j]]
        list_1_idx = idx
        while j+1 < len(list_2) and list_1_idx +1 < len(list_1) and list_2[j+1] == list_1[list_1_idx +1]:
          j += 1
          list_1_idx += 1
          cur_sequence.append(list_2[j])
        if len(cur_sequence) > len(longest_sequence):
          longest_sequence = cur_sequence
    i += 1
  return longest_sequence

# print(findLargestContiguous([1,2,3,5,6,7,8,9], [0,4,5,4,5,3,1,2,5,6,7,8]))




###########################################################################
#### Given a list of strings that consists of a domain or a subdomain and
## the number of hits on that domain, return a data structure of your
#### choice that provides the total number of hits for all domains and
#### subdomains. A subdomain is one that consists of prefix in an
#### existing domain.
####
# Ex:
input = [
  '900,mail.yahoo.com',
  '50,yahoo.com',
  '400,yahoo.sports.com',
  '200,news.wikipedia.com',
  '10,mail.karat.co.uk',
  '50,mail.sports',
  '70,sports.com',
  '80,wikipedia.com',
  '20,google.com',
  '10,google.co.uk'
]
###########################################################################

def findHitsPerDomain(input):
  output = {}

  for i in input:
    string_split = i.split(",")
    num_hits = int(string_split[0])
    domains = list(reversed(string_split[1].split(".")))

    cur_domain = ""
    for domain in domains:
      if cur_domain == "":
        cur_domain = domain
      else:
        cur_domain = domain+"."+cur_domain
      if cur_domain in output:
        output[cur_domain] = output[cur_domain] + num_hits
      else:
        output[cur_domain] = num_hits
  return output

a = findHitsPerDomain(input)
# print(len(a))


#################################################################################
## Bloomberg Interview:  Find the inner most nested string
##
## Input: "af[cd([a])] (a[b])]" -> a,b
## Input: "af[cd([astring])] (a[bstring])]" -> astring, bstring
## [],{},()
## -- assume that you won't get unbalanced parenthesis
##  // [([)]]
#################################################################################

def find_most_nested_string(input, open_brackets = set(['[', '(', '{']), close_brackets = set([']', ')', '}'])):
  if input == None or len(input) < 2:
    return input
  result = ()
  depth = 0
  idx = 0
  while (idx < len(input)):
    if input[idx] in open_brackets:
      depth += 1
    elif input[idx] in close_brackets:
      depth -= 1
    else:
      cur_str = input[idx]

      while (idx+1 < len(input) and input[idx+1] not in open_brackets and input[idx+1] not in close_brackets):
        idx += 1
        cur_str += input[idx]

      if result == () or result[1] < depth:
        result = (cur_str, depth)
    idx += 1
  return result[0] if result != () else ""

# print(find_most_nested_string("af[cd([ab]) (a[b])]"))
# print(find_most_nested_string("[]"))
# print(find_most_nested_string(""))
# print(find_most_nested_string("af[cd([a]) a[b]]"))
# print(find_most_nested_string("af[cd([{string}]) a[{(b-string)}]]"))
# print(find_most_nested_string("af[cd([{string}]) a[{(b-string)}]] [[[[[abecd]]]]]"))
# print(find_most_nested_string("af[cd([{a}])]"))


########################################################################################################################
## Bloomberg Interview: Given a sequence of objects, inputs, and a binary predicate, equiv(a,b) 
##                      (e.g. the equivalence relation).
##                      Write a funciton called classify(inputs, equiv) that computes a collection of sub-sequences 
##                      such that every member of each sub-sequence is equivalent to each other. That is to say, 
##                      equiv partitions inputs into a collection of equivalence classes.

## inputs = [1, 2, 3, 4, 5, 6]
## equiv = lambda a,b: a % 2 == b % 2 # congrument modulo 2
## classify(inputs, equiv)
## false = []

# >>> inputs = [1, 2, 3, 4, 5, 6]
# >>> equiv = lambda a,b: False # nothing is equivalent
# >>> classify(inputs, equiv)
# [[1], [2], [3], [4], [5], [6]]
########################################################################################################################
def classify(inputs, equiv):
    result = []

    for i in inputs:
        if len(result) == 0:
            result.append([i])
        else:
            appended = False
            for j in result:
                if equiv(i,j[0]) == True:
                    j.append(i)
                    appended = True
            if not appended:
                result.append([i])
    return result

# inputs = [1, 2, 3, 4, 5, 6]
# equiv = (lambda a,b: a % 2 == b % 2) # congrument modulo 2
# equiv = (lambda a,b: False) # congrument modulo 2
# print(classify(inputs, equiv))


#################################################################################
## Bloomberg Interview: Given a binary tree, print the right side view
#################################################################################



















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

def is_bst1(node, min=int_min, max=int_max):

    if node is None:
        return True

    if node.data < min or node.data > max:
        return False

    return is_bst(node.left, min, node.data-1) and is_bst(node.right, node.data+1, max)


def is_bst(node, min=0, max=99999999):
    if node == None:
        return True

    result_l = True
    result_r = True

    if node.left != None:
        if node.left.data >= node.data or node.left.data < min:
            result_l =  False
        else:
            result_l = is_bst(node.left, min, node.data)
    if node.right != None:
        if node.right.data <= node.data or node.right.data >= max:
            result_r = False
        else:
            result_r = is_bst(node.right, node.data, max)

    return result_l and result_r


def in_order(root):
    if root.left is not None:
        in_order(root.left)

    print(root.data)

    if root.right is not None:
        in_order(root.right)

# import ../binary_tree as bt
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
# print(is_bst(a.root))
# a.in_order(a.root)






##########################################################################################
# There are N students in a class. Some of them are friends, while some are not. Their
# friendship is transitive in nature. For example, if A is a direct friend of B, and B
# is a direct friend of C, then A is an indirect friend of C. And we defined a friend
# circle is a group of students who are direct or indirect friends.
#
# Given a N*N matrix M representing the friend relationship between students in the class.
# If M[i][j] = 1, then the ith and jth students are direct friends with each other,
# otherwise not. And you have to output the total number of friend circles among all the students.
#
# Example 1:
# Input:
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# Output: 2
# Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
# The 2nd student himself is in a friend circle. So return 2.
#
# Example 2:
# Input:
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# Output: 1
# Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
# so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
###########################################################################
def findCircleNum(M):
    connections = [-1 for i in range(len(M))]

    for i in range(len(M)):
        for j in range(i, len(M)):
            if M[i][j] == 1 and i != j:
                parent_i = find_parent(i, connections)
                parent_j = find_parent(j, connections)
                if parent_i != parent_j:
                    union(i, parent_i, j, parent_j, connections)

    num_circles = 0
    for i in connections:
        if i < 0:
            num_circles += 1

    return num_circles


def find_parent(x, connections):
    while connections[x] >= 0:
        x = connections[x]
    return x


def union(x, x_parent, y, y_parent, connections):
    if connections[x_parent] == -1 and connections[y_parent] == -1:
        connections[y] = x
        connections[x] -= 1
    elif connections[x_parent] <= connections[y_parent]:
        connections[x_parent] += connections[y_parent]
        connections[y_parent] = x_parent
        connections[y] = x_parent
    else:
        connections[y_parent] += connections[x_parent]
        connections[x_parent] = y_parent
        connections[x] = y_parent



#################################################################################
## Interview: Given a binary array, find the maximum length of a contiguous
#             subarray with equal number of 0 and 1.

# Ex:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray
#               with equal number of 0 and 1.

# Ex:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray
#              with equal number of 0 and 1.
#################################################################################
def findMaxLength(self, nums):
    h_map = {}
    max_subarray = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        if nums[i] == 1:
            count -= 1

        if count in h_map:
            max_subarray = max(max_subarray, i - h_map[count])
        else:
            h_map[count] = i
        if count == 0:
            print('hit')
            max_subarray = max(max_subarray, i + 1)

    return max_subarray
