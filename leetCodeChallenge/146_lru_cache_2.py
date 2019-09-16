class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        
    def prepend(self, val):
        new_node = Node(val)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        self.length += 1
    
    def p(self):
        cur = self.head
        while cur and cur.next:
            print(cur.val, "->", end = " ")
            cur = cur.next
        print(cur.val)
    
    def pop(self):
        if self.head is None:
            return None
        ret_node = self.head
        if not ret_node.next:
            self.head = None
            self.length -= 1
            return ret_node.val
        self.head = self.head.next
        self.head.prev = None
        ret_node.next = None
        self.length -= 1
        return ret_node.val
        
    def remove(self, val):  
        cur = self.head
        if cur.val == val:
            self.head = cur.next
            cur.next = None
            self.length -= 1
            return cur.val
        while cur:
            if cur.val == val:
                if cur.prev:
                    cur.prev.next = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                cur.next = None
                cur.prev = None
                self.length -= 1
                return cur.val
            cur = cur.next
        print("Error: Unable to find node: {}".format(val))
        return None
    
    def peek(self):
        if self.head is None:
            return None
        return self.head.val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.lru = LinkedList()
    
    def update_lru(self, key: int) -> int:
        if key in self.hash:
            if self.lru.tail.val != key:
                move = self.lru.remove(key)
                self.lru.append(move)

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        ret_val = self.hash.get(key)
        self.update_lru(key)
        return ret_val

    def put(self, key: int, value: int) -> None:
        # check if key exists
        if key not in self.hash:
            self.hash[key] = value
            self.lru.append(key)
            storage = self.lru.length
            if storage > self.capacity:
                remove = self.lru.pop()
                del self.hash[remove]
        else:
            self.hash[key] = value
            self.update_lru(key)
