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

    def is_empty(self):
        return len(self.stack) == 0

def brace_match(s):
    match = {"}":"{","]":"[",")":"("}
    stack = Stack()
    for ch in s:
        if ch in ["{","[","("]:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match.get(ch):
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(brace_match("[{}]({[{()}]})"))
    print(brace_match("[{({[{()}]})"))
