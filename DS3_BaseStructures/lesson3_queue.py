'''
队列：是一系列有顺序的集合，新元素加入到队列的一端，这一端较叫做“队尾（rear）”，已有元素的移出发生在队列的另一端，叫做队首“froot”。当一个元素被加入队列之后，它就从队尾箱队首前进，知道它成为下一个即将被移除队列的元素
先进先出（FIFO）：最新被加入的元素处于队尾，在队列中停留最长时间的元素处于队首。
    -----------------
rear                 froot
    -----------------


    抽象数据类型（ADT）：
        Queue() :创建一个空队列对象，无序参数，返回空的队列
        enqueue(item)：将数据项目添加早队尾，无返回值
        dequeue() ：从队首移除数据项，无需参数，返回值为队首数据项。
        isEmpty()：是否队列为空，无需参数，返回值为布尔值
        size() ： 返回队列中的数据项的个数，无序参数。

    用python list实现队列
    enqueue   insert()
    dequeue     pop()

'''

'''class Queue():
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.isEmpty())
print(q.dequeue())
'''

'''
    马铃薯游戏（击鼓传花）20s中结束，物品在谁手里，谁就被淘汰。
'''
# from pythonds.basic.queue import Queue
#
# name_list = ['红','橙','黄','绿','青','蓝','紫','黑','白','灰','靛']
# num = 7
#
# def send_flower(name_list,num):
#     q = Queue()
#     for name in name_list:
#         q.enqueue(name)
#     while q.size() > 1:
#         for i in range(num):
#             q.enqueue(q.dequeue())
#         n=q.dequeue()
#         print(n)
#     return q.dequeue()
#
# send_flower(name_list,num)


'''
模拟打印机
平均每天任意一小时有大约10个学生在实验室里，在这一小时中通常每人发起2次打印任务，每个打印任务的页数从1到20也不等，实验室的打印机比较老旧，如果以草稿模式打印，每分钟可以打印10页，打印机可以转换成较高品质的打印模式，但每分钟只能打印5页。较慢的打印速度可能会使学生等待太长时间。应该采取哪种打印方式？
    学生   （等待时间+打印时间）
    打印任务  （打印任务队列）
    打印机   （状态：打印中，空闲）
    
    1-20不等，随机数模拟
    总共10*2 = 20次打印任务，平均每3分钟产生一个打印任务
    在3分钟内的任意一秒产生一个打印任务的概率是：task/180
    随机数模拟，如果产生的随机数是180，就可以认为生成了一个任务
    
    过程：
        1.创建一个打印任务队列，每个任务在生成时被赋予一个“时间戳”
        2.一个小时中的每一秒（currentSecond）都需要判断：是否有新的打印任务生成；打印机现在的状态是什么，如果打印状态是空闲并且队列不为空：
            （1）.从队列中拿出一个任务交给打印机。
            （2）.从加入打印机时间 减去 加入队列的时间 = 等待时间
            （3）.将该任务的等待时间加入到一个列表中，方便后续时候，计算总的学生打印花费时间
            （4）.基于打印的页数的随机数，求出需要多长时间打印
        3.打印机工作中，那对于打印机而言，就是工作了一秒；对于打印任务而言，离打印任务结束又近了一秒；
        4.打印任务完成，剩余时间为0，打印机进入空闲时间。
            
'''
import random
from pythonds.basic.queue import Queue


class Printer:
    def __init__(self, ppm):
        # 设置打印的速率
        self.pagerate = ppm
        self.currentTask = None
        # 打印机当前任务的剩余时间
        self.timeRemaining = 0

    # 内部任务需要的时间计算函数
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    # 切换打印机状态
    def is_busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNew(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):
    labPrinter = Printer(pagesPerMinute)
    printQueue = Queue()
    watingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labPrinter.is_busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            watingtimes.append(nexttask.waitTime(currentSecond))
            labPrinter.startNew(nexttask)

        labPrinter.tick()
    averageWait = sum(watingtimes) / len(watingtimes)
    print("平均等待时间 %6.2f secs 剩下%3d任务" % (averageWait, printQueue.size()))


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 10)

'''
学生变为20，不限时1小时内。
'''







