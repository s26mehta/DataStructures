#################################################################################
# IF given a tree, you are given a value of a node and you
# have to switch its parent to the target parent from its current parent

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

# Write a function that moves a node identified by id (and its subtree)
# from one specified parent to another.
# 1. switchParents("d", "a", "b") => Success!
# 2. switchParents("d", "z", "b") => Failure!
# 3. switchParents("t", "a", "b") => Failure!
# 4. switchParents("d", "a", "z") => Failure!
# 5. switchParents("d", "a", "a") => Success!
# 6. switchParents("d", "a", "d") => Failure!
# 7. switchParents("a", "root", "d") => Failure!
# 8. switchParents("a", "root", "g") => Failure!
#################################################################################


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
