# 一个数的所有因数
def find_all_factors(num):
    nums: list[int] = []
    if num < 1:
        return nums
    else:
        for n in range(1, num+1):
            if num % n == 0:
                nums.append(n)  # 列表追加元素
    return nums
# 输入一个数字
num = int(input())

# 调用函数
print(find_all_factors(num))