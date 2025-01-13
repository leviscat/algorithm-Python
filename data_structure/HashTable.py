class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # 初始化哈希表

    def _hash(self, key):
        return hash(key) % self.size  # 使用内置的哈希函数

    def insert(self, key, value):
        index = self._hash(key)  # 计算索引
        for item in self.table[index]:
            if item[0] == key:  # 如果键已经存在，更新值
                item[1] = value
                return
        self.table[index].append([key, value])  # 如果键不存在，插入新的键值对

    def search(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]  # 找到值并返回
        return None  # 如果键不存在，返回None

    def delete(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]  # 删除键值对
                return
        return None  # 如果键不存在，什么都不做

# 示例
hash_table = HashTable()
hash_table.insert("apple", 5)
hash_table.insert("banana", 3)

print(hash_table.search("apple"))  # 输出 5
print(hash_table.search("banana"))  # 输出 3
hash_table.delete("apple")
print(hash_table.search("apple"))  # 输出 None