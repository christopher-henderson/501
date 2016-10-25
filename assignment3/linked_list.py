#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assignment 3 Singly Linked List."""


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
        for node in self:
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
