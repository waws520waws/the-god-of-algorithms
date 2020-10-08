class Node(object):
    def __init__(self,name,type="dir"):
        self.name = name
        self.type = type     # "dir" or "file"
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name

class FileSystemTree(object):
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self,name):
        # name必须是以/结尾
        if name[-1] != "/":
            name += "/"
        node =Node(name)
        self.now.children.append(node)
        node.parent= self.now

    def ls(self):
        return self.now.children

    def cd(self,name):
        # name必须是以/结尾
        if name[-1] != "/":
            name += "/"
        if name == "../" and self.now.name != "/":
            self.now = self.now.parent
            return
        if name == "../" and self.now.name == "/":
            self.now = self.root
            return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        else:
            raise ValueError("invalid dir")

tree = FileSystemTree()
tree.mkdir("ha11")
tree.mkdir("ha22")
tree.mkdir("ha33")
tree.cd("ha11")
tree.mkdir("ha-11")
tree.cd("../")
tree.cd("../")
print(tree.now.children)