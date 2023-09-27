# 列表最后一个元素

def last_element(my_list):
    # 在此处编写代码
    # 通过len查询列表的长度
    length = len(my_list)

    num = my_list[length - 1]
    return num

# 获取整数输入，并将其转换为列表
input_list = list(map(int, input().split()))

# 调用函数
print(last_element(input_list))