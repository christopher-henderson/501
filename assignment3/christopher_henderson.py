#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Assignment 3.

ASU, SER 501
October 27th, 2016

Christopher Henderson
"""


class SinglyLinkedNode(object):
    """Singly Linked List Node."""

    def __init__(self, key=None, item=None, next_link=None):
        """__init__."""
        super(SinglyLinkedNode, self).__init__()
        self._key = key
        self._item = item
        self._next = next_link

    @property
    def item(self):
        """item."""
        return self._item

    @item.setter
    def item(self, item):
        """item."""
        self._item = item

    @property
    def key(self):
        """key."""
        return self._key

    @key.setter
    def key(self, key):
        """key."""
        self._key = key

    @property
    def next(self):
        """next."""
        return self._next

    @next.setter
    def next(self, next):
        """next."""
        self._next = next

    def __nonzero__(self):
        """__nonzero__."""
        return self.item is not None

    def __bool__(self):
        """__bool__."""
        return self.__nonzero__()

    def __repr__(self):
        """__repr__."""
        return repr(self.item)

    def __str__(self):
        """__str__."""
        if not self.key:
            return str(self.item)
        return str([self.key, self.item])


class SinglyLinkedList(object):
    """Singly Linked List."""

    def __init__(self):
        """__init__."""
        super(SinglyLinkedList, self).__init__()
        self.head = None
        self.length = 0

    def __len__(self):
        """__len__."""
        return self.length

    def __iter__(self):
        """__iter__."""
        node = self.head
        while node is not None:
            yield node.item
            node = node.next

    def nodes(self):
        """nodes."""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __contains__(self, item):
        """__contains__."""
        for node in self.nodes():
            if node.item == item:
                return True
        return None

    def remove(
            self,
            obj,
            comparator=lambda node, obj: node.item == obj,
            fail=False):
        """remove."""
        previous = None
        current = self.head
        while current is not None:
            found = comparator(current, obj)
            if found and current is self.head:
                value = self.head.item
                self.head = self.head.next
                self.length -= 1
                return value
            elif found:
                previous.next = current.next
                self.length -= 1
                return current.item
            else:
                previous = current
                current = current.next
        if not fail:
            return None
        else:
            raise KeyError("Could not find {OBJ}".format(OBJ=obj))

    def prepend(self, item, key=None):
        """prepend."""
        node = SinglyLinkedNode(item=item, key=key)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return node

    def __repr__(self):
        """__repr__."""
        return "List:" + "->".join([str(item) for item in self.nodes()])

    def __str__(self):
        """__str__."""
        return self.__repr__()


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
        return None

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
        return None

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

    def height(self, height=-1):
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
        for k, v in self.left.inorder():
            yield k, v
        yield self.key, self.data
        for k, v in self.right.inorder():
            yield k, v

    def postorder(self):
        """postorder."""
        for k, v in self.left.postorder():
            yield k, v
        for k, v in self.right.postorder():
            yield k, v
        yield self.key, self.data

    def preorder(self):
        """preorder."""
        yield self.key, self.data
        for k, v in self.left.preorder():
            yield k, v
        for k, v in self.right.preorder():
            yield k, v

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
    def length(self):
        """length."""
        return self.size

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

    def _items(self):
        """_items."""
        return [list(item) for item in self.items()]

    def items(self):
        """items."""
        return self.root.inorder()

    def __getitem__(self, key):
        """__getitem__."""
        if key is None:
            return None
        return self.root[key]

    def __setitem__(self, key, value):
        """__setitem__."""
        if key is None:
            return None
        if key not in self:
            self.size += 1
        self.root = self.root.add(key, value)
        return True

    def __delitem__(self, key):
        """__delitem__."""
        if key is None:
            return None
        if key not in self:
            return None
        self.root = self.root.delete(key)
        self.size -= 1
        return True

    def __contains__(self, key):
        """__contains__."""
        return key in self.root

    def __len__(self):
        """__len__."""
        return self.size

    def __str__(self):
        """__str__."""
        return (
            "Inorder:" + "->".join(str(k) for k in self.inorder_keys()) +
            "\n" +
            "Preorder:" + "->".join(str(k) for k in self.preorder_keys())
            )

    def __repr__(self):
        """__repr__."""
        return str(self)

    def display(self):
        """display."""
        return str(self).split("\n")


class ChainedHashDict(object):
    """Chained Hashing Dictionary."""

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        """__init__."""
        super(ChainedHashDict, self).__init__()
        if bin_count <= 0:
            raise TypeError("Bin count must be greater than zero.")
        self.table = [SinglyLinkedList() for _ in range(bin_count)]
        self.max_load = max_load
        self.hash = hashfunc
        self.size = 0

    @property
    def load_factor(self):
        """load_factor."""
        return self.size / self.bin_count

    @property
    def bin_count(self):
        """bin_count."""
        return len(self.table)

    @property
    def should_resize(self):
        """should_resize."""
        return self.load_factor >= self.max_load

    def rebuild(self, bincount):
        """rebuild."""
        tmp = self.table
        self.table = [SinglyLinkedList() for _ in range(bincount)]
        self.size = 0
        for linked_list in tmp:
            for node in linked_list.nodes():
                self[node.key] = node.item
        del tmp

    def items(self):
        """items."""
        return iter(self)

    def __iter__(self):
        """__iter__."""
        for linked_list in self.table:
            for node in linked_list.nodes():
                yield node.key, node.item

    def __getitem__(self, key):
        """__getitem__."""
        address = self._address(key)
        chain = self.table[address]
        for node in chain.nodes():
            if node.key == key:
                return node.item
        return None
        # raise KeyError("{KEY} not found.".format(KEY=key))

    def __setitem__(self, key, value):
        """__setitem__."""
        if key is None:
            return None
        address = self._address(key)
        for node in self.table[address].nodes():
            if node.key == key:
                node.item = value
                return
        self.table[address].prepend(key=key, item=value)
        self.size += 1
        if self.should_resize:
            self.rebuild(self.bin_count * 2)
        return True

    def __delitem__(self, key):
        """__delitem__."""
        if key is None:
            return None
        if key not in self:
            return None
        address = self._address(key)
        self.table[address].remove(
            key,
            lambda node, key: node.key == key,
            fail=True)
        self.size -= 1
        return True

    def __contains__(self, key):
        """__contains__."""
        if key is None:
            return None
        address = self._address(key)
        for node in self.table[address].nodes():
            if node.key == key:
                return True
        return None

    def __len__(self):
        """__len__."""
        return self.size

    def __str__(self):
        """__str__."""
        string = ""
        for index, linked_list in enumerate(self.table):
            string += "{BIN}{LIST}\n".format(
                BIN=index, LIST=linked_list)
        return string.strip()

    def __repr__(self):
        """__repr__."""
        return str(self)

    @property
    def len(self):
        """len."""
        return len(self)

    def display(self):
        """display."""
        return str(self)

    def _address(self, key):
        """_address."""
        return self.hash(key) % self.bin_count


class DELETED(object):
    """"Representative of a deleted key."""

    class key(object):
        """Faking a pair key."""

        pass

    class value(object):
        """Faking a pair value."""

        pass


class EMPTY(object):
    """"Representative of an empty key."""

    class key(object):
        """Faking a pair key."""

        pass

    class value(object):
        """Faking a pair value."""

        pass


class Pair(object):
    """A key value pair in the dictionary."""

    def __init__(self, key, value):
        """__init__."""
        self.key = key
        self.value = value

    def __str__(self):
        """__str__."""
        return "Key: {K}, Value: {V}".format(K=self.key, V=self.value)


class OpenAddressHashDict(object):
    """An open addressed hashing dictionary. Linear probing."""

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        """__init__."""
        super(OpenAddressHashDict, self).__init__()
        if bin_count <= 0:
            raise TypeError("Bin count must be greater than zero.")
        self.table = [EMPTY for _ in range(bin_count)]
        self.max_load = max_load
        self.hash = hashfunc
        self.size = 0

    @property
    def load_factor(self):
        """load_factor."""
        return self.size / self.bin_count

    @property
    def bin_count(self):
        """bin_count."""
        return len(self.table)

    def rebuild(self, bincount):
        """rebuild."""
        tmp = self.table
        self.table = [EMPTY for _ in range(bincount)]
        self.size = 0
        for pair in (p for p in tmp if isinstance(p, Pair)):
            self[pair.key] = pair.value
        del tmp

    @property
    def should_rebuild(self):
        """should_rebuild."""
        return self.load_factor >= self.max_load

    def __iter__(self):
        """__iter__."""
        for entry in self.table:
            if isinstance(entry, Pair):
                yield entry.key, entry.value

    def __getitem__(self, key):
        """__getitem__."""
        if key is None:
            return None
        address = self.address(key)
        pair = self.table[address]
        i = 0
        while pair is not EMPTY:
            i += 1
            if pair.key == key:
                return pair.value
            address = self.address(key, i)
            pair = self.table[address]
        return None

    def __setitem__(self, key, value):
        """__setitem__."""
        if key is None:
            return None
        address = self.address(key)
        pair = self.table[address]
        i = 0
        while pair is not EMPTY and pair is not DELETED:
            i += 1
            if pair.key == key:
                pair.value = value
                return
            address = self.address(key, i)
            pair = self.table[address]
        self.table[address] = Pair(key, value)
        self.size += 1
        if self.should_rebuild:
            self.rebuild(self.bin_count * 2)
        return True

    def __delitem__(self, key):
        """__delitem__."""
        if key is None or key not in self:
            return None
        address = self.address(key)
        pair = self.table[address]
        i = 0
        while pair is not EMPTY:
            i += 1
            if pair.key == key:
                self.table[address] = DELETED
                self.size -= 1
                return True
            address = self.address(key, i)
            # address = (address + 1) % self.bin_count
            pair = self.table[address]
        return None

    def __contains__(self, key):
        """__contains__."""
        return self[key] is not None

    def __len__(self):
        """__len__."""
        return self.size

    @property
    def len(self):
        """len."""
        return len(self)

    def address(self, key, i=0):
        """address."""
        return (self.hash(key) + i) % self.bin_count

    def display(self):
        """display."""
        return str(self)

    def __str__(self):
        """__str__."""
        string = ""
        for index, pair in enumerate(self.table):
            string += "bin {BIN}: {PAIR}\n".format(
                BIN=index,
                PAIR=(
                    str([pair.key, pair.value]) if isinstance(pair, Pair) else
                    "DELETED" if pair is DELETED else "[None, None]"))
        return string.strip()
