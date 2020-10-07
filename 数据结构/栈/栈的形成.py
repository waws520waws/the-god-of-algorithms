# 实际上栈就是一个列表，不过这个列表加上了一些限制

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack):
            return self.stack.pop()
        else:
            print("Empty stack")

    def get_top(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            print("Empty stack")

if __name__ == '__main__':
    stack = Stack()
    for i in range(3):
        stack.push(i)
    print(stack.pop())