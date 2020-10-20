
# 作业：创建模块，模块里面创建方法，定义有参数和无数，有返回值和无返回值的情况，并说明无返回值的默认返回值。

# 有参数，有返回值
def func1(a = 1):
    return a + 1

# 有参数，无返回值
def func2(b = 1):
    b = b + 1

# 无参数,有返回值
def func3(c):
    c = c + 1

# 无参数,无返回值
if __name__ == '__main__':

    print(func1())   # 2
    print(func2())   # None
    print(func3(1))  # None