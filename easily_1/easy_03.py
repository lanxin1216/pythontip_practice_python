# 最大最小数字的差值

def difference_max_min(list_nums):
    # 将列表的第一个值赋给maxnum,minnum
    maxnum = list_nums[0]
    minnum = list_nums[0]
    # 在此处编写代码
    for num in list_nums:

        if(num > maxnum):
            maxnum = num
        elif(num < minnum):
            minnum = num

    return maxnum - minnum
# 输入整数，并将其转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(difference_max_min(numbers))