from NumberTheoryAlgorithms.EuclideanAlgorithm import exgcd
def mod_exp(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b = b // 2
        a = (a * a) % m
    return result
print(mod_exp(2, 3, 3))
#这个算法是快速幂取模算法，实际上是把b转换为二进制，然后根据二进制的每一位来计算结果，这样可以减少计算量
#比如2^3=2^2*2=4*2=8，这样就可以减少一次乘法运算
#这个算法的时间复杂度是O(logn)
#这个算法的应用场景是计算a^b mod m的值，其中a和b都是整数，m是一个很大的素数
#实际应用是RSA加密算法，RSA加密算法是一种非对称加密算法，它的安全性基于大整数分解的困难性
#RAS是由三个人发明的，他们分别是Rivest、Shamir和Adleman，所以叫RSA
#RSA加密算法的原理是，选择两个大素数p和q，计算n=p*q，然后计算欧拉函数φ(n)=(p-1)*(q-1)，选择一个整数e，1<e<φ(n)，且e和φ(n)互质
#计算d，使得d*e mod φ(n)=1，d称为e的模反元素
#公钥是(n,e)，私钥是(n,d)，加密算法是c=m^e mod n，解密算法是m=c^d mod n
#RSA加密算法的安全性基于大整数分解的困难性，即已知n和e，要分解n=p*q，这个问题是一个NP问题，目前没有多项式时间的解法
#RSA加密算法的缺点是速度慢，只适合加密少量数据，一般用来加密对称加密算法的密钥
#具体代码实现如下
#生成大素数的代码如下
import random
def is_prime(n, k=50):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = mod_exp(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
def generate_prime_number(n):
    while True:
        p = random.randint(2 ** (n - 1), 2 ** n - 1)
        if is_prime(p):
            return p
p = generate_prime_number(512) #生成一个512位的大素数
q = generate_prime_number(512) #生成一个512位的大素数 这两个会不会相等呢？答案是不会，因为生成的是随机数 假如相等的概率是1/2^512
n = p * q
phi = (p - 1) * (q - 1)
e = 65537 #为什么选择65537呢？因为65537是一个很大的素数，而且只有两个1，这样计算的速度会比较快 啥叫只有两个1呢？二进制表示是10000000000000001
d = exgcd(e, phi)[0] % phi #计算e的模反元素
public_key = (n, e) #公钥 这里是(n,e) 是将n和e组合成一个元组
private_key = (n, d) #私钥 这里是(n,d) 是将n和d组合成一个元组
#公钥是为了加密数据，私钥是为了解密数据
print(public_key)
print('-----------------------------')
print(private_key)
#加密和解密的代码如下
def encrypt(m, public_key):
    n, e = public_key
    return mod_exp(m, e, n)
def decrypt(c, private_key):
    n, d = private_key
    return mod_exp(c, d, n)
m = 49684198
c = encrypt(m, public_key)
print(c)
print(decrypt(c, private_key))
#RSA加密算法的安全性基于大整数分解的困难性，但是有一些方法可以破解RSA加密算法


