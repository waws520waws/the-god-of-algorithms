# 尾插法创建链表

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

def create_linklist(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def print_linklist(lk):
    while lk:
        print(lk.item,end=",")
        lk=  lk.next

lk = create_linklist([1,2,3])
print_linklist(lk)