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
        假设计算机执行算法每个基本操作的时间是固定的一个时间单位，那么有多少个基本操作，就代表会花费多少时间单位。虽然对于不同的机器环境而言，确切的时间单位是不同的，但是对于算法进行多少个基本操作在规模数量级上是相同的。因此，我们可忽略机器环境的影响，而客观的反应算法的时间效率。
        对于算法的时间效率，用'O'表示。
        O(n^3)
        O(n^2)
    6、时间复杂度分类
        最优时间复杂度：算法完成工作最少需要多少基本操作（过于理想化，没有什么参考价值）
        最坏时间复杂度：算法完成工作最多需要多少基本操作（提供了一种保证，表明算法在此程度的基本操作中一定能完成工作）
        平均时间复杂度：算法完成工作平均需要多少基本操作（对算法整体一个全面的评价，但是这种衡量方式没有保证。）
        我们关注算法的最坏情况。————>最坏时间复杂度
    7、时间复杂度的几条基本计算规则
        基本操作：也就是说只有常数项，认为其时间复杂度为O（1）
        顺序结构，时间复杂度按照加法进行计算
        循环结构，时间复杂度按照乘法进行计算
        分支：取最大值。
        判断一个算法的效率时，只需要关注操作数量的最高此项，其他次要项和常数项可以忽略
        没有特殊情况下，我们分析的都是最坏时间复杂度。
    8、练习
        12  ————》  O(1)
        2n+3  ————》O(n)
        3n^2 + 2n +1   ————》 O(n^2)
        5log2n + 20   ————》 O(logn)
        2n + 5nlogn + 20   ————》 O(nlogn)
        100000n^2 + 2*n^3 + 4 ————》 O(n^3)
        2^n  ————》 O(2^n) 
        
        O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)
    
    9、练习
        

    
        
'''
import time
# 作业，计算前1000个正整数的和
# a=0
# for i in range(0,1001):
#     print(a,'+',i)
#     a+=i
#     print(a)

# start_time = time.time()
# a=0
# b=0
# while b <1001:
#     a = a+b
#     b+=1
#     print(a)
# end_time = time.time()
# sun_time = end_time-start_time
#
# print('所需时间：',sun_time)


# from functools import reduce
# def sum(x,y):
#     return x+y
# print(reduce(sum,range(0,1001)))

'''
练习：求出列表中的最小值。
要求:
    函数1：O(n^2)   两两比较
    函数2：O(n)    设置一个临时变量，更优化的算法就是把这个临时变量设置成列表中的第一个元素
'''
a=[156,15,16,0,1,2,3,4,456]

def get_min1(a):
    print(a)
    for i in range(len(a)):
        for j in range(len(a)):
            a1 = a[i]
            print(a1,'数字1')
            a2 = a[j]
            print(a2,'数字2')
            if a1 > a2:
                break
        return a
print(get_min1(a))












