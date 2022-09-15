# 猜数字游戏

# import random
#
#
# def guess(a):
#     b = int(input('请输入你猜的数字：'))
#     if b == a:
#         print('恭喜你 猜对啦！')
#     elif b > a:
#         print('猜大啦')
#     else:
#         print('猜小啦')
#
#
# d = random.randint(50, 366)
# c = 0
# while c < 3:
#     c += 1
#     guess(d)
# else:
#     print('机会用完啦！重新来吧! 答案是{}'.format(d))


# 简易计算器
# 逻辑运算 and or not
# 算术运算 + - * / %
# 关系运算 < <= > >= == !=

# def count(a, b, symbol):
#     if symbol == '+':
#         print(a + b)
#         return a + b
#     elif symbol == '-':
#         print(a - b)
#         return a - b
#     elif symbol == '*':
#         print(a * b)
#         return a * b
#     elif symbol == '%':
#         print(a % b)
#         return a % b


# 需要对函数的返回值操作的话  一定要加返回值！！！不然打印出来的值是不能直接操作的 ⭐⭐⭐⭐⭐

# num1 = float(input('请输入运算的第一个值:'))
# symbol1 = str(input('请输入运算符号：'))
# num2 = float(input('请输入运算的第二个值:'))
# count(num1, num2, symbol1)
# print(format("%.2f" % (count(num1, num2, symbol1))))

# 限制输出小数位
# print(round(1.23333, 2))
# print(format("%.2f" % 1.236454))


# 打工人的一天
time1 = 9
while True:
    if time1 == 9:
        print("开始打工人的一天啦！")
        time1 += 1
        continue
    elif 9 < time1 < 12:
        print('继续干活 马上休息了')
        time1 += 1
        continue
    elif 12 <= time1 <= 13:
        print('午休时间到！')
        time1 += 1
        continue
    elif 13 <= time1 <= 18:
        print('继续干活，马上吃饭了')
        time1 += 1
        continue
    elif 18 < time1 <= 22:
        print('继续干活，马上吃饭了')
        time1 += 1
        continue
    elif time1 == 22:
        print('吃饭下班！不能吃太多哦！')
        break
