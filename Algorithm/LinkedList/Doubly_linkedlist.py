class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = self.Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.prev = cur_node

    def delete_at_front(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return data

    def delete_at_end(self):
        if not self.head:
            return None
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        if cur_node.prev:
            cur_node.prev.next = None
        else:
            self.head = None
        return cur_node.data

    def insert_at_index(self, index, data):
        if index < 0:
            raise IndexError("Index out of range")
        if index == 0:
            self.insert_at_front(data)
            return
        new_node = self.Node(data)
        cur_node = self.head
        for i in range(index):
            if not cur_node:
                raise IndexError("Index out of range")
            cur_node = cur_node.next
        new_node.prev = cur_node.prev
        new_node.next = cur_node
        cur_node.prev.next = new_node
        cur_node.prev = new_node

    def display(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print()

    def remove_at_index(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Invalid index")
        if index == 0:
            self.remove_first()
        elif index == self.size - 1:
            self.remove_last()
        else:
            current = self.head
            for i in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1

# 이중 연결 리스트 생성
dll = DoublyLinkedList()

# 맨 앞에 노드 추가
dll.insert_at_front(3)
dll.insert_at_front(2)
dll.insert_at_front(1)
dll.display()  # 출력: 1 2 3

# 맨 뒤에 노드 추가
dll.insert_at_end(4)
dll.insert_at_end(5)
dll.display()  # 출력: 1 2 3 4 5

# 맨 앞에서 노드 삭제
dll.delete_at_front()
dll.delete_at_front()
dll.display()  # 출력: 3 4 5

# 맨 뒤에서 노드 삭제
dll.delete_at_end()
dll.display()  # 출력: 3 4

my_list = DoublyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

# 인덱스 1에 있는 노드(값 20)를 제거
my_list.remove_at_index(1)

# 출력: 10 -> 30
my_list.print_list()