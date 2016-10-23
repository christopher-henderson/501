from __future__ import division

from linked_list import SinglyLinkedList


class ChainedHashDict(object):

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(ChainedHashDict, self).__init__()
        # TODO: Construct a new table
        if bin_count <= 0:
            raise TypeError("Bin count must be greater than zero.")
        self.table = [SinglyLinkedList() for _ in range(bin_count)]
        self.max_load = max_load
        self.hash = hashfunc
        self.size = 0

    @property
    def load_factor(self):
        return self.size / self.bin_count

    @property
    def bin_count(self):
        return len(self.table)

    @property
    def should_resize(self):
        return self.load_factor >= self.max_load

    def rebuild(self, bincount):
        # Rebuild this hash table with a new bin count
        # TODO
        tmp = self.table
        self.table = [SinglyLinkedList() for _ in range(bincount)]
        self.size = 0
        for linked_list in tmp:
            for node in linked_list:
                self[node.key] = node.item
        del tmp

    def items(self):
        for linked_list in self.table:
            yield from linked_list
            # for node in linked_list:
            #     yield node.key, node.value

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        address = self._address(key)
        chain = self.table[address]
        for node in chain:
            if node.key == key:
                return node.item
        return None

    def __setitem__(self, key, value):
        # TODO:
        address = self._address(key)
        for node in self.table[address]:
            if node.key == key:
                node.item = value
                return
        self.table[address].prepend(key=key, item=value)
        self.size += 1
        if self.should_resize:
            self.rebuild(self.bin_count*2)

    def __delitem__(self, key):
        # TODO
        address = self._address(key)
        self.table[address].remove(key, lambda node, key: node.key == key)
        self.size -= 1

    def __contains__(self, key):
        # TODO
        address = self._address(key)
        for node in self.table[address]:
            if node.key == key:
                return True
        return False

    def __len__(self):
        # TODO
        return self.size

    def _address(self, key):
        return self.hash(key) % self.bin_count

    def display(self):
        # TODO: Return a string showing the table with multiple lines
        # TODO: I want the string to show which items are in which bins
        print("{")
        for index, linked_list in enumerate(self.table):
            print("\t[{BIN}]=> {LIST}".format(BIN=index, LIST=linked_list))
        print("}")


m = ChainedHashDict()
from random import randrange
for _ in range(100):
    m[randrange(-100, 100)] = randrange(-100, 100)
# m.display()
for i in m.items():
    print(i)
print(len(m))
