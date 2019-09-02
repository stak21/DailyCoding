def oddEvenList(head):
    # Group together all the odd nodes followed by the even nodes
    # relative order they were in 
    # 1 2 3 4 5 6
    # 1 3 2 4 5 6
    # Steps: 
    #setup
    # odd_tail is on 1
    # even_head and tail is on 2
    # odd is even_tail next 3
    #Action
    # odd_tail next to odd next 1-> 3
    # even_tail next to odd next 2 -> 4
    # odd next to even_head 3 -> 2
    #setup
    # set odd_tail to odd
    # set even_tail to even_tail next
    # set odd to even_tail next
    # 1 3 2 4 5 6
    # 1 3 2 4 5
    # 3-> 5
    # 4 -> 6
    # 5-> 2
    # 1 3 5 2 4 6 null
    # 
    if not head:
        return head
    odd_tail = head
    even_head, even_tail = head.next, head.next
    while even_tail is not None and even_tail.next is not None:
        odd = even_tail.next
        odd_tail.next = odd
        even_tail.next = odd.next
        odd.next = even_head
        odd_tail = odd
        even_tail = even_tail.next
    return head
class Node():
    def __init__(self, n):
        self.val = n
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
oddEvenList(head)
while head is not None:
    print(head.val)
    head = head.next

    # Notes
    """ use a = b = 1 to set two variables to the same value """
        
