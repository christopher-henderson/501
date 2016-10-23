#!/usr/bin/env python3


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
        raise KeyError("Element {K} not found".format(K=key))

    @property
    def parent(self):
        return NullBinaryTreeNode.SINGLETON

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
        raise KeyError("Element {K} not found".format(K=key))

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


class BinaryTreeNode(object):
    def __init__(
            self,
            data=None,
            key=None,
            left=NullBinaryTreeNode(),
            right=NullBinaryTreeNode(),
            parent=NullBinaryTreeNode()):
        super(BinaryTreeNode, self).__init__()
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def add(self, key, data):
        if self >= key:
            self.left = self.left.add(key, data)
            self.left.parent = self
        elif self <= key:
            self.right = self.right.add(key, data)
            self.right.parent = self
        return self

    def inorder(self):
        yield from self.left.inorder()
        yield self.key, self.data
        yield from self.right.inorder()

    def postorder(self):
        yield from self.left.postorder()
        yield from self.right.postorder()
        yield self.key, self.data

    def preorder(self):
        yield self.key, self.data
        yield from self.left.preorder()
        yield from self.right.preorder()

    def height(self, height=-1):
        height += 1
        left_height = self.left.height(height)
        right_height = self.right.height(height)
        return max(left_height, right_height)

    def __getitem__(self, key):
        if self == key:
            return self.data
        elif self > key:
            return self.left[key]
        else:
            return self.right[key]

    def replace_child(self, child, replacement):
        if self.left is child:
            self.left = replacement
        else:
            self.right = replacement

    def delete(self, key):
        if self > key:
            self.left.delete(key)
            return self
        if self < key:
            self.right.delete(key)
            return self
        if self.left and self.right:
            replacement = self.right.pop_minimum()
            self.parent.replace_child(self, replacement)
            replacement.parent = self.parent
            if self.left is not replacement:
                replacement.left = self.left
            if self.right is not replacement.right:
                replacement.right = self.right
            return replacement
        elif self.left and not self.right:
            self.parent.replace_child(self, self.left)
            self.left.parent = self.parent
            return self.left
        elif not self.left and self.right:
            self.parent.replace_child(self, self.right)
            self.right.parent = self.parent
            return self.right
        else:
            self.parent.replace_child(self, self.right)
            return self.right

    def pop_minimum(self):
        if self.left:
            return self.left.pop_minimum()
        self.parent.replace_child(self, self.left)
        self.right.parent = self.parent
        return self

    def __contains__(self, item):
        if self == item:
            return True
        if self < item:
            return item in self.right
        if self > item:
            return item in self.left

    def __eq__(self, other):
        if isinstance(other, BinaryTreeNode):
            return self.key == other.key
        return self.key == other

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if isinstance(other, BinaryTreeNode):
            return self.key > other.key
        return self.key > other

    def __lt__(self, other):
        if isinstance(other, BinaryTreeNode):
            return self.key < other.key
        return self.key < other

    def __ge__(self, other):
        if isinstance(other, BinaryTreeNode):
            return self.key >= other.key
        return self.key >= other

    def __le__(self, other):
        if isinstance(other, BinaryTreeNode):
            return self.key < other.key
        return self.key <= other


class BinarySearchTreeDict(object):

    def __init__(self):
        super(BinarySearchTreeDict, self).__init__()
        self.root = NullBinaryTreeNode()
        self.size = 0

    @property
    def height(self):
        return self.root.height()

    def inorder_keys(self):
        return (k for k, _ in self.items())

    def postorder_keys(self):
        return (k for k, _ in self.root.postorder())

    def preorder_keys(self):
        return (k for k, _ in self.root.preorder())

    def items(self):
        return self.root.inorder()

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
        # TODO: Print the keys using INORDER on one
        #      line and PREORDER on the next
        return (
            ", ".join(str(k) for k in self.inorder_keys()) + "\n" +
            ", ".join(str(k) for k in self.preorder_keys())
            )







def main():
    b = BinarySearchTreeDict()
    b['i'] = 1
    b['b'] = 2
    b['a'] = 3
    b['c'] = 3
    b['d'] = 3
    b['j'] = 3
    print(b.display())
    # print(b.height)
    # print(b.root.key)
    # del b["i"]
    # print(b.root.key)
    # print("i" in b)



main()
