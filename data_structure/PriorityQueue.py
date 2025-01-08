import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0  # 用于处理优先级相同的元素，保持插入顺序

    def push(self, item, priority):
        # 堆元素是元组 (priority, counter, item)，优先级低的元素排在前面
        heapq.heappush(self.queue, (priority, self.counter, item))
        #往堆中插入的元素是一个元组，元组的第一个元素是优先级，第二个元素是计数器，第三个元素是元素本身
        self.counter += 1

    def pop(self):
        # 返回优先级最小的元素
        if not self.is_empty():
            return heapq.heappop(self.queue)[-1]
        else:
            return None

    def peek(self):
        # 返回优先级最小的元素，但不删除它
        if not self.is_empty():
            return self.queue[0][-1]
        else:
            return None

    def is_empty(self):
        # 检查队列是否为空
        return len(self.queue) == 0


# 测试优先队列
pq = PriorityQueue()
pq.push("task1", priority=3)
pq.push("task2", priority=1)
pq.push("task3", priority=2)

print("队列中的最小优先级元素:", pq.peek())  # task2，优先级为1
print("弹出最小优先级元素:", pq.pop())  # task2
print("弹出最小优先级元素:", pq.pop())  # task3
print("弹出最小优先级元素:", pq.pop())  # task1
