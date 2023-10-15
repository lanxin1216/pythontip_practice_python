# 相同的字符串

def is_string_identical(text_string):
    # 此处编写代码
    num = text_string.count(text_string[0])

    if num == len(text_string):
        return True
    else:
        return False

# 获取输入
text_string = input()
# 调用函数
print(is_string_identical(text_string))