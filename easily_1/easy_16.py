# 列表乘积整除

def is_product_divisible_by_sum(numbers_list):
    # 此处编写代码
    cheng = 1
    for n in numbers_list:
        cheng = cheng * n
    if cheng % sum(numbers_list) == 0:
        return True
    else:
        return False
# 获取整数输入并将其转换为列表
numbers_list = list(map(int, input().split()))
# 调用函数打印结果
print(is_product_divisible_by_sum(numbers_list))