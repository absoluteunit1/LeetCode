# My solution
# O(n) memory. Each time I iterate over a node that I is not in my collection of prev nodes, I add to the collection. 

def hasCycle(head):
    nodes = {}                      # Create a dict object to store nodes as keys and assign a value of True if you have passed them already            
    while head:                     
        if head not in nodes:
            nodes[head] = True
            head = head.next
        else:
            return True             # If that node is in the dictionary that means that there is a cycle in the list since we are iterating over it again
    return False                    # If the list ends, that means there is no cycle. 


# This question placed no restriction on modifying the values of the nodes. This is kind of a "cheat" solution 
# O(1) memory solution
# Select an arbitrary value and iterate through the list, checking if a nodes value equals that arbitary value.


def hasCycle2(head):
    while head:
        if head.val == -10000:
            return True
        else:
            head.val = -10000
            head = head.next 
    return False



# Most optimal solution 
# Using the Tortoise and Hare algorithm for cycle detection 

# We iterate over the list one node at a time and two nodes at a time. If they are cyclic, they will eventually meet! Otherwise, if the list ends, we will have a comparisong between None and a node
#   which will cause an AttributeError
# O(1) memory solution

def hasCycle3(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except AttributeError as e:
        return False
