class Linklist(object):
    class Node(object):
        def __init__(self,item):
            self.item = item
            self.next = None

    class LinklistIterator(object):
        def __init__(self,node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self


    def __init__(self,iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self,obj):
        s = Linklist.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self,iterable):
        for obj in iterable:
            self.append(obj)

    def find(self,obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False


    def __iter__(self):
        return self.LinklistIterator(self.head)

    def __repr__(self):
        return "<<"+"，".join(map(str,self))+">>"


# 这个部分实际上是使用的拉链法解决冲突
class HashTable(object):
    def __init__(self,size=101):
        self.size = size
        self.T = [Linklist() for _ in range(self.size)]

    def h(self,k):
        return k % self.size

    def find(self,k):
        i = self.h(k)
        return self.T[i].find(k)

    def insert(self,k):
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert")
        else:
            self.T[i].append(k)

ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(10)
ht.insert(102)

print("".join(map(str,ht.T)))
print(ht.find(102))
