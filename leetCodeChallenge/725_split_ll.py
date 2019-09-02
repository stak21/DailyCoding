def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
    """ K is the number of lists
        The earlier lists will have more if extra
        if there isn't enough nodes, the rest will be null
        order should be in the order it is represented
    """
    # idea:
    # iterate through and get a count
    # then divide that by k
    # if divisible by k then
    # # the iterate through the ll first k times
    # # append to the list for each node
    # append the list to the returning list
    count = extra = 0
    counting = cur = root
    ret_list = []
    
    while counting:
        count += 1
        counting = counting.next
    members = int(count / k)

    if not members:
        members = 1
    else:
        extra = count % k    
    for section in range(k):
        ret_list.append(cur)
        for member in range(members - 1):
            if cur:
                cur = cur.next
        if extra:
            extra -= 1
            cur = cur.next
        if cur:
            temp = cur
            cur = cur.next
            temp.next = None
    return ret_list
