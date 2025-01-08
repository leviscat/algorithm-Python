def heapify(arr, n, i):
    # 将堆中从节点i开始的子树调整为最大堆
    largest = i  # 假设当前节点是最大节点
    left = 2 * i + 1  # 左子节点索引
    right = 2 * i + 2  # 右子节点索引

    # 如果左子节点更大
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点更大
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是当前节点，则交换并继续调整
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)  # 递归调用，继续调整受影响的子树

def heap_sort(arr):
    n = len(arr)

    # 构建最大堆，从最后一个非叶子节点开始
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一个一个取出最大元素，将其放到数组末尾
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换堆顶元素与最后一个元素
        heapify(arr, i, 0)  # 重新调整堆
#这是最大堆排序算法的代码，这个算法的时间复杂度是O(nlogn),空间复杂度是O(1)
# 测试堆排序
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("排序后的数组:", arr)
