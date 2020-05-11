# 1．将下列值通过“除以二”转化为二进制。写出余数的栈。
# a) 17
# b) 45
# c) 96
# n_list = [17,45,96]
# for n in n_list:
n = int(input('请输入数字：'))
print('当前数字是',n)
b = []  # 存储余数
while True:  # 一直循环，商为0时利用break退出循环
    s = n // 2  # 商
    # print('商',s)
    y = n % 2  # 余数
    # print('余数',y)
    b = b + [y]  # 每一个余数存储到b中
    # print (b)
    if s == 0:
        break  # 余数为0时结束循环
    n = s
b.reverse()  # 使b中的元素反向排列
b = [ str(i)for i in b ]
print ('该数字转换为二进制后是：',' '.join(b))


# 2．将下列中缀表达式转化为前缀表达式（使用全括号的方法）：
# a) (A+B)*(C+D)*(E+F)
# b) A+((B+C)*(D+E))
# c) A*B*C*D+E+F

class Stack:
    def __init__(self):
        self.items = []

    # 是否为空
    def is_empty(self):
        return self.items == []

    # 进栈
    def push(self, item):
        self.items.append(item)

    # 出栈
    def pop(self):
        return self.items.pop()

    # 返回栈顶值，不改变栈
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈长度
    def size(self):
        return len(self.items)


def infix_to_prefix(infix_expr):
    prec = dict()
    prec[")"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    prefix_expr = []
    s = Stack()
    # 从右到左扫描
    for item in reversed(infix_expr.split()):
        # 如果标记是操作数，将其附加到输出列表的末尾
        if item not in prec.keys():
            prefix_expr.append(item)
        # 如果标记是右括号，将其压到 s 上
        elif item == ')':
            s.push(item)
        # 如果标记是左括号，则弹出 s，直到删除相应的右括号。将每个运算符附加到
        # 输出列表的末尾
        elif item == '(':
            while s.peek() != ')':
                prefix_expr.append(s.pop())
            s.pop()
        # 如果标记是运算符， *，/，+  或  -  ，将其压入 s。但是，首先删除已经在
        # s 中具有更高或相等优先级的任何运算符，并将它们加到输出列表中
        else:
            while (not s.is_empty()) \
                    and s.peek() != ')' \
                    and prec[s.peek()] > prec[item]:
                prefix_expr.append(s.pop())
                s.push(item)
            s.push(item)
        # print(s.items)
    # 当输入表达式被完全处理时，检查 s。仍然在栈上的任何运算符都可以删除并加到
    # 输出列表的末尾
    while not s.is_empty():
        prefix_expr.append(s.pop())
    # 反转序列
    prefix_expr.reverse()
    return ' '.join(prefix_expr)


def prefix_eval(prefix_expr):
    s = Stack()
    for item in reversed(prefix_expr.split()):
        # 如果不是运算符号，压栈
        if item not in '+-*/':
            s.push(item)
        else:
            op1 = int(s.pop())
            op2 = int(s.pop())
            # print(op1, item, op2)
            result = do_match(item, op1, op2)
            s.push(result)
            # print(s.items)
            return result


# 运行结果
def do_match(op, op1, op2):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    else:
        raise Exception('Error operation!')

print('中缀转化前缀')
for i in ['( A + B ) * ( C + D ) * ( E + F )','A + ( ( B + C ) * ( D + E ) )','A * B * C * D + E + F ']:
    print('原式为：',i)
    infix_str = i
    prefix_output = infix_to_prefix(infix_str)
    print('转换后为：',prefix_output)


# 3．将上述的中缀表达式转化为后缀表达式（使用全括号的方法）。
from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print('中缀转化后缀')
for i in ['( A + B ) * ( C + D ) * ( E + F )','A + ( ( B + C ) * ( D + E ) )','A * B * C * D + E + F ']:
    print('原式为：',i)
    print('转换后为：',infixToPostfix(i))




# 4．采用直接的转化算法将上述的中缀表达式转化为后缀表达式。写出转化时栈
# 的实时变化。

# 5．计算下列后缀表达式的值。写出当每个操作数和操作符被处理时栈的实时变
# 化。
# a) 2 3 * 4 +
# b) 1 2 + 3 + 4 + 5 +
# c) 1 2 3 4 5 * + * +

# 6．队列（Queue）的一种替换实现是使用一个列表使队列的尾在列表的末端。
# 这样的替换操作会对其大 O 数量级产生什么样的影响？

# 7．在链表中，使用 add 方法时执行顺序相反的结果是什么？参考结果是什么？
# 可能会什么样的问题？

# 8．解释当数据项在最后一个节点时链表的 remove 方法如何实现。

# 9．解释当数据项是链表中唯一一个节点时链表的 remove 功能如何实现。

# 3.10.编程练习
# 1．修改中缀表达式转为后缀表达式的算法使之能处理错误输入。
# 2．修改后缀表达式求值的算法使之能处理错误输入。
# 3．实现一个结合了中缀到后缀的转化法和后缀的求值算法的直接求中缀表达式值的方法。你的
# 求值法应该从左至右处理中缀表达式中的符号，并且使用两个栈来完成求值，一个存储操作数，一
# 个存储操作符。
# 4．将上一题的中缀求值法转化为一个计算器。
# 5．实现一个 Queue，使用一个 list 使 Queue 的尾部在 list 的末端。
# 6．设计并实现一个实验，对以上两种 Queue 进行基准比较。你从这个实验中学到了什么？
# 7．实现一个队列并使它的 enqueue 和 dequeue 方法平均时间复杂度都是 O(1)。也就是说，在
# 大多数情况下 enqueue 和 dequeue 都是 O（1），除了在一种特殊情况下 dequeue 可能为 O（n）。
# 8. 考虑一个现实生活中的情况。制定一个问题，然后设计一个可以帮助解决问题的模拟实验。
# 可能的情况包括：
# a）洗车店一字排开的汽车
# b）在杂货店结账的顾客
# C）在跑道起飞、降落的飞机
# d）一个银行柜员
# 一定要解释清楚做的任何假设，并且提供该方案必须包含的和概率有关的数据。
# 9．修改热土豆模拟实验，采用一个随机选择的数值，使每轮实验不能通过前一
# 次实验来预测。
# 10．实现基数排序。十进制的基数排序是一个使用了“箱的集合”（包括一个主箱和 10 个数字
# 箱）的机械分选技术。每个箱像队列（Queue）一样，根据数据项的到达顺序排好并保持它们的值。
# 算法开始时，将每一个待排序数值放入主箱中。然后对每一个数值进行逐位的分析。每个从主箱最
# 前端取出的数值，将根据其相应位上的数字放在对应的数字箱中。比如，考虑个位数字，534 被放置
# 在数字箱 4，667 被放置在数字箱 7。一旦所有的数值都被放置在相应的数字箱中，所有数值都按照
# 从箱 0 到箱 9 的顺序，依次被取出，重新排入主箱中。该过程继续考虑十位数字，百位数字，等
# 等。当最后一位被处理完后，主箱中就包含了排好序的数值。
# 11．括号匹配问题的另一个例子是超文本标记语言（HTML）。在 HTML 中，标记以开始
# （opening tag，<tag>）和结束（closing tag，</tag>）的形式存在，它们必须成对出现来正确地描
# 述 web 文档。这个非常简单的 HTML 文档：
# 只是为了表明语言中标记的匹配和嵌套结构。写一个程序，它可以检查 HTML 文档中是否有匹
# 配的开始和结束标记。
# <html>
# <head>
# <title>
# Example
# </title>
# </head>
# <body>
# <h1>Hello, world</h1>
# </body>
# </html>
# . .12. 扩展 Listing 2.15 的程序来处理带空格的回文序列。比如，I PREFER PI 是一个回文序列，因
# 为如果忽略空格，它向前和向后读是一样的。
# 13. 为了实现 length 方法，我们在链表中计算节点的数目。一种代替的方法是链表中的节点的
# 数目作为附加的数据片段储存在链表表头中。修改无序列表类，包含这个信息并且重新编写 length
# 方法。
# 14. 实现 remove 方法，使得当列表中没有相应数据项的时候它能正常运行。
# 15. 修改列表使它允许重复。有哪些方法将受到这种变化的影响？
# 16. 实现无序列表类的__str__方法。对于列表而言，什么是一个好的字符串形式的表现？
# 17. 实现__str__方法，使列表以 Python
