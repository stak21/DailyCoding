class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """ so the digits are stored in reverse 102 -> 201
        given two LL add the two and output
        Questions:
        Can I manipulate and return one of the LL?
        I would think that the two ll can have different lengths?
        because they can be different lengths is it better to return a new LL
    """
    # 428 + 53 = 481
    # output => 184
    # 8 -> 2
    # 3 -> 5 -> 6
    # 1 -> 8
    # keep a carry variable to track numbers of 9
    # iterate through both linked lists
    #  #  add the two values together
    # .#  store the result in a new node + carry
    # .# .modulo and get the carry if any
    # # if only one of the LL is empty then add the remaining LL to the ret and return
    
    carry = 0
    l1_cur = l1
    l2_cur = l2
    while l1_cur and l2_cur:
        r = l1_cur.val + l2_cur.val + carry
        carry = int(r / 10)
        r = r % 10
        l1_cur.val = r
        if l2_cur.next and l1_cur.next is None and carry:
            while l2_cur.next and carry:
                r = l2_cur.next.val + carry
                carry = int(r /10)
                r = r % 10
                l2_cur.next.val = r
                l1_cur.next = l2_cur.next
                l2_cur = l2_cur.next
            if carry:
                l2_cur.next = ListNode(carry)
            return l1
        elif l2_cur.next and l1_cur.next is None:
            l1_cur.next = l2_cur.next
            return l1
        prev = l1_cur
        l1_cur = l1_cur.next
        l2_cur = l2_cur.next
    if carry:
        if prev.next is None:
            prev.next = ListNode(carry)
        else:
            while prev.next and carry:
                r = prev.next.val + carry
                carry = int(r /10)
                r = r % 10
                prev.next.val = r
                prev = prev.next
            if carry:
                prev.next = ListNode(carry)
    return l1

root1 = ListNode(5)
root2 = ListNode(5)
ret = addTwoNumbers(root1, root2)
while ret:
    print(ret.val)
    ret = ret.next
