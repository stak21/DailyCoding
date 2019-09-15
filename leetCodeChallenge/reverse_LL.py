class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_ll(head: Node) -> Node:
    cur = head
    prev = None
    # process
    # set temp to cur.next
    # set cur to point to prev
    # set prev to cur
    # set cur to temp
    # return prev because cur will be none
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

head = Node(0)
head.next = Node(1)
head.next.next = Node(2)

head = reverse_ll(head)

while head:
    print(head.val)
    head = head.next
