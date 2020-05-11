'''
    1.哪些问题适合用递归解决
    2.怎么使用递归的方式写程序
    3.递归的三大法则（重要！！！）
    递归也是一种迭代

    一、什么是递归
        递归是一种解决问题的方法，它把一个问题分解为越来越小的子问题，直到问题的规模小到可以被很简单的直接解决。
        通常为了达到分解问题的效果，递归的过程中要引入一个***调用自身的函数***，
    二、递归的三大定律：
        1、递归算法必须有一个基本结束条件
        2、递归算法必须改变自己的状态并向基本结束条件演进
        3、递归算法必须递归地调用自身（核心）


    三、练习：
        1、使用list_sum 计算数列[2,4,6,8,10]要进行多少次递归调用

        2、计算某个数的阶乘的递归算法。(最合适的基本结束条件)，假设0！=1
        def fuck(n):
            if n == 1 or n ==0:
                return 1
            else:
                return n*fuck(n-1)

        print(fuck(5))

    四、LeetCode 第405题
        给定一个整数，编写一个算法将这个数转换成十六进制数
        对于负整数，我们通常使用补码运算方法

        给定一个整数，转成任意进制的数

    769 转换成  769
    str = "0123456789"
    769/10  = 76 余 9
    76/10   = 7  余 6
    7/10    = 0  余 7
    str[9] + str[6] + str[7]


计算[1,2,3,4,5,6,7]的和

迭代求和

def the_list(my_list):
    the_num = 0
    for num in my_list:
        the_num = the_num + num
    return the_num

    print(the_list([1,2,3,4,5,6,7]))

    不用循环求和 ----》  递归
def the_list(my_list):
    # 函数结束运行的辟谣条件，否则就是一个死循环。

    if len(my_list) == 1 :
        # print('长度=1的时候',my_list[0])
        return my_list[0]
    else:
        print('列表：', my_list)
        print(my_list[0],'+',the_list(my_list[1:]) ,'==',my_list[0] + the_list(my_list[1:]))

        return my_list[0] + the_list(my_list[1:])

print(the_list([1,2,3,4,5,6,7]))
'''
# def to_str(num,base):
#     con_str = '0123456789ABCDEF'
#     if num < base:
#         return con_str[num]
#     else:
#         return to_str(num//base,base) + con_str[num % base]
#
# print(to_str(967,10))
# print(to_str(769,2))
# print(to_str(769,8))
# print(to_str(769,16))

from pythonds.basic.stack import Stack

s = Stack()

def to_str(num,base):
    str = '0123456789ABCDEF'
    while num > 0 :
        if num < base:
            s.push(str[num])
        else:
            s.push(str[num%base])
        num = num // base

    result = ''
    while not s.isEmpty():
        result = result + s.pop()
    return result

print(to_str(8,16))









