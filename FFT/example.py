import numpy as np
# 定义输入数据
x = np.array([1, 2, 3, 4])

# 使用 NumPy 的 FFT
fft_result = np.fft.fft(x)
#这个函数的作用是计算一维离散傅里叶变换。它返回一个数组，其中包含输入数组的傅里叶变换。
print("FFT Result:", fft_result)

import numpy as np


def fft_iterative(x):
    N = len(x)
    # 计算log2(N)
    logN = int(np.log2(N))

    # 计算输入数据的二进制反转
    x = np.array(x, dtype=complex)  # 确保输入是复数类型
    bit_reversed_indices = np.array([int(f'{i:0{logN}b}'[::-1], 2) for i in range(N)])
    x = x[bit_reversed_indices]

    # 执行迭代
    step = 1
    while step < N:
        for start in range(0, N, step * 2):
            for i in range(step):
                # 计算蝶形操作
                j = start + i
                k = start + i + step
                t = np.exp(-2j * np.pi * i / (2 * step)) * x[k]
                x[k] = x[j] - t
                x[j] = x[j] + t
        step *= 2
    return x


# 测试
x = np.array([1, 2, 3, 4])
fft_result = fft_iterative(x)
print("Iterative FFT Result:", fft_result)
