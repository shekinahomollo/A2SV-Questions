dummy = SinglyLinkedListNode(data)
    
if head is None:
    return dummy
    
current = head
while current.next:
    current = current.next
    
current.next = dummy

return head