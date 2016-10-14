from __future__ import division

from linked_list import SinglyLinkedNode


class DELETED(object):

    class key(object):
        pass

    class value(object):
        pass


class EMPTY(object):

    class key(object):
        pass

    class value(object):
        pass


class Pair(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


    def __str__(self):
        return "Key: {K}, Value: {V}".format(K=self.key, V=self.value)

class OpenAddressHashDict(object):

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(OpenAddressHashDict, self).__init__()
        if bin_count <= 0:
            raise TypeError("Bin count must be greater than zero.")
        self.table = [EMPTY for _ in range(bin_count)]
        self.max_load = max_load
        self.hash = hash
        self.size = 0

    @property
    def load_factor(self):
        # TODO
        return self.size / self.bin_count

    @property
    def bin_count(self):
        # TODO
        return len(self.table)

    def rebuild(self, bincount):
        # Rebuild this hash table with a new bin count
        # TODO
        tmp = self.table
        self.table = [EMPTY for _ in range(bincount)]
        self.size = 0
        for pair in (p for p in tmp if isinstance(p, Pair)):
            self[pair.key] = pair.value
        del tmp

    @property
    def should_rebuild(self):
        return self.load_factor >= self.max_load

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        address = self.address(key)
        pair = self.table[address]
        while pair is not EMPTY:
            if pair.key == key:
                return pair.value
            address = (address + 1) % self.bin_count
            pair = self.table[address]
        raise KeyError()

    def __setitem__(self, key, value):
        address = self.address(key)
        pair = self.table[address]
        while pair is not EMPTY and pair is not DELETED:
            if pair.key == key:
                pair.value = value
                return
            address = (address + 1) % self.bin_count
            pair = self.table[address]
        self.table[address] = Pair(key, value)
        self.size += 1
        if self.should_rebuild:
            self.rebuild(self.bin_count*2)

    def __delitem__(self, key):
        # TODO
        address = self.address(key)
        pair = self.table[address]
        while pair is not EMPTY:
            if pair.key == key:
                self.table[address] = DELETED
                self.size -= 1
                return
            address = (address + 1) % self.bin_count
            pair = self.table[address]
        raise KeyError()

    def __contains__(self, key):
        # TODO
        try:
            self[key]
        except:
            return False
        else:
            return True

    def __len__(self):
        # TODO
        return self.size

    def address(self, key):
        return self.hash(key) % self.bin_count

    def display(self):
        print (str(self))

    def __str__(self):
        # TODO: Return a string showing the table with multiple lines
        # TODO: I want the string to show which items are in which bins
        string = "{\n"
        for index, pair in enumerate(self.table):
            string += "\t[{BIN}]=> {PAIR}\n".format(
                BIN=index,
                PAIR=(
                    pair if isinstance(pair, Pair) else
                    "DELETED" if pair is DELETED else "EMPTY"))
        string += "}"
        return string

m = OpenAddressHashDict()
for i in range(20):
    m[i] = i
print(m.size)

# m[1] = 1
# del m[1]
# print(len(m))
# m.display()
# m[1] = 1
# m.display()
# print(len(m))

# from random import randrange
# keys = set()
# for i in range(100):
#     if i and i % 5 is 0:
#         del m[keys.pop()]
#     else:
#         key = randrange(-100, 100)
#         m[key] = randrange(-100, 100)
#         keys.add(key)
# m.display()
# print (len(m))
