# 求最大公约数
def find_gcd(a, b):
    # 在此处编写代码
    # 辗转相除法法
    while 1:
        c = a % b
        if c == 0:
            return b
        else:
            a = b
            b = c
# 输入整数
first_number = int(input())
second_number = int(input())
# 调用函数
print(find_gcd(first_number, second_number))