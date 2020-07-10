
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

maxLength = float("-inf")

def getMinWordBreak(s, dict):
	dict = set(dict)
	memo = {}
	n = len(s)
	res = dfs(s, [], dict, memo, 0)
	return maxLength if res else 0

def dfs(s, path, dict, memo, level):
	if s in memo:
		return memo[s]
	if not s:
		maxLength = max(maxLength, level)
		return [""]
	path = []
	for word in dict:
		if s[:len(word)] != word:
			continue
		for r in dfs(s[len(word):], path, dict, memo, level + 1):
			path.append(word + (r if r == "" else " " + r) )
	memo[s] = path
	return path

s = "bedbathandbeyand"
dict = ["bed", "bath", "bat", "and", "hand", "bey", "beyond"]
# print(getMinWordBreak(s, dict))


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

# print(reduce_string('dddabbbbaccccaax'))



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

def numberOfCarryOperations(num_1, num_2):
  num_1 = str(num_1)
  num_2 = str(num_2)

  num_1_len = len(num_1)
  num_2_len = len(num_2)

  difference = abs(num_1_len - num_2_len)

  if difference != 0 and num_1_len > num_2_len:
    temp = "0"*difference
    num_2 = temp+num_2
  elif difference != 0 and num_1_len < num_2_len:
    temp = "0"*difference
    num_1 = temp+num_1

  num_1_len = len(num_1)
  num_2_len = len(num_2)

  total_carry_over = 0
  i = num_1_len-1
  cur_carry = 0
  while(i >= 0):
    total = int(num_2[i]) + int(num_1[i]) + cur_carry
    if total > 9:
      total = str(total)
      total_carry_over += int(total[0])
      cur_carry = int(total[0])
    else:
      cur_carry = 0
    i -=1
  print(total_carry_over)

# numberOfCarryOperations(55, 65) # 2
# numberOfCarryOperations(123, 456) # 0
# numberOfCarryOperations(555, 555) # 3
# numberOfCarryOperations(900, 11) # 0
# numberOfCarryOperations(145, 55) # 2
# numberOfCarryOperations(0, 0) # 0
# numberOfCarryOperations(1, 99999) # 5
# numberOfCarryOperations(999045, 1055) # 5
# numberOfCarryOperations(101, 809) # 1
# numberOfCarryOperations(189, 209) # 1



#########################################################
#### Given 2 lists, find the size of the largest
#### contiguous sub list that exists in both lists.
#### them. Ex:
####            [1,2,3,5,6,7,8,9]
####            [0,1,11,4,3,2,13,14,5,6,7,8]
###########################################################

def findlargestContiguous(user_1, user_2):
  max_count = 0
  cur_count = 0

  if len(user_1) <= len(user_2):
    for i in range(len(user_1)):
      if user_1[i] == user_2[i]:
        cur_count += 1
        max_count = max(max_count, cur_count)
      else:
        cur_count = 0
  else:
    for i in range(len(user_2)):
      if user_1[i] == user_2[i]:
        cur_count += 1
        max_count = max(max_count, cur_count)
      else:
        cur_count = 0
  print(max_count)

# findlargestContiguous([1,2,3,5,6,7,8,9], [0,4,5,4,5,3,1,2,5,6,7,8])



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

def find_most_nested_string1(input):
    open_brackets = set(['[', '(', '{'])
    close_brackets = set([']', ')', '}'])
    result = []

    max_depth = 0
    cur_depth = 0
    cur_string = ""

    for i in input:
        if i in open_brackets:
            cur_depth += 1
            cur_string = ''
            continue
        if i in close_brackets:
            if cur_depth == max_depth:
                result.append(cur_string)
            cur_depth -= 1
            cur_string = ''
            continue
        if cur_depth < max_depth:
            continue
        if cur_depth > max_depth:
            result = []
            max_depth = cur_depth
        cur_string += i

    return result

#
# print(find_most_nested_string("af[cd([ab]) (a[b])]"))
# print(find_most_nested_string("[]"))
# print(find_most_nested_string(""))
# print(find_most_nested_string("af[cd([a]) a[b]]"))
# print(find_most_nested_string("af[cd([{string}]) a[{(b-string)}]]"))
# print(find_most_nested_string("af[cd([{string}]) a[{(b-string)}]] [[[[abecd]]]]"))
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
