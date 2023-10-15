# 第n小的数

def find_nth_smallest(numbers_list, n):
    # 此处编写你的代码
    # 检查 n 是否大于列表的长度
    if n > len(numbers_list):
        return None

    # 对整数列表进行排序
    numbers_list.sort()

    # 返回第n小的整数
    return numbers_list[n - 1]

# 将输入的整数转换为列表
numbers_list = list(map(int, input().split()))
# 获取n的输入
n = int(input())
# 调用函数
print(find_nth_smallest(numbers_list, n))