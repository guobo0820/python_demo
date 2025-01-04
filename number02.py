
print("------------------------------")
#for 循环可以遍历任何序列，比如：字符串。如下所示：
str = "hello world"
for i in str:
    print(i)
print("------------------------------")
#while 循环，满足条件时进行循环，不满足条件时退出循环。如下所示：
m = 10
while m>0:
    m-=1
    print(m)
print("------------------------------")
#continue 用在 for 循环和 while 循环语句中，用来终止本次循环。如下所示：
#break 用在 for 循环和 while 循环语句中，用来终止整个循环。如下所示：
str = "python"
for i in str:
    if i=='y':
        continue
        #break
    print(i)
print("------------------------------")
#pass 是空语句，它不做任何事情，一般用做占位语句，作用是保持程序结构的完整性。如下所示：
if False:
    pass
    print("True")
else:
    pass
    print("False")
print("------------------------------")