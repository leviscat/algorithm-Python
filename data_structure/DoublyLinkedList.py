class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_head(self, data):
        new_node = DoubleNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
            #如果 head 不为空，将 new_node 和 head 连接起来
        self.head = new_node
        #先将 new_node 和 head 连接起来，然后将 head 重新赋值
    def insert_at_tail(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                current.next.prev = current
                return
            current = current.next
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()