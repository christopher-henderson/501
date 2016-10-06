# -*- coding: utf-8 -*-


class SinglyLinkedNode(object):

    def __init__(self, item=None, next_link=None):
        super(SinglyLinkedNode, self).__init__()
        self._item = item
        self._next = next_link

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __repr__(self):
        return repr(self.item)


class SinglyLinkedList(object):

    def __init__(self):
        super(SinglyLinkedList, self).__init__()
        self.head = None
        self.length = 0

    def __len__(self):
        # TODO
        return self.length

    def __iter__(self):
        # TODO
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __contains__(self, item):
        # TODO
        for node in self:
            if node.item == item:
                return True
        return False

    def remove(self, item):
        # TODO: find item and remove it.

        previous = None
        current = self.head
        while current is not None:
            found = current.item == item
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
        return None

    def prepend(self, item):
        # TODO ad item to the front of the list
        node = SinglyLinkedNode(item)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def __repr__(self):
        s = "List:" + "->".join([item for item in self])
        return s

# =============================================================================


class BinaryTreeNode(object):

    def __init__(self, data=None, key=None, left=None, right=None, parent=None):
        super(BinaryTreeNode, self).__init__()
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def height(self, height=0):
        if self.left is not None:
            left_height = self.left.height(height + 1)
        else:
            left_height = height
        if self.right is not None:
            right_height = self.right.height(height + 1)
        else:
            right_height = height
        return max(left_height, right_height)

    def inorder(self):
        if self.left is not None:
            yield self.left.inorder()
        yield self.key, self.data
        if self.right is not None:
            yield self.right.inorder()

    def preorder(self):
        yield self.key, self.data
        if self.left is not None:
            yield self.left.preorder
        if self.right is not None:
            yield self.right.preorder

    def postorder(self):
        if self.left is not None:
            yield self.left.preorder
        if self.right is not None:
            yield self.right.preorder
        yield self.key, self.data

    def add(self, node):
        if self == node:
            self.value = node.value
            return 0
        elif node < self and self.left is None:
            node.parent = self
            self.left = node
            return 1
        elif node > self and self.right is None:
            node.parent = self
            self.right = node
            return 1
        elif node < self:
            return self.left.add(node)
        else:
            return self.right.add(node)

    def __eq__(self, other):
        return self.key == other.key

    def __gt__(self, other):
        return self.key > other.key

    def __lt__(self, other):
        return self.key < other.key

    def __contains__(self, key):
        if self.key == key:
            return True
        if self.key < key:
            return key in self.left if self.left is not None else False
        if self.key > key:
            return key in self.right if self.right is not None else False


class BinarySearchTreeDict(object):

    def __init__(self):
        super(BinarySearchTreeDict, self).__init__()
        self.root = None
        self.size = 0

    @property
    def height(self):
        if self.root is None:
            return 0
        return self.root.height()

    def inorder_keys(self):
        return (key for key, _ in self.items())

    def postorder_keys(self):
        if self.root is None:
            return iter(())
        return (key for key, _ in self.root.postorder())

    def preorder_keys(self):
        if self.root is None:
            return iter(())
        return (key for key, _ in self.root.preorder())

    def items(self):
        if self.root is None:
            return iter(())
        return self.root.inorder()

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        for k, v in self.items():
            if key == v:
                return v
        return None

    def __setitem__(self, key, value):
        # TODO:
        node = BinaryTreeNode(key, value)
        if self.root is None:
            self.root = node
            self.size += 1
        else:
            self.size += self.root.add(node)

    def __delitem__(self, key):
        # TODO
        pass

    def __contains__(self, key):
        # TODO
        return self.root is not None and key in self.root

    def __len__(self):
        # TODO
        return self.size

    def display(self):
        # TODO: Print the keys using INORDER on one
        #      line and PREORDER on the next
        return (
            ", ".join(self.inorder_keys()) + "\n" +
            ", ".join(self.preorder_keys())
            )


# =============================================================================


class ChainedHashDict(object):

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(ChainedHashDict, self).__init__()
        # TODO: Construct a new table
        pass

    @property
    def load_factor(self):
        # TODO
        pass

    @property
    def bin_count(self):
        # TODO
        pass

    def rebuild(self, bincount):
        # Rebuild this hash table with a new bin count
        # TODO
        pass

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        pass

    def __setitem__(self, key, value):
        # TODO:
        pass

    def __delitem__(self, key):
        # TODO
        pass

    def __contains__(self, key):
        # TODO
        pass

    def __len__(self):
        # TODO
        pass

    def display(self):
        # TODO: Return a string showing the table with multiple lines
        # TODO: I want the string to show which items are in which bins
        pass


class OpenAddressHashDict(object):

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(OpenAddressHashDict, self).__init__()

        # TODO initialize
        pass

    @property
    def load_factor(self):
        # TODO
        pass

    @property
    def bin_count(self):
        # TODO
        pass

    def rebuild(self, bincount):
        # Rebuild this hash table with a new bin count
        # TODO
        pass

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        pass

    def __setitem__(self, key, value):
        # TODO:
        pass

    def __delitem(self, key):
        # TODO
        pass

    def __contains__(self, key):
        # TODO
        pass

    def __len__(self):
        # TODO
        pass

    def display(self):
        # TODO: Return a string showing the table with multiple lines
        # TODO: I want the string to show which items are in which bins
        pass


def terrible_hash(bin):
    """A terrible hash function that can be used for testing.

    A hash function should produce unpredictable results,
    but it is useful to see what happens to a hash table when
    you use the worst-possible hash function.  The function
    returned from this factory function will always return
    the same number, regardless of the key.

    :param bin:
        The result of the hash function, regardless of which
        item is used.

    :return:
        A python function that can be passed into the constructor
        of a hash table to use for hashing objects.
    """
    def hashfunc(item):
        return bin
    return hashfunc


def main():
    # Thoroughly test your program and produce useful out.
    #
    # Do at least these kinds of tests:
    #  (1)  Check the boundary conditions (empty containers,
    #       full containers, etc)
    #  (2)  Test your hash tables for terrible hash functions
    #       that map to keys in the middle or ends of your
    #       table
    #  (3)  Check your table on 100s or randomly generated
    #       sets of keys to make sure they function
    #
    #  (4)  Make sure that no keys / items are lost, especially
    #       as a result of deleting another key
    pass


if __name__ == '__main__':
    main()
