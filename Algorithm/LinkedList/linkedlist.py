class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def insert_after(self, prev_data, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current is not None:
                if current.data == prev_data:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next

    def print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
# 링크드 리스트 객체 생성
linked_list = LinkedList()

# 노드 추가
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# 노드 삽입
linked_list.insert_after(1, 4)

# 노드 삭제
linked_list.delete(2)

# 링크드 리스트 출력
linked_list.print()