###################################################################################################
## Dropbox Interview: Output a list of lists that has the duplicates files in a path
##                    hierachy. The content is what makes the files duplicates not the
##                    file names. (Generate md4/md5 hash but to double check if the files
##                    are duplicates you can hash again.)
##                    If two files have same size and same hash code, they are probably equal.
##                    But there will still be a little chance these two files are different
##                   (except if file size is less than hash code size).
###################################################################################################

import os
import hashlib

values = dict()
duplicates = []
og_path = []
def get_duplicates(path):
    if len(og_path) == 0:
        og_path.append(path)

    for name in os.listdir(path):
        if os.path.isdir(name):
            get_duplicates(os.path.abspath(name))

        if os.path.isfile(name):
            hash = md5(name)
            if hash in values:
                values[hash].append(os.path.abspath(name))
            else:
                values[hash] = [os.path.abspath(name)]

    if path == og_path[0]:
        output_duplicates()

def output_duplicates():
    for key in values:
        if len(values[key])> 1:
            duplicates.append(values[key])

    print duplicates


def md5(name):
    hash_md5 = hashlib.md5()
    with open(name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# get_duplicates(os.getcwd())


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
## Interview: Check if a string is a palindrome and if the rotation of each char
##            to end is a palindrome
#################################################################################
import math
def is_palindrome(str):
    if len(str) == 0 or len(str) == 1:
        return True
    else:
        end = len(str)-1
        for i in range(len(str)-1):
            if str[i] != str[end]:
                return False

            if len(str) % 2 == 0 and end == ((len(str)/2)+1):
                break
            if len(str) % 2 != 0 and end == i:
                break
            end = end-1

        return True
# print is_palindrome("racecar")



#################################################################################
## Interview: Convert linked list to binary tree
#################################################################################










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
                print (key, num-key)
                values[num-key] = 1

# a = [1,2,3,14,22,5,6,8,10,16,12]
# find_nums_for_sum(30, a)


##############################################################################################
## Interview: Given an array and num find and print three numbers in the array that sum to num
##############################################################################################
values = dict()
def find_n_nums_for_sum(num, arr, total_values=2):
    if len(values) == 0:
        for i in range(len(arr)):
            if arr[i] < num:
                values[arr[i]] = 0
    print 'num: %s', num
    #print 'dict: %s', len(values)


    if total_values > 1:
        for key in values:
            if (num-key) in values and num-key != key:
                    a = find_n_nums_for_sum(key, arr, total_values-1)
                    if a == False:
                        print key
                        b = find_n_nums_for_sum(num-key, arr, total_values-1)

                        if b == False:
                            print 'Couldn\'t find'
                    else:
                       print num-key


                    if values[key] < total_values-1:
                        print key
                        values[key] +=1
                        print num-key
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


###############################################################################################
## Facebook Interview: Given a sequence of numbers and an integer total, check if a contiguous
##                     sequence adds to the integer total
###############################################################################################
def total_exists(arr, sum):
    current_total = 0

    for i in range(len(arr)):
        current_total += arr[i]
        for j in range(i + 1, len(arr)):
            if current_total == sum:
                return True
            if current_total < sum:
                current_total += arr[j]
            if current_total > sum:
                break
        current_total = 0

    return False

#[6, 1 ,2, 2, 4, 23]
#arr = [6, 0 ,1, 2, 4, 23]
#total = 8
# print total_exists(arr, total)


##############################################################################################
## Interview: Find the maximum sum path in a pyramid, given the pyramid as a list of lists
##############################################################################################
def maximum_sum_path(pyramid):

    while len(pyramid) != 1:
        row = []
        second_last = len(pyramid) - 2
        last = len(pyramid)-1
        for i in range(second_last):
            row.append(max(pyramid[second_last][i] + pyramid[last][i], pyramid[second_last][i] + pyramid[last][i+1]))

        del row[-1]
        del row[-1]

        pyramid.append(row)

    return pyramid[0][0]



#################################################################
## Interview: Implement binary tree traversal without recursion
#################################################################
def binary_tree_traversal(root):
    if root is None:
        return None

    stack = [root]

    while len(stack) != 0:
        print stack[0]

        pop = stack[0]

        del stack[0]

        if pop.right is not None:
            stack.insert(0,root.right)
        if pop.left is not None:
            stack.insert(0, root.left)



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

l = [2,6,4,18,12,5,10]
print(max_profit(l))

