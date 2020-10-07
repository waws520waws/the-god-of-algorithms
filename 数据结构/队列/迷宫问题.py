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

def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append((curNode[0],curNode[1]))
        curNode = path[curNode[2]]
    realpath.append(curNode[0:2])  # 将起点添加到路径中
    realpath.reverse()
    for node in realpath:
        print(node)


from collections import deque
def maze_path(x1,y1,x2,y2):   # x1,y1代表起点的位置，x2,y2代表终点的位置
    queue = deque()
    queue.append((x1,y1,-1))
    path = []
    while (len(queue) > 0):
        curNode = queue.popleft()
        path.append(curNode)
        # x,y四个方向 左 x-1,y  右 x+1，y   上 x,y-1  下 x,y+1
        if curNode[0] == x2 and curNode[1] == y2:
            # 走到了终点
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            # 如果下个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0],nextNode[1],len(path)-1))
                maze[nextNode[0]][nextNode[1]] = 2  # 2表示为已经走过
    else:
        print("没有路")
        return False

maze_path(1,1,8,8)