"""
-----------------------欢迎进入V2022班学生管理系统-----------------------------
请选择系统功能：
0:显示所有学员信息
1:添加一个学员信息
2:删除一个学员信息
3:修改一个学员信息
4:查询一个学员信息
exit:退出学生管理系统
"""

slist = []


#
# def show():
#     print(slist)
#
#
def adds(str):
    slist.append(str)


def delete(str):
    slist.remove(str)


def updata():
    n1 = str(input("请输入修改人的姓名："))
    n2 = str(input("请输入修改后的姓名："))
    slist[n1] = n2
    print(slist)
    return slist


# def searchs():
print("-----------------------欢迎进入V220班学生管理系统-----------------------------")
choic = input("请选择系统功能:\n0:显示所有学员信息\n1:添加一个学员信息\n2:删除一个学员信息\n3:修改一个学员信息\n4:查询一个学员信息\nexit:退出学生管理系统")
print(type(choic))
while True:
    if choic == "0":
        print(slist)
        continue
    elif choic == 1:
        name1 = str(print("请输入添加入的姓名:"))
        adds(name1)
        continue
    elif choic == 2:
        name2 = str(print("请输入添加入的姓名:"))
        delete(name2)
        continue
    elif choic == 3:
        updata()
        continue
