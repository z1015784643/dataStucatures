

# def remove(num,fromPole,withPole,toPole):
#     if num >= 1:
#         remove(num-1,fromPole,withPole,toPole)
#         removeDisk(fromPole,toPole)
#         remove(num-1,withPole,toPole,fromPole)
# def removeDisk(fromPole,toPole):
#     print('移动盘子从',fromPole,'到',toPole)
#
#
# remove(5,'A','B','C')

'''
迷宫  LeetCode 1210题
1.从初识位置尝试向上走一步，以此来开始递归
2.如果上面走不通则尝试走下面，再开始递归
3.上下都不通，走左边，再开始递归
4.上下走都不通，走右边，再开始递归。

四种基本情况：
    1.碰到‘墙壁’，方格被占用无法通行
    2.方格被访问过，为避免陷入循环不在此位置继续寻找
    3.碰到边缘，表示成功
    4.四个方向探索失败，游戏失败

    turtle
    __init__  用来读取迷宫的数据，初始化迷宫内部，并找到游戏精灵的初识位置
    deaw_maze  用来在屏幕上绘制迷宫
    update_position  用来更新迷宫内的状态和游戏精灵的位置
    is_exit  用来判断当前位置是否是出口
'''
# 迷宫的地图：从txt文件中获取,地图是一个只包含 ‘+’和' '的
# turtle  GUI库绘制迷宫地图
# 用到的绘制迷宫的符号 ‘+’，空格
class Maze():
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsMaze = 0
        self.mazelist = []







