'''
力扣第912题，
冒泡排序法：
def bubbleSort(alist):
    for passnum in range(len(nums)-1,0,-1):
        for i in range(passnum):
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
nums = [5,2,3,1]
bubbleSort(nums)
print(nums)

#选择排序
def seletcSort(alist):
    for fillslot in range(len(nums)-1,0,-1):
        positionMax = 0
        for location in range(1,fillslot+1):
            if nums[location] > nums[positionMax]:
                positionMax = location
        temp = nums[fillslot]
        nums[fillslot] = nums[positionMax]
        nums[positionMax] = temp

nums = [5,2,3,1,0]
seletcSort(nums)
print(nums)


[54, 26, 93, 17, 77, 31, 44, 55, 20]
一、冒泡排序: 对一个列表多次遍历，比较相邻的两项，并且交换顺序排错的项。
每对列表进行一次遍历，就有一个最大项排在了正确的位置，大体上讲，
列表的每一个数据项都会在其相应位置 “冒泡”
第一次遍历：n - 1
次
[54, 26, 93, 17, 77, 31, 44, 55, 20]
第1次
交换
[26, 54, 93, 17, 77, 31, 44, 55, 20]
第2次
不交换
[26, 54, 17, 93, 77, 31, 44, 55, 20]
第3次
交换
[26, 54, 17, 77, 93, 31, 44, 55, 20]
第4次
交换
[26, 54, 17, 77, 31, 93, 44, 55, 20]
第5次
交换
[26, 54, 17, 77, 31, 44, 93, 55, 20]
第6次
交换
[26, 54, 17, 77, 31, 44, 55, 93, 20]
第7次
交换
[26, 54, 17, 77, 31, 44, 55, 20, 93]
第8次
交换
结果：[26, 54, 17, 77, 31, 44, 55, 20, 93]
第二次遍历： n - 2
次

# 实现冒泡排序
# def bubbleSort(alist):
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i] > alist[i+1]:
#                 temp = alist[i]
#                 alist[i] = alist[i+1]
#                 alist[i+1] = temp
#                 # alist[i],alist[i+1] = alist[i+1],alist[i]
# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)
# 假设输入的是一个已经排好序的列表  [17, 20, 26, 31, 44, 54, 55, 77, 93]
# 如果列表整个排序过程没有交换，说明列表已经完成了排序，因此可以通过判断有没有发生交换，改良冒泡排序改良完了之后，就是：短路冒泡排序实现短路冒泡排序
def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shortBubbleSort(alist)
print(alist)
# 练习：[19,1,9,7,3,10,13,15,8,12]  写出第三次遍历之后的列表


二、选择排序：每遍历一次列表只交换一次数据，也就是进行一次遍历时找到最大的项
完成遍历后，再把它换到正确的位置
alist = [26, 54, 93, 17, 77, 31, 44, 55, 20]
第1次遍历[26, 54, 20, 17, 77, 31, 44, 55, 93]  93
第2次遍历[26, 54, 20, 17, 55, 31, 44, 77, 93]  77
第3次遍历[26, 54, 20, 17, 44, 31, 55, 77, 93]  55
第4次遍历[26, 31, 20, 17, 44, 54, 55, 77, 93]  54
第5次遍历[26, 31, 20, 17, 44, 54, 55, 77, 93]  44
第6次遍历[26, 31, 20, 17, 44, 54, 55, 77, 93]  31
第7次遍历[20, 17, 26, 31, 44, 54, 55, 77, 93]  26
第8次遍历[17, 20, 26, 31, 44, 54, 55, 77, 93]  20

def seletcSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionMax = 0

        for location in range(1,fillslot+1):
            if alist[location] > alist[positionMax]:
                positionMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionMax]
        alist[positionMax] = temp

alist = [26,54,93,17,77,31,44,55,20]
seletcSort(alist)
print(alist)
'''

'''
    三、插入排序：总是会保持一个位置靠前的已经拍好的字表[54]，[26,93,17,77,31,44,55,20]，然后每一个新的数据项被“插入”到前面的字表中，拍好的第一个字表就增加了一项，
    alist = [54,26,93,17,77,31,44,55,20]
    分成两个字表[54],[26,93,17,77,31,44,55,20]，取出字表的数据一一和另一个字表进行比较，然后插入数据。
    第一步 [26,54]    [93,17,77,31,44,55,20],取出26比较，然后插入
    第二步 [26,54,93]    [17,77,31,44,55,20],取出93比较，然后插入
'''
# def insertSort(alist):
#     for index in range(1,len(alist)):
#         currentValue = alist[index]
#         position = index
#         while position > 0 and alist[position-1] > currentValue:
#             alist[position] = alist[position-1]
#             position = position-1
#             alist[position] = currentValue
# alist = [54,26,93,17,77,31,44,55,20]
# insertSort(alist)
# print(alist)


'''
力扣第147题
四、希尔排序（缩小间隔排序）：以插入排序为基础，将原来要排序的列表划分成一列子列表，再对每一个子列表执行插入操作，从而实现对插入排序性能的改进。
    关键：划分子列表的特定方法
    alist = [54,26,93,17,77,31,44,55,20]
    1.以3为间隔来划分，分成3个子列表.将列表以3为间隔，来划分，每隔3个数字取一个值
    [54,17,44]    [17,26,93,44,77,31,54,55,20]
    [26,77,55]    [17,26,93,44,55,31,54,77,20]
    [93,31,20]    [17,26,20,44,55,31,54,77,93]
    
    在进行标准插入排序：[17],[26,20,44,55,31,54,77,93]
    优化了对比和移动的次数
    
    2.以2为间隔，划分成5个子列表
    [54,93]  
    [17,31]  
    [44,20]
    [26,77]
    [31,55]
    

def shellSort(alist):
    pass

def gapInsertionSort(alist,start,gap):
    for i in range(0,len(alist),gap):
        currentValue = alist[i]
        position = i

        if position >= gap and alist[position-gap] > currentValue:
            alist[position] = alist[position-gap]
            position = position - gap
            alist[position] = currentValue

alist = [54,26,93,17,77,31,44,55,20]
for i in range(len(alist)//3):
    gapInsertionSort(alist,i,3)
print(alist)
'''

'''
    五、归并排序
    具体做法：递归算法，不断地将列表拆分成一半，
    如果列表为空或者只有一个元素，那么根据定义，它就排好了。
    alist = [54,26,93,17,77,31,44,55,20]
    第一次拆分[54,26,93,17]            [77,31,44,55,20]
    第二次拆分[54,26] [93,17]          [77,31] [44,55,20]
    第三次拆分[54][26][93][17]         [77][31][44][55,20]
    第四次拆分                                   [55][20]
    
    
    [54][26]  [93][17]      [77][31] [44][55] [20]
1.    [26,54]  [17,93]        [31,77]     [20,55].
2.     [17,26,54,93]                  [20,44,55]
3.                             [20,31,44,55,77]
4.              [17,20,26,31,44,54,55,77,93]

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i =0
        j = 0
        k = 0
        while i <len(righthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i=i+1
            else:
                alist[k] = righthalf[j]
                j = j +1
            k = k + 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
'''


'''
六、快速排序
    选择一个值作为枢纽值，一般就是列表第一项，枢纽值作为帮助拆分的标准

    alist = [54,26,93,17,77,31,44,55,20]
            [17,20,26,31,44,54,55,77,93]
    54始终在原列表中31的位置上，这个位置叫做拆分点
    
    54  左标记[26,93,17,77,31,44,55,20]  右标记
    首先增加左标记，直到找到一个大于枢纽值的值停止，然后递减右标记，直到找到一个小于枢纽值的值停止，交换这两项。

'''
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
# def quickSort(alist):
#     quickSortHelper(alist,0,len(alist)-1)
#
# def quickSortHelper(alist,first,last):
#     if first < last:
#         splitpoint = partition(alist,first,last)
#         quickSortHelper(alist,first,splitpoint-1)
#         quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
# partition(alist,0,len(alist)-1)
quickSort(alist)
print(alist)










