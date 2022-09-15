# 1. list操作

li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(len(li))
# for i in li:
#     print(i)
# li.append('seven')
# print(li)
# # 指定位置插入值
# li.insert(1, 'Tony')
# print(li)
# # 指定位置修改值
# li[1] = 'Kelly'
# print(li)
# 列表合并
# li3 = ['233', '345', 'hhhh']
# li2 = li + li3
# print(li2)
# 将字符串分别添加到列表里
# str1 = 'suprise'
# for i in str1:
#     li2.append(i)
# print(li2)
#
# li2.remove('ritian')
# print(li2)
# li2.remove(li2[1])
# print(li2)

# 删除某个区间的列表的值 由于删除操作列表顺序会发生变化 导致从小到大循环下标位置会变 所以倒叙循环删除不会改变前面排序

# for i in reversed(range(2, 5)):
#     li.remove(li[i])
# print(li)

#### 2 . lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 2. 列表操作2
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# # # 将列表中的k改为K 转换大小写K
# print(lis)
# a = str(lis)
# b = a.replace("k", "K")  # replace 是返回一个重新排序后的列表 并没有改变a的排序 所以需要重新给一个变量赋值接收
# print(b)
# c = a.replace('tt', '100')
# print(c)
# lis[3].insert(0, "火车头")
# print(lis)

# 移除两端空格 返回处理结果
# lis = "hellohjkklkl;n"
# print(lis)
# print(lis.strip())
# 切片 前闭后开
# startswith 判断字符串是否是以‘he’开头 返回 true false
# replace  替换并返回新的字符串 (new old time(替换次数))  不指定次数默认替换所有
# print((lis[3:6]) == 'he')
# print(lis.startswith('he'))
# print((lis[-2:]) ==';n')
# print(lis.replace('h','233',1))
# 切片是从[索引：索引：步长]前闭后开
# print(lis[1::3])

# 3.字典操作

dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}

dic['k4'] = 'V4'
dic['k1'] = '23333'
dic["k3"].append(18)
print(dic)

# 4.字典操作

dic1 = {
    'name': ['alex', 2, 3, 5],
    'job': 'teacher',
    'oldboy': {'alex': ['python1', 'python2', 100]}
}
dic1['name'].append('sir')
dic1['name'][0] = 'Alex'
print(dic1)
dic1['oldboy']['老男孩'] = []
print(dic1)
dic1['oldboy']['老男孩'].append('hh')
print(dic1)