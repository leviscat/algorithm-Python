import random
from sympy import isprime


# 生成大质数
def generate_prime(bits):
    while True:
        # 生成一个指定位数的随机奇数
        num = random.getrandbits(bits) | (1 << bits - 1) | 1
        if isprime(num):
            return num


# 扩展欧几里得算法，求逆元
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


# 求逆元 是指对于给定的整数a和模数m，求一个整数b，使得a*b ≡ 1 (mod m) 目的是为了求解同余方程 a*x ≡ b (mod m)
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"{a} and {m} are not coprime, no inverse exists")
    return x % m


# 生成 RSA 密钥对
def generate_rsa_keys(bits=512):
    # 选择两个大质数 p 和 q
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)

    # 计算 n 和 φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # 选择 e，通常选择 65537
    e = 65537
    gcd, x, y = extended_gcd(e, phi_n)

    # 计算 d，使得 e * d ≡ 1 (mod φ(n))
    d = mod_inverse(e, phi_n)

    # 公钥 (e, n)，私钥 (d, n)
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


# 公钥加密
def encrypt(plain_text, public_key):
    e, n = public_key
    # 将明文转换为整数（假设明文每个字符都是一个整数）
    plain_int = int.from_bytes(plain_text.encode('utf-8'), 'big')
    # 加密公式 c = m^e % n
    cipher_int = pow(plain_int, e, n)
    return cipher_int


# 私钥解密
def decrypt(cipher_int, private_key):
    d, n = private_key
    # 解密公式 m = c^d % n
    plain_int = pow(cipher_int, d, n)
    # 将解密后的整数转换为字符串
    plain_text = plain_int.to_bytes((plain_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return plain_text


# 示例：生成密钥对，进行加密解密操作
public_key, private_key = generate_rsa_keys(bits=512)
message = "Hello, RSA!"

print("公钥:", public_key)
print("私钥:", private_key)

# 加密
cipher_text = encrypt(message, public_key)
print("密文:", cipher_text)

# 解密
decrypted_message = decrypt(cipher_text, private_key)
print("解密后的消息:", decrypted_message)
