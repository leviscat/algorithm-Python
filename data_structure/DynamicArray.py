class DymanicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity
    def append(self, element):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.size] = element
        self.size += 1
    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    def get(self, index):
        if index < 0 or index >= self.size:
            return None
        return self.array[index]
    def __len__(self):
        return self.size
    def remove(self):
        if self.size == 0:
            return None
        self.size -= 1
        if self.size <= self.capacity // 4:
            self.shrink()
    def shrink(self):
        self.capacity //= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
# 示例
arr = DymanicArray()
arr.append(1)
arr.append(2)
arr.append(3)
print(len(arr))  # 输出 3
print(arr.get(0))  # 输出 1
# 删除最后一个元素
arr.remove()
print(len(arr))  # 输出 2
arr.remove()
print(len(arr))

