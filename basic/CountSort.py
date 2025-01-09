def counting_sort(arr):
    # 1. 找到数组中的最小值和最大值
    min_val = min(arr)
    max_val = max(arr)

    # 2. 创建计数数组
    count = [0] * (max_val - min_val + 1)

    # 3. 统计每个元素的出现次数
    for num in arr:
        count[num - min_val] += 1

    # 4. 累积计数数组
    #count[1] = count[1] + count[0]  # count[1] 表示 1 和 2 的数量
# count[2] = count[2] + count[1]  # count[2] 表示 1, 2, 3 的数量
# count[3] = count[3] + count[2]  # count[3] 表示 1, 2, 3, 4 的数量
# count[4] = count[4] + count[3]  # count[4] 表示 1, 2, 3, 4, 5 的数量
    #最后count[]的值是[1, 3, 5, 6, 6, 6, 6, 7]
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 5. 构建排序后的数组
    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        sorted_arr[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
#防止重复计数，所以count[num - min_val] -= 1
    return sorted_arr

# 测试用例
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("排序后的数组:", sorted_arr)