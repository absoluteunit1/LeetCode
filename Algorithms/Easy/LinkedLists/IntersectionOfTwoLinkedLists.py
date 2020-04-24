# My solution 

# Iterate through listA first and add each node to a dictionary
# Iterate through listB; if a node of listB is in the dictionary containing nodes of A, then it is an intersecting node and we return that node.
#   other wise if listB ends, None is returned because listA and listB do not have intersecting nodes

def getIntersection(headA, headB):
    nodesA = {}
    while headA:
        nodesA[headA] = True
        headA = headA.next
    while headB:
        if headB in nodesA:
            return headB
        else:
            headB = headB.next
    return None 

# Two pointers solution 

# Slower than the hash map approach but O(1) space complexity

# Create a pointer for each list
# Iterate through both lists simultaneously with the condition "until nodeA is nodeB".
# if the lists are of the same length, then on the first iteration we will reach their intersection or the end of both lists (None == None)
# if the lists are of diferent lengths, when we reach the end of one list, we point it to the head of the opposite list. This way, eventually they will meet.

def getIntersection(headA, headB):
    if headA and headB:
        pointA, pointB = headA, headB
        while pointA != pointB:
            pointA = pointA.next if pointA else headB
            pointB = pointB.next if pointB else headA
        return pointB