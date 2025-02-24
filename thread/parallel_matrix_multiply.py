import threading
import numpy as np

def matrix_multiply_chunk(A, B, result, row_start, row_end):
    for i in range(row_start, row_end):
        for j in range(len(B[0])):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(len(B)))

def parallel_matrix_multiply(A, B):
    rows_A = len(A)
    cols_B = len(B[0])
    result = np.zeros((rows_A, cols_B))

    num_threads = 4  # 使用4个线程
    thread_list = []
    rows_per_thread = rows_A // num_threads

    for i in range(num_threads):
        row_start = i * rows_per_thread
        row_end = (i + 1) * rows_per_thread if i != num_threads - 1 else rows_A
        thread = threading.Thread(target=matrix_multiply_chunk, args=(A, B, result, row_start, row_end))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    return result
# 测试
A = np.random.randint(0, 10, (4, 3))
B = np.random.randint(0, 10, (3, 5))
print("矩阵 A:")
print(A)
print("矩阵 B:")
print(B)
print("矩阵乘法结果:")
print(parallel_matrix_multiply(A, B))
