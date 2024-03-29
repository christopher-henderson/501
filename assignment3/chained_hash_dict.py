#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assignment 3 Chained Hashing Dictionary."""
from __future__ import division

from linked_list import SinglyLinkedList


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
            for node in linked_list:
                self[node.key] = node.item
        del tmp

    def items(self):
        """items."""
        yield from self

    def __iter__(self):
        """__iter__."""
        for linked_list in self.table:
            for node in linked_list:
                yield node.key, node.item

    def __getitem__(self, key):
        """__getitem__."""
        address = self._address(key)
        chain = self.table[address]
        for node in chain:
            if node.key == key:
                return node.item
        raise KeyError("{KEY} not found.".format(KEY=key))

    def __setitem__(self, key, value):
        """__setitem__."""
        address = self._address(key)
        for node in self.table[address]:
            if node.key == key:
                node.item = value
                return
        self.table[address].prepend(key=key, item=value)
        self.size += 1
        if self.should_resize:
            self.rebuild(self.bin_count * 2)

    def __delitem__(self, key):
        """__delitem__."""
        address = self._address(key)
        self.table[address].remove(
            key,
            lambda node, key: node.key == key,
            fail=True)
        self.size -= 1

    def __contains__(self, key):
        """__contains__."""
        address = self._address(key)
        for node in self.table[address]:
            if node.key == key:
                return True
        return False

    def __len__(self):
        """__len__."""
        return self.size

    def __str__(self):
        """__str__."""
        string = "{\n"
        for index, linked_list in enumerate(self.table):
            string += "\t[{BIN}]=> {LIST}\n".format(
                BIN=index, LIST=linked_list)
        return string + "}"

    def __repr__(self):
        """__repr__."""
        return str(self)

    def display(self):
        """display."""
        return str(self)

    def _address(self, key):
        """_address."""
        return self.hash(key) % self.bin_count
