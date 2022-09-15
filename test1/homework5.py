# 1.接收两个参数返回最大值

# def max1(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)

#
# s = str(input("请输入咔咔一h堆："))
# print(type(s))
# print(tuple(s))


# 2.获取奇数索引数值 并返回新列表
# def newlist():
#     str1 = str(input("请输入多个数值用英文逗号隔开："))
#     li1 = str1.split(",")
#     li2 = []
#     print(li1)
#     print(len(li1))
#     for i in range(0, len(li1)):
#         if i % 2 != 0:
#             li2.append(li1[i])
#     print(li2)
#
#
# newlist()


# 3. 用户输入列表是否大于5 ，是 返回前五个元素组成列表，否 返回原列表
# def returnFive():
#     lis1 = str(input("请输入多个数字用逗号隔开："))
#     lis2 = lis1.split(",")
#     if len(lis2) >= 5:
#         print(lis2[0:5])
#         return lis2[0:5]
#     else:
#         print(lis2)
#         return lis2
#
#
# returnFive()


# 4. 检查传入字符串是否包含空格 并返回结果

# def ifblank():
#     str1 = str(input("请输入内容："))
#     for i in str1:
#         if bool(i):
#             return True
#         else:
#             return False
#
#
# fun = ifblank()
# print(fun)


# 5.计算多个值的 + - * /

def count(*args):
    str1 = str(*args)
    list1 = str1.split(",")

    def add():
        print()

    def sub():
        print(a - b)

    def mul():
        print(a * b)

    def div():
        print(a / b)


print()
