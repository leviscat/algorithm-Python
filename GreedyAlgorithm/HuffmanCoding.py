import heapq

def huffman_encoding(frequencies):
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # 从堆中取出两个最小的节点
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        # 给这两个节点的编码加上前缀
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        # 将这两个节点合并为一个节点
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
print(huffman_encoding(frequencies))


# 定义树节点
class Node:
    def __init__(self, char, freq):
        self.char = char  # 字符
        self.freq = freq  # 字符的频率
        self.left = None  # 左子树
        self.right = None  # 右子树

    # 用于优先队列的比较（频率越小优先级越高）
    def __lt__(self, other):
        return self.freq < other.freq


# 构建哈夫曼树
def build_huffman_tree(char_freq):
    # 创建一个最小堆
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # 取出两个最小频率的节点
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # 创建新节点，频率是两个子节点频率之和
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # 将新节点插入堆中
        heapq.heappush(heap, merged)

    # 返回树的根节点
    return heap[0]


# 生成编码
def generate_huffman_codes(root, prefix="", codebook={}):
    if root is None:
        return codebook

    # 叶子节点，存储编码
    if root.char is not None:
        codebook[root.char] = prefix

    # 递归左子树和右子树
    generate_huffman_codes(root.left, prefix + "0", codebook)
    generate_huffman_codes(root.right, prefix + "1", codebook)

    return codebook


# 主函数
def huffman_encoding_2(char_freq):
    root = build_huffman_tree(char_freq)
    codes = generate_huffman_codes(root)
    return codes


# 示例使用
char_freq = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
codes = huffman_encoding_2(char_freq)

print("Huffman Codes:", codes)