        
class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashmap =  {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
       
    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].value
        else:
            return -1
    
        
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = Node(key, value)
        self.hashmap[key] = node
        self.insert(node)
        
        if len(self.hashmap) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]


    def remove(self, Node) -> None:
        prev, nxt = Node.prev, Node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = Node
        nxt.prev = Node
        Node.next, Node.prev = nxt, prev


