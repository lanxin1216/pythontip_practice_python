# 字符串首尾连接

def join_first_last(input_str):
    # 在此处编写你的代码
    a_str = 'az'

    b_str = a_str.replace('a', input_str[0])
    print_str = b_str.replace('z', input_str[len(input_str) - 1])

    return print_str

# 输入字符串
given_string = input()

# 调用函数
print(join_first_last(given_string))