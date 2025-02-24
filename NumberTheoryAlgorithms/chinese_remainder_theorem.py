# 扩展欧几里得算法，用于求解逆元
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


# 求解逆元
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"{a} and {m} are not coprime, no inverse exists")
    return x % m


# 中国剩余定理实现
def chinese_remainder_theorem(a, n):
    """
    求解一组同余方程 x ≡ a_i (mod n_i)
    参数 a: 余数列表 [a1, a2, ..., ak]
    参数 n: 模数列表 [n1, n2, ..., nk]
    返回解 x
    """
    # 步骤 1: 计算 N = n1 * n2 * ... * nk
    N = 1
    for ni in n:
        N *= ni

    # 步骤 2: 计算每个 N_i = N / n_i
    result = 0
    for ai, ni in zip(a, n):
        # 计算 N_i
        Ni = N // ni

        # 步骤 3: 计算 N_i 关于 n_i 的逆元
        yi = mod_inverse(Ni, ni)

        # 步骤 4: 加权求和
        result += ai * Ni * yi

    # 步骤 5: 计算最终结果
    return result % N


# 示例：
a = [2, 3, 1]  # 余数列表 [x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 1 (mod 7)]
n = [3, 5, 7]  # 模数列表 [3, 5, 7]

x = chinese_remainder_theorem(a, n)
print(f"解为 x = {x}")
