class SinglyLinkedNode(object):

    def __init__(self, key=None, item=None, next_link=None):
        super(SinglyLinkedNode, self).__init__()
        self._key = key
        self._item = item
        self._next = next_link

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __nonzero__(self):
        return self.item is not None

    def __bool__(self):
        return self.__nonzero__()

    def __repr__(self):
        return repr(self.item)


class SinglyLinkedList(object):

    def __init__(self):
        super(SinglyLinkedList, self).__init__()
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __contains__(self, item):
        for node in self:
            if node.item == item:
                return True
        return False

    def remove(self, obj, comparator=lambda node, obj: node.item == obj):
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
        return None

    def prepend(self, item, key=None):
        node = SinglyLinkedNode(item=item, key=key)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def __repr__(self):
        return "List: " + " -> ".join([str(item) for item in self])
