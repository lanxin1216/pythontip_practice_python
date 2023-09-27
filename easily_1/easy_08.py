# 列表唯一的数字
'''
首先检查列表是否为空，如果是空列表则返回None。
然后，我们使用一个字典num_count来统计每个数字在列表中出现的次数。
最后，我们遍历字典，找出出现次数为1的数字，即唯一的数字，并返回它。
如果没有找到唯一的数字，就返回None。
'''

def find_unique_number(num_list):
    # 此处编写你的代码
    length = len(num_list)

    if length == 0:
        return None
    elif length == 1:
        return num_list[0]

    num_count = {}

    for num in num_list:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    for num, count in num_count.items():
        if count == 1:
            return num

    return None
# 将输入的整数转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique_number(numbers))