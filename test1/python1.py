# list1 = [1, 2, 3434, 3433, 3455]
# print(list1[-1])
#
# tuple1 = (i for i in range(1, 10))
# print(tuple1)
# for i in tuple1:
#     print(i)
#
# print("tuple的数据类型：", type(tuple1))

# s = "2552211135"

# def ip():
#     list1 = []
#     numb = [[], [], [], []]
#     numb1 = []
#     s =[]
#     for i in s:
#         print(i)
#         list1.append(i)
#     print(list1)
#     for i in range(4):
#         for j in range(10):
#             for n in range(3):
#                 if n % 3 == 0:
#                     while list1[j] < 3:
#                         numb1[i].append(list1[j])
#                         break
#                     numb1[i].append(list1[j])
#         numb[i].append(numb1)

# 快递信息分拣
dict1 = {}
list2 = []
list3 = []
list4 = []
list1 = [['吴天真', '北京市海淀区苏州街科技大道'], ['张*灵', '青岛市滨海区朝霞大道'], ['王胖胖', '北京市潘家园'], ['大金牙', '天津市鼓楼区高新区'], ['王瞎子', '昆明市石林'],
         ['铁三角', '青岛市滨海区朝霞大道']]
# 目标格式：{'北京市':[['吴天真', '北京市海淀区苏州街科技大道'], ['张*灵','北京市潘家园']], '青岛市':[['张*灵', '青岛市滨海区朝霞大道'], ['铁三角','青岛市滨海区朝霞大道']]}
# print(list1[0][1])
# if str in list1[0][1]:
#     print("存在")

for i in range(len(list1)):
    if '北京市' in str(list1[i][1]):
        dict1['北京市'] = list2.extend(list1[i])
    elif '青岛市' in str(list1[i][1]):
        list3 = list1[i]
        dict1['青岛市'] = list3
    else:
        list4 = list1[i]
        dict1['天津市'] = list4
print(dict1)
