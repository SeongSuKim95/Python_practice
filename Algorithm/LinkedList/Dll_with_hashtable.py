class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.size = 0
        
    def append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node
        self.size += 1
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        
    def pop_left(self):
        if self.size == 0:
            return None
        node = self.head.next
        self.remove(node)
        return node
        
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [DoublyLinkedList() for _ in range(size)]
        
    def _hash_function(self, key):
        return hash(key) % self.size
        
    def put(self, key, value):
        hash_val = self._hash_function(key)
        linked_list = self.table[hash_val]
        node = linked_list.head.next
        while node is not linked_list.tail:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = Node(key=key, value=value)
        linked_list.append(new_node)
        
    def get(self, key):
        hash_val = self._hash_function(key)
        linked_list = self.table[hash_val]
        node = linked_list.head.next
        while node is not linked_list.tail:
            if node.key == key:
                return node.value
            node = node.next
        return None
        
    def remove(self, key):
        hash_val = self._hash_function(key)
        linked_list = self.table[hash_val]
        node = linked_list.head.next
        while node is not linked_list.tail:
            if node.key == key:
                linked_list.remove(node)
                return
            node = node.next
