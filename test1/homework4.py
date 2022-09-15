# 1.打印乘法表

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}*{}={}'.format(j, i, j * i), end=' ')
#     print()  # print() 循环换行

# 2.根据输入行数打印图案
# i = int(input('请输入打印的行数'))
# n = 1
# for j in range(1, i + 1):
#     print(n * '*')
#     n += 2
# 思考考🤔
# list2 =[1,2,3,3,8]
# list3 = list2.copy()
# list3.remove(1)
# print(list3)
# li1 = [2, 3, 4, 4]
# li2 = [4, 4, 5, 5]
# li3 = [8, 6, 7]
# print(str(li1[2]) + str(li2[3]) + str(li3[0]))

# 3.组合数字
# list1 = [1, 2, 3, 4]
# list3 = []
# list4 = []
# for i in range(0, 4):
#     for j in range(0, 4):
#         for n in range(0, 3):
#             list2 = list1.copy()
#             list2.remove(list1[i])
#             # print(str(list2[n]))
#             list3.append(list2[n])
#             list3.append(list1[i])
#             list3.append(list1[j])
#             print(list3)
#             list4.append(list3)
#             list3.clear()
#         print()

# 4.嵌套for循环输出等边三角形

# for i in range(1, 8):
#     print((7 - i) * '@' + i * '*')

# 5. s ="123a4b5c"
# 切片新字符串”a4b“ ”2abc“
# s = "123a4b5c"
# newS = s[3:6]
# print(newS)
# newS2 = s[1::2]
# print(newS2)

# 6. li = ["alex", "WuSir", "ritian", "barry", "wenzhou"] 完成字符串操作

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li2 = []
for i in range(0, len(li)):
    if i % 2 == 0:
        li2.append(li[i])
print(li2)
li.append('seven')
print(li)
li.insert(1, "Tony")
print(li)
li[2] = "太白"
print(li)
l2 = [1, "a", 3, 4, "heart"]
for i in range(0, len(l2)):
    li.append(l2[i])
print(li)
s = "qwert"
li3 = list(s)
print(li3)

# 7.切片
li = [1, 3, 2, "a", 4, "b", 5, "c"]
l2 = li[0:3]
print(l2)
l3 = li[3:6]
print(l3)
l4 = li[0:8:2]
print(l4)
l5 = li[1:7:2]
print(l5)
l6 = li[-1:]
print(l6)
li.reverse()
print(li)
l7 = li[0:8:2]
print(l7)
