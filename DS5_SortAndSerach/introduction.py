'''
    排序和搜索（查找）
    1.搜索：顺序搜索，二分搜索，
    2.排序：选择排序，冒泡排序，插入排序，希尔排序，归并排序，快速排序，堆排序，计算排序，桶排序，基数排序。
    https://www.runoob.com/w3cnote/ten-sorting-algorithm.html
    3.散列（Hash）


    一、搜索：

    1.顺序搜索：
        当数据项被存储在集合中时，如存储到一个列表中，我们就说，这些数据项之间有一个线性或顺序的关系，
        每一个数据项存储在一个和其他数据项相对的位置。在python的列表中，这些相对位置所对应的是单个项的索引值，由于这些索引值是有一定次序的，可以一次去访问它们，这一个过程产生了第一个搜索方法：顺序搜索。
    2.二分搜索：二分搜索将从中间开始检测，而不是按顺序搜索列表。如果查找项与我们刚搜索到的项匹配，则结束。如果不匹配，我们可以利用列表的有序性来排除掉一半的剩余项，



'''

# 从[1,2,3,4,5,56,6]中找10： 第一种结果找到了需要的数据项；第二种结果遍历了所有的数据项。

'''
无序：
def suquentialSearch(alist,item):
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

alist=[1,2,3,4,5,56,6]
# 时间复杂度最好的情况O(1)
print(suquentialSearch(alist,1))
# 时间复杂度最坏的情况O(n)
print(suquentialSearch(alist,6))
# 时间复杂度的平均情况O(n)

有序：
def orderedSequentialSearch(alist,item):
    pos = 0
    found = False
    stop = False

    while pos<len(alist) and not found and not stop:
        if alist[pos] == item:
            found = False
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found

alist = [17,20,26,31,44,54,55,65,77,93]
print(orderedSequentialSearch(alist,50))
'''

'''
二分查找：
    
def binarySerach(alist,item):
    first = 0
    last = len(alist)-1
    found = False
    midpoint = (first+last) // 2
    while first <= last and not found:
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

alist = [17,20,26,31,44,54,55,65,77,93]
print(binarySerach(alist,50))

# 递归二分查找
def binarySearch(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item <alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:], item)

alist = [17,20,26,31,44,54,55,65,77,93]
print(binarySearch(alist, 50))
'''











