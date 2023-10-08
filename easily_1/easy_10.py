# 素数判断
def check_prime(num):
    # 在此处编写代码
    fanhui = True
    if num <= 1:
        fanhui = False
    for i in range(2, num - 1):
        if num % i == 0:
            fanhui = False
            break

    return fanhui


# 输入一个整数
number = int(input())

# 调用函数
print(check_prime(number))