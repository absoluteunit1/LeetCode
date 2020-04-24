def getDecimalValue(head):
        values = ""
        while head:
            values += str(head.val)
            head = head.next
        return int(values, 2)