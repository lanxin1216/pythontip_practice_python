# 一个数的所有因数
def find_all_factors(num):
    # 此处写你的代码
    for n in range(1, num):
        if num%n == 0:
            
# 输入一个数字
num = int(input())

# 调用函数
print(find_all_factors(num))