def gcd(a, b):
    while b != 0:
        a, b = b, a % b #a%b是a除以b的余数
    return a
print(gcd(15, 12))
#扩展欧几里得算法
def exgcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, q = exgcd(b, a % b)
    x, y = y, x - a // b * y
    return x, y, q
print(exgcd(15, 12))
#得到的结果是-1 1 3，-1*15+1*12=3
#扩展欧几里得算法是为了解决不仅要求最大公约数，还要求x和y满足ax+by=gcd(a,b)的问题
#得到的x y q 分别代表什么意义呢？
#x和y是满足ax+by=gcd(a,b)的整数解，q是最大公约数