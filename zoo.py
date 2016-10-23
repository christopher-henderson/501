class NullBinaryTreeNode(object):

    SINGLETON = None

    def __new__(cls):
        if NullBinaryTreeNode.SINGLETON is not None:
            return NullBinaryTreeNode.SINGLETON
        NullBinaryTreeNode.SINGLETON = super(
            NullBinaryTreeNode, cls).__new__(cls)
        return NullBinaryTreeNode.SINGLETON

    def __init__(self):
        pass

    def __bool__(self):
        return False

    def __nonzero__(self):
        return False

    def __gt__(self, other):
        return False

    def __lt__(self, other):
        return False

    def __ge__(self, other):
        return False

    def __le__(self, other):
        return False

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return False

    def __contains__(self, key):
        return False

    def __getitem__(self, key):
        return None

    @property
    def parent(self):
        return NullBinaryTreeNode.SINGLETON

    @property
    def children(self):
        return iter(())

    @property
    def left(self):
        return NullBinaryTreeNode.SINGLETON

    @property
    def right(self):
        return NullBinaryTreeNode.SINGLETON

    @parent.setter
    def parent(self, other):
        return

    @left.setter
    def left(self, other):
        return

    @right.setter
    def right(self, other):
        return

    def replace_child(self, child, replacement):
        return

    def delete(self, key):
        raise Exception("Element {K} not found".format(K=key))

    def add(self, key, data):
        return BinaryTreeNode(key=key, data=data)

    def inorder(self):
        return iter(())

    def preorder(self):
        return iter(())

    def postorder(self):
        return iter(())

    def height(self, height=0):
        return height


class TreeNode(object):
    def __init__(
            self,
            value=None,
            parent=NullBinaryTreeNode(),
            children=[]):
        super(TreeNode, self).__init__()
        self.value = value
        self.parent = parent
        self.children = children

    def add(self, node):
        pass

    def deserialize(self, obj, parent=NullBinaryTreeNode()):
        self.value = obj[0]
        self.parent = parent
        self.children = [TreeNode().deserialize(c, self) for c in obj[1]]
        return self

    def minimum(self, target=None, height=0):
        # r = [c.minimum(height + 1) for c in self.children] if self.children else 0
        if self.value == target:
            return height
        if not self.children:
            return None
        mins = [c.minimum(target=target, height=height + 1) for c in self.children]
        return min(m for m in mins if m is not None)
        # return min([c.minimum(height + 1) for c in self.children] if self.children else [height])

    def display(self, tabs=0):
        print(self, self.children)
        for child in self.children:
            child.display()

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    @property
    def isOwnAncestor(self):
        parent = self.parent
        while parent:
            if parent.value is self.value:
                pass


class Tree(object):

    def __init__(self):
        super(Tree, self).__init__()
        self.root = TreeNode()
        self.size = 0

    def minimum(self, target):
        return self.root.minimum(target)

    def deserialize(self, obj):
        self.root.deserialize(obj)

    def __getitem__(self, key):
        return self.root[key]

    def __setitem__(self, key, value):
        self.root = self.root.add(key, value)

    def __delitem__(self, key):
        # TODO
        self.root = self.root.delete(key)

    def __contains__(self, key):
        return key in self.root

    def __len__(self):
        return self.size

    def display(self):
        self.root.display()







def main():
    tree = Tree()
    things = ("cat",
                (
                    ("dpg", ()),
                    ("caw",
                        (
                            ("moo", ()),
                        )
                    ),
                    ("pig",
                        (
                            ("fuck", (
                                ("moo", ()),
                            )),
                        )
                    ),
                )
            )
    tree.deserialize(things)
    tree.display()
    print(tree.minimum("moo"))





main()
