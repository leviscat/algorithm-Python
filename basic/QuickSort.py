
def quicksort(arr):
    if len(arr) <= 1:  # 基本情况：数组长度为 1 或 0 时已经有序
        return arr
    pivot = arr[0]  # 选择基准元素，这里选择第一个元素
    left = [x for x in arr[1:] if x <= pivot]  # 小于等于基准元素的部分
    right = [x for x in arr[1:] if x > pivot]  # 大于基准元素的部分
    return quicksort(left) + [pivot] + quicksort(right)  # 递归排序并合并结果

# 测试用例
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("排序后的数组:", sorted_arr)

#上面的代码是快速排序算法的代码，这个算法的时间复杂度是O(nlogn),空间复杂度是O(n)
#下面是快速排序的另一种实现方式，这种实现方式是原地排序，不需要额外的空间
def partition(arr, low, high):
    pivot = arr[high]  # 选择最后一个元素作为基准
    i = low - 1  # i 是小于等于 pivot 的部分的边界
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 将 pivot 放到正确的位置
    return i + 1
#这个函数的作用是将arr[low,high]分成两部分，一部分是小于等于pivot的部分，另一部分是大于pivot的部分
def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)  # 获取基准元素的位置
        quicksort(arr, low, pi - 1)  # 排序基准元素左侧部分
        quicksort(arr, pi + 1, high)  # 排序基准元素右侧部分

# 测试用例
arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)
print("排序后的数组:", arr)
#上面的代码是快速排序算法的代码，这个算法的时间复杂度是O(nlogn),空间复杂度是O(1)