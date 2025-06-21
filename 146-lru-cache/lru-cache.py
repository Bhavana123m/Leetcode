class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0) 
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev  = self.head
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert_start(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert_start(node)
            return node.value
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert_start(node)
            return
        elif len(self.cache) >= self.capacity:
            node = self.tail.prev
            self.remove(node)
            self.cache.pop(node.key)   # del self.cache[lru.key]
        newNode = Node(key, value)
        self.insert_start(newNode)
        self.cache[key] = newNode
        


