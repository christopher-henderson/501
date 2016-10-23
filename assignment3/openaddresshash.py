# -*- coding: utf-8 -*-
"""Assignment 3 Open Addressed Hashing Dictionary."""
from __future__ import division


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
        self.hash = hash
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
        address = self.address(key)
        pair = self.table[address]
        while pair is not EMPTY:
            if pair.key == key:
                return pair.value
            address = (address + 1) % self.bin_count
            pair = self.table[address]
        raise KeyError("{KEY} not found.".format(KEY=key))

    def __setitem__(self, key, value):
        """__setitem__."""
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
            self.rebuild(self.bin_count * 2)

    def __delitem__(self, key):
        """__delitem__."""
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
        """__contains__."""
        try:
            self[key]
        except Exception:
            return False
        else:
            return True

    def __len__(self):
        """__len__."""
        return self.size

    def address(self, key):
        """address."""
        return self.hash(key) % self.bin_count

    def display(self):
        """display."""
        print(str(self))

    def __str__(self):
        """__str__."""
        string = "{\n"
        for index, pair in enumerate(self.table):
            string += "\t[{BIN}]=> {PAIR}\n".format(
                BIN=index,
                PAIR=(
                    pair if isinstance(pair, Pair) else
                    "DELETED" if pair is DELETED else "EMPTY"))
        string += "}"
        return string
