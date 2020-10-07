
class queue(object):
    def __init__(self,size=100):
        self.queue = [0 for i in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0

    def push(self,element):
        if self.is_full():
            print("queue is full")
            return
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element

    def pop(self):
        if self.is_empty():
            print("queue is empty")
            return
        self.rear = (self.rear + 1) % self.size
        return self.queue[self.front]

    def is_full(self):
        return  (self.rear+1) % self.size == self.front

    def is_empty(self):
        return  self.rear == self.front

