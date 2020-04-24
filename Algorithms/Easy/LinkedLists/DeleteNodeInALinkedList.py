# Tricky problem!

# We need to remove the current node

# 1. Change the value of the current node to the value of the next node.


# 2. Ee can remove the SecondNode, by making the current nodes "next" pointer, point to the third node. 
# CurrentNode -> SecondNode -> ThirdNode
# node.next = node.next.next
# CurrentNode -> ThirdNode

# Change the current nodes value to the value of the node we removed.

def delete(node):
    node.val = node.next.val
    node.next = node.next.next
