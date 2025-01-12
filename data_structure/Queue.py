class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
        #insert函数是在指定位置插入元素，第一个参数是位置，第二个参数是元素
        #为什么要在第一个位置插入元素呢？因为这样可以保证队列的先进先出
        #后面的元素会被挤到后面

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)