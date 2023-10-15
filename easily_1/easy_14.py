# 错位词

def are_anagrams(string1, string2):
    # 此处编写代码
    # 移除字符串中的空格并将字符都转换为小写
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()

    # 如果两个字符串排序后相等，它们是错位词
    return sorted(string1) == sorted(string2)

# 获取输入string1 和 string2
string1 = input()
string2 = input()
# 调用函数并打印结果
print(are_anagrams(string1, string2))