class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.lru = []
    
    def update_lru(self, key: int) -> int:
        if key in self.lru:
            move = self.lru.pop(self.lru.index(key))
            self.lru.append(move)
        
    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        ret_val = self.hash.get(key)
        self.update_lru(key)
        return ret_val

    def put(self, key: int, value: int) -> None:
        # check if key exists
        if key not in self.lru:
            self.hash[key] = value
            self.lru.append(key)
            storage = len(self.lru)
            if storage > self.capacity:
                remove = self.lru.pop(0)
                del self.hash[remove]
        else:
            self.hash[key] = value
            self.update_lru(key)

obj = LRUCache(2)
cmds = {'get': obj.get, 'put': obj.put}
cmd = [cmds['get'], cmds['put'], cmds['get']]
opts = [1, (1, 5), 1]
for cmd, opts in zip(cmd, opts):
    if type(opts) is tuple:
        k, v = opts
        print(cmd(k, v))
    else:
        print(cmd(opts))
    

            
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

""" with an initial capacity, most likely an array to store the data in order
    For getting stuff and storing stuff using a hash is a good idea
    
    ex: (1,5)p, (3,6)p, (3)g, (4)g,(3,7)p `cap full`, (4, 1)p
    1: checks for 1 and stores 5, appending 1 to lru
    2: checks for 3 and stores 6, apprending 3 to lru
    3: grabs 3, moves the 3 to the top of the queue
        pops the first element and appends it to the end
    4: returns -1
    5: updates value at 3 and find the key in the array and move it to the top
    6: remove the bottom (lru) and add the new key to the top
    [4, 3]
    {4: 13: 7}
"""

""" 
Test case:
    [] {} max: 2
    get 1 -> -1
    put 1, 2
    get 1 -> 2
    put 1, 3
    get 1-> 3
    put 3, 4
    get 3 -> 4
    [1, 3] { 1: 3, 3: 4}
    get 1 -> 3
    [3, 1]
    put 6, 1
    [1, 6] { 1: 3, 6: 1}
    put 1,2
    [6, 1]
    put 7, 1
    [1, 7]

    
    
"""
