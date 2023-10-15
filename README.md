# pythotip_practice_python

[课程列表-哈希编程-PythonTip学编程 (py2fun.com)](https://edu.py2fun.com/learn#/course/list)

pythontip的刷题代码（python）

刷题记录，使用python语言。

- difficulty_1为困难类型题目
- easily_1为简单类型题目
- secondary_1为中等类型题目

## 刷题目录列表：
## easily_1

- easy_01: 分秒转换
- easy_02: 字符串转换为整数
- easy_03: 最大最小数字的差值
- easy_04: 列表最后一个元素
- easy_05: 比较字符串长度
  - 使用len()得到字符串的长度，比较长度是否相等
- easy_06: 字符串首尾连接
  - 定义一个a_str = 'az'字符串，提取指定字符串中的首尾字符使用.replace()函数替换头和尾的字符。
- easy_07: 检查复数单词
- easy_08: 列表唯一的数字
  - 首先检查列表是否为空，如果是空列表则返回None,使用一个字典num_count来统计每个数字在列表中出现的次数,最后，遍历字典，找出出现次数为1的数字，即唯一的数字，并返回它。 如果没有找到唯一的数字，就返回None。
- easy_09:range转为列表
- easy_10:素数判断
  - 输入一个整数n，首先假设它是素数，然后从2到num-1遍历整数i，如果num能被i整除，说明num不是素数，将fanhui标志设为False，并跳出循环；否则，继续遍历。最后，根据fanhui的值输出判断结果。
- easy_11:元音字母数量
- easy_12:一个数的所有因数
- easy_13:反转数字
- easy_14:错位词
  - 首先移除两个输入字符串中的空格并将它们都转换为小写，以便不区分大小写和空格。然后，对这两个处理后的字符串分别进行排序，并比较它们是否相等。如果排序后相等，那么这两个字符串就是错位词，函数返回True，否则返回False。
- easy_15:相同的字符串
  - 解题思路：使用.count()统计字符串第一个字符出现的次数，比较第一个字符出现的次数是否等于字符串的长度。
- easy_16:列表乘积整除
- easy_17:第n小的数
  - 首先检查 n 是否大于整数列表的长度，如果是，就返回None，因为没有第n小的整数。然后使用sort()方法对整数列表进行排序，这将使最小的整数在列表的第一个位置。最后返回排序后的列表中的第n-1个元素