#TODO: Get rid of all flake8 warnings -- that means adding docstrings
#      to the file, classes, and methods.

#=============================================================================

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
        # TODO
        pass

    def __len__(self):
        # TODO
        pass

    def __iter__(self):
        # TODO
        pass

    def __contains__(self, item):
        # TODO
        pass

    def remove(self, item):
        # TODO: find item and remove it.
        pass

    def prepend(self, item):
        # TODO ad item to the front of the list
        pass

    def __repr__(self):
        s = "List:" + "->".join([item for item in self])
        return s

#=============================================================================

class BinaryTreeNode(object):
    def __init__(self, data = None, left = None, right = None, parent=None):
        super(BinaryTreeNode, self).__init__()
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTreeDict(object):

    def __init__(self):
        super(BinarySearchTreeDict, self).__init__()

        # TODO initialize
        pass

    @property
    def height(self):
        # TODO
        pass

    def inorder_keys(self):
        # TODO:Use the 'yield'  keyword and StopIteration exception
        # to return the keys, using an INORDER traversal
        pass

    def postorder_keys(self):
        # TODO: Use 'yield' and 'StopIteration' to yield key in POSTORDER
        pass

    def preorder_keys(self):
        # TODO: Use 'yield' and 'StopIteration' to yield key in PREORDER
        pass

    def items(self):
        # TODO: Use 'yield' to return the items (key and value) using
        # an INORDER traversal.
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
        # TODO: Print the keys using INORDER on one
        #      line and PREORDER on the next
        pass

#=============================================================================

class ChainedHashDict(object):

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(ChainedHash, self).__init__()

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
