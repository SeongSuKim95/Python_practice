class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.prev = self.head
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = self.head
            self.head.prev = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.prev = self.head
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def remove(self, key):
        cur = self.head
        if cur and cur.data == key:
            if cur.next == self.head:
                self.head = None
            else:
                nxt = cur.next
                while nxt.next != self.head:
                    nxt = nxt.next
                nxt.next = cur.next
                self.head = cur.next
                self.head.prev = nxt
                cur = None
            return

        prev = None
        while cur.next != self.head:
            prev = cur
            cur = cur.next
            if cur.data == key:
                prev.next = cur.next
                nxt = cur.next
                nxt.prev = prev
                cur = None
                
    def __str__(self):
        res_str = ""
        cur = self.head
        while cur:
            res_str += str(cur.data) + " <-> "
            cur = cur.next
            if cur == self.head:
                break
        return res_str
