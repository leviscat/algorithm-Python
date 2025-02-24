def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [x for x in range(2, n + 1) if sieve[x]]
print(sieve_of_eratosthenes(100))
#上述算法得逻辑是，先把2到n的数都标记为素数，然后从2开始遍历，如果是素数，那么把它的倍数都标记为非素数，最后返回所有的素数