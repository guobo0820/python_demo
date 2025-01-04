#除了上面的基本运算外，我还可以借助数学模块 math 实现更多的运算。
import math
#我的基本运算见下表，整型和浮点型均支持下表中运算。
x = 10
y = 30
z = -100
v = -1.6
print("------------------------------")
#x 和 y 的和
print(x+y)
print("------------------------------")
#x 和 y 的差
print(x-y)
print("------------------------------")
#x 和 y 的乘积
print(x*y)
print("------------------------------")
#x 和 y 的商
print(x/y)
print("------------------------------")
#x 除以 y，取整除
print(x//y)
print("------------------------------")
#x 除以 y，取模
print(x%y)
print("------------------------------")
#x 取反
print(-x)
print("------------------------------")
#x 不变
print(+x)
print("------------------------------")
#x 的绝对值
print(abs(z))
print("------------------------------")
#将 x 转换为整数
print(int(v))
print("------------------------------")
#将 x 转换为浮点数
print(float(x))
print("------------------------------")
#一个带有实部 x 和虚部 y 的复数，y 默认为 0。
print(complex(x,y))
print("------------------------------")
#(x // y, x % y)
print(divmod(x,y))
print("------------------------------")
#x 的 y 次幂
print(pow(x,y))
print("------------------------------")
#x 的 y 次幂
print(x**y)
print("------------------------------")
#除了上面的基本运算外，我还可以借助数学模块 math 实现更多的运算。

print("------------------------------")
#返回 x 的平方根
print(math.sqrt(1024))
print("------------------------------")
#返回 x 的绝对值
print(math.fabs(-100))
print("------------------------------")
#返回 x 的上入整数，如：math.ceil(1.1) 返回 2
print(math.ceil(1.1))
print("------------------------------")
#返回 x 的下舍整数，如：math.floor(1.1) 返回 1
print(math.floor(1.1))
print("------------------------------")
#返回 e 的 x 次幂
print(math.exp(1))
print("------------------------------")
#返回以 e 为底 x 的对数
print(math.log(1))
print("------------------------------")
#返回以 10 为底 x 的对数
print(math.log10(1))
print("------------------------------")
#返回 x 的 y 次幂
print(math.pow(10,3))
print("------------------------------")
#返回 x 的平方根
print(math.sqrt(30))
print("------------------------------")
print(math.factorial(3))
print("------------------------------")
print("------------------------------")
print("------------------------------")
print("------------------------------")
#在安全领域有时会用到随机数，random 模块对随机数的生成提供了支持。
import random

random.seed(1)
print("------------------------------")
print(random.random())
print("------------------------------")
print(random.uniform(1,10))
print("------------------------------")
print(random.randint(0,10))
print("------------------------------")
print(random.choice([1,2,3,4,5]))
print("------------------------------")
print(random.Random().random())
print("------------------------------")