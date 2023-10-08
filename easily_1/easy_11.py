# 元音字母数量
def vowel_count(string):
    # 此处写你的代码
    num = 0
    for i in string:
        if i == 'a' or i == 'o' or i == 'e' or i == 'i' or i == 'u':
            num = num + 1

    return num
# 获取输入字符串
input_string = input()
# 调用函数
print(vowel_count(input_string))