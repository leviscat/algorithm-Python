def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # 1. 找到数据的最小值和最大值
    min_val = min(arr)
    max_val = max(arr)

    # 2. 确定桶的数量，桶的数量设为数组的长度
    bucket_count = len(arr)
    # 初始化桶（每个桶是一个空列表）
    buckets = [[] for _ in range(bucket_count)]

    # 3. 将数据分配到桶中
    for num in arr:
        # 计算数据分配到哪个桶
        index = int(
            (num - min_val) * (bucket_count - 1) // (max_val - min_val))  # 强制转换为整数
        buckets[index].append(num)

    # 4. 对每个桶内部进行排序
    for i in range(bucket_count):
        buckets[i] = sorted(buckets[i])  # 对每个桶使用内建的排序方法（通常是快速排序或插入排序）

    # 5. 合并所有桶中的数据
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

# 测试
arr = [0.42, 0.32, 0.23, 0.43, 0.10, 0.45, 0.31]
sorted_arr = bucket_sort(arr)
print(sorted_arr)