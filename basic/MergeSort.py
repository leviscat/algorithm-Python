# 归并排序算法的关键操作是将两个有序的数组合并成一个更大的有序数组。这个操作是通过一个辅助数组来完成的，这个辅助数组的大小和原数组相同
# MERGE(A, p, q, r)
def merge(arr, p, q, r):
    # 类型检查：确保 arr 是列表，p, q, r 是整数
    if not isinstance(arr, list):
        raise TypeError("arr should be a list")
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("arr elements should be integers or floats")
    if not (isinstance(p, int) and isinstance(q, int) and isinstance(r, int)):
        raise TypeError("p, q, r should be integers")
    n1 = q - p + 1
    n2 = r - q
    left = [0] * (n1 + 1)#creat a new array left [0]*n is a way to create a new array
    right = [0] * (n2 + 1)
    for i in range(n1):
        left[i] = arr[p + i] #将arr[p,q]赋值给left
    for j in range(n2):
        right[j] = arr[q + j + 1] #将arr[q+1,r]赋值给right
    #下面需要对n1和n2进行判断，如果n1和n2不是整数，需要对n1和n2进行取整,代码如下
    left[n1] = float('inf')
    right[n2] = float('inf')  # float('inf')表示正无穷大 为什么要加这一行代码？答案是为了防止数组越界
    #为什么会报Unexpected type(s): (str, int)错误？答案是因为left和right是数组，而不是int类型
    i = 0
    j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
    return arr
arr = [10, 11, 13, 14, 7, 8, 9]
p, q, r = 0, 3, 6  # 设置将arr[p,q]和arr[q+1,r]合并成一个有序的数组 前提是arr[p,q]和arr[q+1,r]都是有序的
merge(arr, p, q, r) #这个函数的作用是将arr[p,q]和arr[q+1,r]合并成一个有序的数组
print(arr)  # 输出合并后的结果

#分析时间复杂度是多少？答案是O(n),因为只需要遍历一次数组
#分析空间复杂度是多少？答案是O(n),因为需要一个额外的数组
#接下来把上面的代码整合到一个函数中
def merge_sort(array, p1, r1):
    if p1 < r1:
        q1 = (p1 + r1) // 2  #取整除 - 返回商的整数部分（向下取整）
        merge_sort(array, p1, q1)
        merge_sort(array, q1 + 1, r1)
        merge(array, p1, q1, r1)
    return array
#测试用例
arr = [45, 11, 74, 14, 17, 8, 9]
#图示,随着算法自底向上的推进，数组被分成越来越小的部分，直到每个部分只有一个元素，然后再将这些部分合并成一个有序的数组
#arr = [45, 11, 74, 14, 17, 8, 9]
#arr = [45, 11, 74] [14, 17, 8, 9]
#arr = [45] [11, 74] [14, 17] [8, 9]
#arr = [11, 45, 74] [14, 17] [8, 9]
#arr = [11, 45, 74] [14, 17] [8, 9]
#arr = [11, 14, 17, 45, 74] [8, 9]
#arr = [8, 9, 11, 14, 17, 45, 74]
print(merge_sort(arr, 0, len(arr)-1))  # 输出排序后的结果
#分析时间复杂度是多少？答案是O(nlogn),因为每次都是对数组进行二分
#分析空间复杂度是多少？答案是O(n),因为需要一个额外的数组
