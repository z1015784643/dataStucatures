# # 注册牛客网，LeetCode(必刷)
# # 如果 a+b+c=1000，并且 a^2+b^2 = c^2 ,求出所有的a,b,c的可能的组合
# import  time
# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 print('a,b,c:%d,%d,%d'%(a,b,c))
#
# end_time = time.time()
# print('运行时间为：%f'%(end_time - start_time))
# 结果
'''a,b,c:0,500,500
a,b,c:200,375,425
a,b,c:375,200,425
a,b,c:500,0,500
运行时间为：192.717984'''


# 以上方法时间太长，为了让执行时间更短，使用第二种方法

# import time
# start_time = time.time()
#
# for a in range(0,1001):
#     for b in range(0,1001):
#         c = 1000 - a - b
#         if a**2 + b**2 == c**2:
#             print('a,b,c:%d,%d,%d' % (a, b, c))
#
# end_time = time.time()
# print('运行时间为：%f'%(end_time - start_time))
'''结果：
a,b,c:0,500,500
a,b,c:200,375,425
a,b,c:375,200,425
a,b,c:500,0,500
运行时间为：1.589163
'''
# 思考，都可以从哪些角度去优化程序


'''
    1、什么是算法？
    算法是独立存在的一种解决问题的方法和思想
    2、算法的五大特性
        输入：算法具有0个或者多个输入
        输出：算法至少有1个或者多个输出
        有穷性：算法在有限的步骤之后会自动结束而且不会无限循环，并且每一个步骤可以在可接受的时间内完成。
        确定性：算法中的每一步都有确定的含义，不会出现二义性。
        可行性：算法的每一步都是可行的（每一步都能够执行有限的次数完成）,
    3、算法效率衡量
        实现算法程序的执行的时间可以反应出来算法的效率
        单纯依靠运行时间来比较算法的优劣不一定是客观准确性的（程序的运行离不开计算机环境，所以和硬件，操作系统有关）
    4、最终算法用什么去衡量？
        时间复杂度
    5、表示法： 字母大写O 来表示
        
'''

# 作业，计算前1000个正整数的和
# a=0
# for i in range(0,1001):
#     print(a,'+',i)
#     a+=i
#     print(a)


# a=0
# b=0
# while b <1001:
#     a = a+b
#     b+=1
#     print(a)


from functools import reduce
def a(x,y):
    return x+y

print(reduce(a,range(0,1001)))









