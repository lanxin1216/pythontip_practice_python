# 反转数字
def reverse_number_digits(num):
    # 在此处编写你的代码
    nums: list[int] = []

    while num > 0:
        m = num % 10
        nums.append(m)
        num = int(num / 10)

    return nums

# 获取用户输入
num = int(input())

# 调用函数
print(reverse_number_digits(num))