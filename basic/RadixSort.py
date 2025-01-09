def radix_sort(arr):
    RADIX = 10
    placement = 1
    max_digit = max(arr)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                arr[a] = i
                a += 1
        placement *= RADIX
    return arr
 #测试用例
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))  # 输出排序后的结果