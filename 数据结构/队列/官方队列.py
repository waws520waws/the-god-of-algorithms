from collections import deque

# q = deque()
# q.append(1)             # 队尾进队
# print(q.popleft())      # 队首出队

# 用于双向队列
# q.pop()    队尾出队
# q.appendleft(1)   队首进队

#两个参数，第一个是放入队列中的数据，第二个是队列的大小
# 这个部分有个好玩的事情：队满了，在添加元素不报错，而是将之前的多余元素弹出去
q = deque([1,2,3,4,5,6],5)
print(q.popleft())      # 队首出队
"""
输出是：2
这个部分在创建队列的时候，我们规定大小是5,这样我们[1,2,3,4,5],队内元素已经满了,
然后6进来，先进先出，1被顶出去了，所以我们能看到的popleft的时候的输出是2

熟悉的东西是linux的tail的命令
def tail(n):
    with open("test.txt","r") as f:
        q = deque(f,n)
        return q

上面能写f的实际的原因就是，f其实就是一个文件的列表对像，我们可以直接使用，和上面的列表导入deque是一个道理
"""
