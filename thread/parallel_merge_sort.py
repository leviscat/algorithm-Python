import threading

# 归并函数：将两个已排序的数组合并
def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

# 归并排序函数
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # 递归处理左半部分
    right = merge_sort(arr[mid:])  # 递归处理右半部分
    return merge(left, right)

# 并行归并排序
def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # 创建两个线程来分别对左右两部分进行排序
    left_result = []
    right_result = []

    def sort_left():
        nonlocal left_result
        left_result = merge_sort(arr[:mid])

    def sort_right():
        nonlocal right_result
        right_result = merge_sort(arr[mid:])

    # 创建并启动线程
    left_thread = threading.Thread(target=sort_left)
    right_thread = threading.Thread(target=sort_right)

    left_thread.start()
    right_thread.start()

    left_thread.join()  # 等待左边的线程完成
    right_thread.join()  # 等待右边的线程完成

    # 合并左右两部分的结果
    return merge(left_result, right_result)

# 测试并行归并排序
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = parallel_merge_sort(arr)
print(f"Sorted array: {sorted_arr}")
