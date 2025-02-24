import numpy as np
from concurrent.futures import ThreadPoolExecutor

def parallel_fft(x, num_threads=4):
    N = len(x)
    logN = int(np.log2(N))

    # 计算输入数据的二进制反转
    bit_reversed_indices = np.array([int(f'{i:0{logN}b}'[::-1], 2) for i in range(N)])
    x = np.array(x)[bit_reversed_indices]

    step = 1
    while step < N:
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            futures = []
            # 每次迭代计算step大小的蝶形操作
            for start in range(0, N, step * 2):
                for i in range(step):
                    # 提交任务给线程池，计算蝶形操作
                    futures.append(executor.submit(
                        butterfly_operation, i, start, step, x
                    ))

            # 等待线程池中的所有任务完成并更新数组
            for future in futures:
                result = future.result()
                x[result[0]] = result[1]
                x[result[0] + step] = result[2]

        step *= 2

    return x

def butterfly_operation(i, start, step, x):
    # 计算蝶形操作的两个结果
    t = np.exp(-2j * np.pi * i / (2 * step)) * x[start + i + step]
    return start + i, x[start + i] + t, x[start + i] - t

# 测试并行FFT
x = np.array([1, 2, 3, 4], dtype=complex)  # 让输入为复数
fft_result = parallel_fft(x)
print(f"FFT result: {fft_result}")
