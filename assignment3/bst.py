#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assignment 3 Binary Search Tree."""


class NullBinaryTreeNode(object):
    """Null object pattern for a BST."""

    SINGLETON = None

    def __new__(cls):
        """__new__."""
        if NullBinaryTreeNode.SINGLETON is not None:
            return NullBinaryTreeNode.SINGLETON
        NullBinaryTreeNode.SINGLETON = super(
            NullBinaryTreeNode, cls).__new__(cls)
        return NullBinaryTreeNode.SINGLETON

    def __init__(self):
        """__init__."""
        pass

    def __bool__(self):
        """__bool__."""
        return False

    def __nonzero__(self):
        """__nonzero__."""
        return False

    def __gt__(self, other):
        """__gt__."""
        return False

    def __lt__(self, other):
        """__lt__."""
        return False

    def __ge__(self, other):
        """__ge__."""
        return False

    def __le__(self, other):
        """__le__."""
        return False

    def __eq__(self, other):
        """__eq__."""
        return False

    def __ne__(self, other):
        """__ne__."""
        return False

    def __contains__(self, key):
        """__contains__."""
        return False

    def __getitem__(self, key):
        """__getitem__."""
        raise KeyError("Element {K} not found".format(K=key))

    @property
    def parent(self):
        """parent."""
        return NullBinaryTreeNode.SINGLETON

    @property
    def left(self):
        """left."""
        return NullBinaryTreeNode.SINGLETON

    @property
    def right(self):
        """right."""
        return NullBinaryTreeNode.SINGLETON

    @parent.setter
    def parent(self, other):
        """parent."""
        return

    @left.setter
    def left(self, other):
        """left."""
        return

    @right.setter
    def right(self, other):
        """right."""
        return

    def replace_child(self, child, replacement):
        """replace_child."""
        return

    def delete(self, key):
        """delete."""
        raise KeyError("Element {K} not found".format(K=key))

    def add(self, key, data):
        """add."""
        return BinaryTreeNode(key=key, data=data)

    def inorder(self):
        """inorder."""
        return iter(())

    def preorder(self):
        """preorder."""
        return iter(())

    def postorder(self):
        """postorder."""
        return iter(())

    def height(self, height=0):
        """height."""
        return height


class BinaryTreeNode(object):
    """A BST Node."""

    def __init__(
            self,
            data=None,
            key=None,
            left=NullBinaryTreeNode(),
            right=NullBinaryTreeNode(),
            parent=NullBinaryTreeNode()):
        """__init__."""
        super(BinaryTreeNode, self).__init__()
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def add(self, key, data):
        """add."""
        if self == key:
            self.data = data
        elif self > key:
            self.left = self.left.add(key, data)
            self.left.parent = self
        elif self < key:
            self.right = self.right.add(key, data)
            self.right.parent = self
        return self

    def inorder(self):
        """inorder."""
        yield from self.left.inorder()
        yield self.key, self.data
        yield from self.right.inorder()

    def postorder(self):
        """postorder."""
        yield from self.left.postorder()
        yield from self.right.postorder()
        yield self.key, self.data

    def preorder(self):
        """preorder."""
        yield self.key, self.data
        yield from self.left.preorder()
        yield from self.right.preorder()

    def height(self, height=-1):
        """height."""
        height += 1
        left_height = self.left.height(height)
        right_height = self.right.height(height)
        return max(left_height, right_height)

    def __getitem__(self, key):
        """__getitem__."""
        if self == key:
            return self.data
        elif self > key:
            return self.left[key]
        else:
            return self.right[key]

    def replace_child(self, child, replacement):
        """replace_child."""
        if self.left is child:
            self.left = replacement
        else:
            self.right = replacement

    def delete(self, key):
        """delete."""
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
        """pop_minimum."""
        if self.left:
            return self.left.pop_minimum()
        self.parent.replace_child(self, self.left)
        self.right.parent = self.parent
        return self

    def __contains__(self, item):
        """__contains__."""
        if self == item:
            return True
        if self < item:
            return item in self.right
        if self > item:
            return item in self.left

    def __eq__(self, other):
        """__eq__."""
        if isinstance(other, BinaryTreeNode):
            return self.key == other.key
        return self.key == other

    def __ne__(self, other):
        """__ne__."""
        return not self == other

    def __gt__(self, other):
        """__gt__."""
        if isinstance(other, BinaryTreeNode):
            return self.key > other.key
        return self.key > other

    def __lt__(self, other):
        """__lt__."""
        if isinstance(other, BinaryTreeNode):
            return self.key < other.key
        return self.key < other

    def __ge__(self, other):
        """__ge__."""
        if isinstance(other, BinaryTreeNode):
            return self.key >= other.key
        return self.key >= other

    def __le__(self, other):
        """__le__."""
        if isinstance(other, BinaryTreeNode):
            return self.key < other.key
        return self.key <= other


class BinarySearchTreeDict(object):
    """Binary Search Tree Dictionary."""

    def __init__(self):
        """__init__."""
        super(BinarySearchTreeDict, self).__init__()
        self.root = NullBinaryTreeNode()
        self.size = 0

    @property
    def height(self):
        """height."""
        return self.root.height()

    def inorder_keys(self):
        """inorder_keys."""
        return (k for k, _ in self.items())

    def postorder_keys(self):
        """postorder_keys."""
        return (k for k, _ in self.root.postorder())

    def preorder_keys(self):
        """preorder_keys."""
        return (k for k, _ in self.root.preorder())

    def items(self):
        """items."""
        return self.root.inorder()

    def __getitem__(self, key):
        """__getitem__."""
        return self.root[key]

    def __setitem__(self, key, value):
        """__setitem__."""
        if key not in self:
            self.size += 1
        self.root = self.root.add(key, value)

    def __delitem__(self, key):
        """__delitem__."""
        self.root = self.root.delete(key)
        self.size -= 1

    def __contains__(self, key):
        """__contains__."""
        return key in self.root

    def __len__(self):
        """__len__."""
        return self.size

    def __str__(self):
        """__str__."""
        return (
            "Inorder: " + ", ".join(str(k) for k in self.inorder_keys()) +
            "\n" +
            "Preorder: " + ", ".join(str(k) for k in self.preorder_keys())
            )

    def __repr__(self):
        """__repr__."""
        return str(self)

    def display(self):
        """display."""
        print(self)
