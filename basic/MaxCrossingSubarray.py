

def find_max_crossing_subarray(array, low, mid, high):
    left_sum = float('-inf')
    total_sum = 0
    for i in range(mid, low - 1, -1):#
        total_sum += array[i]
        if total_sum > left_sum:
            left_sum = total_sum
            max_left = i
    right_sum = float('-inf')
    total_sum = 0
    for j in range(mid + 1, high + 1):
        total_sum += array[j]
        if total_sum > right_sum:
            right_sum = total_sum
            max_right = j
    return left_sum + right_sum, max_left, max_right
def find_max_subarray(arr, low, high):
    if low == high:
        return arr[low], low, high  # 基本情况，只有一个元素

    mid = (low + high) // 2

    left_sum, left_low, left_high = find_max_subarray(arr, low, mid)  # 左边子数组
    right_sum, right_low, right_high = find_max_subarray(arr, mid + 1, high)  # 右边子数组
    cross_sum, cross_low, cross_high = find_max_crossing_subarray(arr, low, mid, high)  # 跨越中点的子数组

    # 返回最大和的子数组
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_low, left_high
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_low, right_high
    else:
        return cross_sum, cross_low, cross_high
#测试用例
arr = [13, 3,40,-5, 7, -8, -9, 10,-1, -8, 2, 4, -2, 6, -2]
low, high = 0, len(arr) - 1
max_sum, start, end = find_max_subarray(arr, low, high)
print(f"最大子数组的和: {max_sum}, 起始位置: {start}, 结束位置: {end}")