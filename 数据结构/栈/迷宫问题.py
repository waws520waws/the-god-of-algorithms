maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
dirs = [
    lambda x,y:(x+1,y),
    lambda x,y:(x-1,y),
    lambda x,y:(x,y-1),
    lambda x,y:(x,y+1),
]

# 回溯法
def maze_path(x1,y1,x2,y2):   # x1,y1代表起点的位置，x2,y2代表终点的位置
    stack = []
    stack.append((x1,y1))
    while(len(stack)>0):
        curNode = stack[-1]
        # x,y四个方向 左 x-1,y  右 x+1，y   上 x,y-1  下 x,y+1
        if curNode[0] == x2 and curNode[1] == y2:
            # 走到了终点
            for p in stack:
                print(p)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            # 如果下个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2 # 2表示为已经走过
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2
            stack.pop()
    else:
        print("没有路")
        return False

maze_path(1,1,8,8)


