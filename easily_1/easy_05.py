# 比较字符串长度

def compare_length(str1, str2):
    # 此处编写你的代码
    length1 = len(str1)
    length2 = len(str2)

    if length1 == length2:
        return True
    else:
        return False

# 获取输入
input_str1 = input()
input_str2 = input()

# 调用函数
print(compare_length(input_str1, input_str2))