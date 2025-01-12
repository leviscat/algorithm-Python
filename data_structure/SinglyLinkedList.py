class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    #在链表的头部插入元素
    def insert_at_head(self, data):
        new_node = SinglyNode(data)
        new_node.next = self.head
        #将新节点的next指向原来的头部
        self.head = new_node
        #新节点变成了头部 逻辑是先将新节点的next指向原来的头部再将新节点变成头部
        #11行和12行的顺序不能颠倒，为什么呢？第一行的代码是将新节点的next指向原来的头部第二行的代码是将新节点变成头部，指向和赋值的顺序不能颠倒
        #如果颠倒了，那么新节点的next指向的是新节点，新节点的next指向的是原来的头部，这样就会形成一个环
    def insert_at_tail(self, data):
        new_node = SinglyNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        #last表示最后一个节点，先从头部开始，然后遍历到最后一个节点
        while last.next:
            last = last.next
        #找到最后一个节点，然后将最后一个节点的next指向新节点
        last.next = new_node
    # 删除指定元素
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    # 查找指定元素
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    # 打印链表
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()
#node的本质其实是一个对象，这个对象有两个属性，一个是data，一个是next
# 测试链表操作
if __name__ == '__main__':
    _list = SingleLinkedList()
    _list.insert_at_head(1)
    _list.insert_at_head(2)
    _list.insert_at_head(3)
    _list.insert_at_head(4)
    _list.insert_at_head(5)
    _list.insert_at_tail(6)
    _list.insert_at_tail(7)
    _list.insert_at_tail(8)
    _list.print_list()
    _list.delete(4)
    _list.print_list()
    print(_list.search(4))
