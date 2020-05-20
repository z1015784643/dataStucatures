'''
力扣 1203题
一、问题描述
    字梯问题：将单词‘FOOL’，转换成单词‘SAGE’，
    前提条件：每一步必须将一个字符转换成另一个字符

    举例：FOOL
         POOL
         POLL
         POLE
         PALE
         SALE
         SAGE
    目的：计算从FOOL到SAGE所需要的的最小转换次数
    步骤：
        1.将字之间的俄关系表示成图
        2.使用广度优先搜索的图算法来找到从开始字到结束字的而有效路径
'''

# from pythonds.graphs import Graph
# # 顶点
# def buildGraph(wordFile):
#     d = {}
#     g = Graph
#     wfile = open(wordFile,'r')
#     lines = wfile.readlines()
#     for line in lines:
#         word = line.strip('\n')
#         for i in range(len(word)):
#             bucket = word[:i] + "_" + word[i + 1:]
#             if bucket in d:
#                 d[bucket].append(word)
#             else:
#                 d[bucket] = [word]
#     for bucket in d.keys():
#         for word1 in d[bucket]:
#             for word2 in d[bucket]:
#                 if word1 != word2:
#                     g.addEdge(word1, word2)
#     return g
#
# wordFile = './word.txt'
# print(buildGraph(wordFile).getVertices())


'''
广度（宽度）优先搜索的图算法 (BFS)
    过程：
    1.给定的图G和起始顶点s,BFS算法通过探索图中的边找到G中的所有顶点，其中存在从s开始的路径。找到和s相距k的所有顶点
    然后找到距离为k+1的所有顶点
        特点：BFS先从起始顶点开始添加它的所有的子节点，然后再添加子节点的子节点
    2.怎么确定一个顶点的状态？BFS将每个顶点着色为：白色，灰色和黑色
      所有的顶点被初始化为白色，白色顶点是未发现的顶点
      当一个顶点被发现的时候，它变成灰色：灰色顶点可能还有与其相邻的一些白色顶点。
      当BFS完全探索完一个顶点的时，它就变成黑色：变成黑色意味着这个顶点已经没有与它相邻的白色顶点。
    3.使用邻接表表示法实现图，使用Queue（队列），存储顶点顺序，决定下一个探索的顶点
        BFS从起始顶点开始，颜色从灰色开始，distance=0 predecessor=None，表名这个顶点正在被探索。
        BFS的Vertex类扩展版本，中有distance（距离），predecessor（前导），color（颜色）。
        把生成的顶点放到队列中，检查队列（迭代邻接表）中前面的顶点中的颜色，如果是白色，顶点未被开发：
           （1）新的，未开发的顶点nbr，被着色为灰色；
           （2）nbr的前导被设置为当前节点currentVert
           （3）到nbr的距离设置为当currentVert + 1 的距离
           （4）nbr被添加到队列的末尾。
    
    
    
深度优先搜索的图算法
'''
from pythonds.graphs import Graph
from pythonds.basic.queue import Queue
def bsf(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size()>0):
        currentVert = vertQueue.dequeue()
    #     遍历所有的边
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')








