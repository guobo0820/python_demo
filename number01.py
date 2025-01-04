print("hello world000")

#在进行逻辑判断时，我们需要用到条件语句，Python 提供了 if、elif、else 来进行逻辑判断。格式如下所示：
if True:
    print("hello world111")

if False:
    print("hello world222")

if False:
    print("hello world333")
else:
    print("hello world444")
    if True:
        print("hello world555")
    else:
        print("hello world666")

print("------------------------------")
# name = input()
# print('Hi',name)

print("------------------------------")
#Python 中一般以新行作为语句的结束标识，可以使用 \ 将一行语句分为多行显示。如下所示：


a = 128
b = 1024
c = 512
d = a +\
    b +\
    c
print(d)

print("hello world777")
arr = {a: 1, b: 2, c: 3}
print(arr)
print("------------------------------")
#Python 中单行注释使用 #，多行注释使用三个单引号（'''）或三个双引号（"""）。如下所示：


#单行注释

"""
多行注释
多行注释
多行注释
多行注释
"""
print("------------------------------")