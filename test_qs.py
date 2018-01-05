import time

#Output the first letter in the string that doesn't repeat
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
            print(str[index])
            return str[index]

#Blackjack - Depending on the count of your current cards should you be hit again or not?
# 17 and under is hit
# above 17 is not hit
cards = {}
def decision(str):
    global cards

    if str in cards:
        cards[str] += 1
    else:
        cards[str] = 1

    card_count = 0
    ace_count = 0

    for key in cards:
        if key == 'ace':
            ace_count = cards[key]

        if key != 'ace':
            card = {
                'one' : 1,
                'two' : 2,
                'three': 3,
                'four' : 4,
                'five' : 5,
                'six' : 6,
                'seven' : 7,
                'eight' : 8,
                'nine' : 9,
                'ten' : 10,
                'jack': 10,
                'queen': 10,
                'king' : 10
            }[key]
            card_count += card

    card_count = first(ace_count, card_count)

    print("card_count: %s" % card_count)

    if card_count < 42:
        print("Hit again, card count is: %s" % card_count)
    if card_count > 41:
        print("Dont hit again, card count is: %s" % card_count)


def first(ace_count, card_count):
    print(ace_count)
    print(card_count)
    if ace_count == 0:
        return 0
    if ace_count < 5:
        if card_count > 34:
            card_count += 1
        if card_count < 35:
            card_count += 11
        ace_count -= 1
        card_count += first(ace_count, card_count)
    if ace_count > 4:
        if card_count != 34:
            card_count += first(4, card_count)
            ace_count -= 4
            card_count += ace_count
        if card_count == 34:
            card_count = card_count + ace_count
    return card_count


# decision('ace')
# print("\n")
# decision('ace')
# print("\n")
# decision('ace')
# print("\n")
# decision('four')
# print("Cards: %s \n" % cards)










# IF given a tree, you are given a value of a node and you have to switch its parent to the target parent from its current parent

# We have a tree that is stored as a list, with each node storing
# the IDs of its children, for example:

node_tree = [
    { "id": "root",  "children": [ "b", "a", "h" ] },
    { "id": "a",     "children": [ "c", "d" ] },
    { "id": "c",     "children": [ "f" ] },
    { "id": "b",     "children": [ "e" ] },
    { "id": "d",     "children": [ "g" ] },
    { "id": "e",     "children": [] },
    { "id": "f",     "children": [] },
    { "id": "g",     "children": [] },
    { "id": "h",     "children": [] },
]

# Write a function that moves a node identified by id (and its subtree) from one specified parent to another.

# 1. switchParents("d", "a", "b") => Success!

#// 2. switchParents("d", "z", "b") => Failure!

#// 3. switchParents("t", "a", "b") => Failure!

#// 4. switchParents("d", "a", "z") => Failure!

#// 5. switchParents("d", "a", "a") => Success!

#// 6. switchParents("d", "a", "d") => Failure!

#// 7. switchParents("a", "root", "d") => Failure!

#// 8. switchParents("a", "root", "g") => Failure!


# public void switchParents(string value, string initialParent, string targetParent) {
#
#   for(int x = 0; x < node_tree.size(); x++) {
#     if(node_tree.get(x).get("id").equals(initialParent)) {
#       ArrayList children = node_tree.get(x).get("children");
#       for(int y = 0; y < children.size(); y++)
#         if(children.get(y).equals(value)) {
#           children.remove(y);
#         }
#         if initalParent is children of targetParent or its targetParent.children()
#         if targetParent has initialParent as child or targetParent.children have initialParentas child
#           return "Are you stupid nigga?"
#       }
#
#     } else if(node_tree.get(x).get("id").equals(targetParent)) {
#       children.add(value);
#     }
#   }
#
#
# }

import math
def find_missing_num(array, start=0):
    length = len(array)

    if length == 2:
        if array[0] == start +1 and array[1] != start+2:
            print "Missing num is %s" % (start+2)
            return start
        else:
            print "Missing num is %s" % (start+1)
            return start

    print length
    print math.floor(length/2)
    print array[0:int(math.floor(length/2))+1]
    if math.floor(array[length/2] + start) > math.floor(length/2+1+start):
        find_missing_num(array[0:(int(math.floor(length/2)) -1 )])
    else:

        
        find_missing_num(array[int(math.floor(length/2)):(length+1)], start=(start+length/2))



r = [1,2,3,5,6,7,8]
find_missing_num(r)




