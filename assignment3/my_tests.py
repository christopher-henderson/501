#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Testing file for assignment 3."""

from christopher_henderson import BinarySearchTreeDict
from christopher_henderson import ChainedHashDict
from christopher_henderson import OpenAddressHashDict
from christopher_henderson import SinglyLinkedList

from itertools import chain
from random import randrange
from random import shuffle
from types import FunctionType


def test_linked_list_empty():
    """test_linked_list_empty."""
    ll = SinglyLinkedList()
    for _ in ll:
        raise AssertionError("Collection should be empty, iterator returned.")
    assert not any(value in ll for value in range(-100, 100))
    assert ll.remove(5) is None
    assert len(ll) is 0
    print("No items, ", ll)
    print("Passed all tests for empty linked list.")


def test_linked_list_single_item():
    """test_linked_list_single_item."""
    ll = SinglyLinkedList()
    ll.prepend(5)
    assert ll.head.item is 5
    print("One item, ", ll)
    for node in ll:
        assert node is 5
    assert 5 in ll
    assert not any(value in ll for value in range(-100, 100) if value is not 5)
    assert len(ll) is 1
    assert ll.remove(5) is 5
    assert 5 not in ll
    assert len(ll) is 0
    for _ in ll:
        raise AssertionError("Collection should be empty, iterator returned.")
    print("Passed all tests for single item in linked list")


def test_linked_list_many_items():
    """test_linked_list_many_items."""
    ll = SinglyLinkedList()
    numbers = [value for value in range(-100, 100)]
    for number in numbers:
        ll.prepend(number)
    print("Many items, ", ll)
    assert len(ll) == len(numbers)
    assert [node.item for node in ll.nodes()] == numbers[-1::-1]
    assert all(number in ll for number in numbers)
    assert not any(
        number in ll for number in chain(range(-200, -100), range(100, 200)))
    assert ll.remove(500) is None
    assert all(ll.remove(value) is not None for value in numbers)
    assert not any(number in ll for number in numbers)
    assert len(ll) is 0
    for _ in ll:
        raise AssertionError("Collection should be empty, iterator returned.")
    print("Passed all tests for single item in linked list")


def test_bst_empty():
    """test_bst_empty."""
    bst = BinarySearchTreeDict()
    assert len(bst) is 0
    assert not any(number in bst for number in range(-100, 100))
    for _ in bst.inorder_keys():
        raise Exception("Collection should be empty, iterator returned.")
    for _ in bst.preorder_keys():
        raise Exception("Collection should be empty, iterator returned.")
    for _ in bst.postorder_keys():
        raise Exception("Collection should be empty, iterator returned.")
    assert bst[0] is None
    bst.__delitem__(0) is None
    assert len(bst) is 0
    assert bst.height is -1
    print(bst)


def test_bst_one_item():
    """test_bst_one_item."""
    bst = BinarySearchTreeDict()
    bst[0] = 1
    assert bst[0] is 1
    assert len(bst) is 1
    assert bst.height is 0
    assert bst[1] is None
    print(bst)
    del bst[0]
    assert len(bst) is 0
    assert 0 not in bst


def test_bst_many_items():
    """test_bst_many_items."""
    bst = BinarySearchTreeDict()
    pairs = [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5], ['f', 6]]
    for key, value in pairs:
        bst[key] = value
    print(bst)
    assert len(bst) == len(pairs)
    assert bst.height == len(pairs) - 1
    assert all(key in bst and bst[key] == value for key, value in pairs)
    assert [[k, bst[k]] for k in bst.inorder_keys()] == pairs
    assert [[k, bst[k]] for k in bst.preorder_keys()] == pairs
    assert [[k, bst[k]] for k in bst.postorder_keys()] == pairs[-1::-1]
    del bst['d']
    print(bst)
    assert len(bst) == len(pairs) - 1
    assert bst.height == len(pairs) - 2
    assert all(
        key in bst and bst[key] == value for key, value in pairs if key != 'd')

    print("Mutating existing keys.")
    incremented_pairs = [[k, v + 1] for k, v in pairs]
    for key, value in incremented_pairs:
        bst[key] = value
    print(bst)
    assert len(bst) == len(incremented_pairs)
    assert all(
        key in bst and bst[key] == value for key, value in incremented_pairs)

    print("Shuffling input")
    for k, _ in incremented_pairs:
        del bst[k]
    assert len(bst) is 0
    shuffled = incremented_pairs
    shuffle(shuffled)
    for key, value in shuffled:
        bst[key] = value
    print(bst)
    assert len(bst) == len(shuffled)
    assert all(
        key in bst and bst[key] == value for key, value in shuffled)


def test_chained_hash_dict_empty():
    """test_chained_hash_dict_empty."""
    chd = ChainedHashDict()
    print(chd)
    assert len(chd) is 0
    for _ in chd:
        raise Exception("Collection should be empty, iterator returned.")
    assert chd.__delitem__(0) is None
    assert chd[0] is None
    print("Passed empty ChainedHashDict")


def test_chained_hash_dict_one_item():
    """test_chained_hash_dict_one_item."""
    chd = ChainedHashDict()
    chd[0] = 1
    print(chd)
    for k, v in chd:
        assert k is 0 and v is 1
    assert len(chd) is 1
    chd[0]
    assert chd[10] is None
    del chd[0]
    assert len(chd) is 0
    for _, _ in chd:
        raise Exception("Collection should be empty, iterator returned.")
    print("Passed single item ChainedHashDict")


def test_chained_hash_dict_many_items():
    """test_chained_hash_dict_many_items."""
    chd = ChainedHashDict()
    test_dict = dict()
    for key in (randrange(-100, 100) for _ in range(1000)):
        value = randrange(-100, 100)
        chd[key] = value
        test_dict[key] = value
    assert len(chd) == len(test_dict)
    for k, v in test_dict.items():
        assert chd[k] == v
    print(chd)
    print("Passed many item ChainedHashDict")


def test_chained_hash_dict_bad_hash():
    """test_chained_hash_dict_bad_hash."""
    chd = ChainedHashDict(hashfunc=terrible_hash(5))
    test_dict = dict()
    for key in (randrange(-100, 100) for _ in range(1000)):
        value = randrange(-100, 100)
        chd[key] = value
        test_dict[key] = value
    assert len(chd) == len(test_dict)
    for k, v in test_dict.items():
        assert chd[k] == v
    print(chd)
    print("Passed bad hash ChainedHashDict")


def test_chained_hash_dict_low_load_factor():
    """test_chained_hash_dict_low_load_factor."""
    oad = ChainedHashDict(max_load=0.1)
    test_dict = dict()
    for key in (randrange(-100, 100) for _ in range(1000)):
        value = randrange(-100, 100)
        oad[key] = value
        test_dict[key] = value
    assert len(oad) == len(test_dict)
    for k, v in test_dict.items():
        assert oad[k] == v
    print(oad)
    print("Passed low load OpenAddressHashDict")


def test_chained_hash_dict_del():
    """test_chained_hash_dict_del."""
    oad = ChainedHashDict()
    test_dict = dict()
    for key in (randrange(-100, 100) for _ in range(1000)):
        value = randrange(-100, 100)
        oad[key] = value
        test_dict[key] = value
    num_deleted = 0
    deleted = dict()
    keys = [k for k in test_dict.keys()]
    for key in keys:
        deleted[key] = test_dict[key]
        del test_dict[key]
        del oad[key]
        num_deleted += 1
        if num_deleted >= 500:
            break
    assert len(oad) == len(test_dict)
    for k, v in test_dict.items():
        assert oad[k] == v
    for k, v in deleted.items():
        assert k not in oad
    for k, v in deleted.items():
        oad[k] = v
        test_dict[k] = v
    assert len(oad) == len(test_dict)
    for k, v in test_dict.items():
        assert oad[k] == v
    print(oad)
    print("Passed OpenAddressHashDict deletion.")


def test_open_addressed_dict_empty():
    """test_open_addressed_dict_empty."""
    oad = OpenAddressHashDict()
    print(oad)
    assert len(oad) is 0
    for _ in oad:
        raise Exception("Collection should be empty, iterator returned.")
    assert oad.__delitem__(0) is None
    assert oad[0] is None
    print("Passed empty OpenAddressHashDict")


def test_open_addressed_dict_one_item():
    """test_open_addressed_dict_one_item."""
    oad = OpenAddressHashDict()
    oad[0] = 1
    print(oad)
    for k, v in oad:
        assert k is 0 and v is 1
    assert len(oad) is 1
    oad[0]
    assert oad[10] is None
    del oad[0]
    assert len(oad) is 0
    for _, _ in oad:
        raise Exception("Collection should be empty, iterator returned.")
    print("Passed single item OpenAddressHashDict")


def test_open_addressed_dict_many_items():
    """test_open_addressed_dict_many_items."""
    oad = OpenAddressHashDict()
    test_dict = dict()
    for key in (randrange(-100, 100) for _ in range(1000)):
        value = randrange(-100, 100)
        oad[key] = value
        test_dict[key] = value
    assert len(oad) == len(test_dict)
    for k, v in test_dict.items():
        assert oad[k] == v
    print(oad)
    print("Passed many item OpenAddressHashDict")


def test_open_addressed_dict_bad_hash():
    """test_open_addressed_dict_bad_hash."""
    oad = OpenAddressHashDict(hashfunc=terrible_hash(5))
    test_dict = dict()
    for key in (randrange(-100, 100) for _ in range(1000)):
        value = randrange(-100, 100)
        oad[key] = value
        test_dict[key] = value
    assert len(oad) == len(test_dict)
    for k, v in test_dict.items():
        assert oad[k] == v
    print(oad)
    print("Passed bad hash OpenAddressHashDict")


def test_open_addressed_dict_low_load_factor():
    """test_open_addressed_dict_low_load_factor."""
    oad = OpenAddressHashDict(max_load=0.1)
    test_dict = dict()
    for key in (randrange(-100, 100) for _ in range(1000)):
        value = randrange(-100, 100)
        oad[key] = value
        test_dict[key] = value
    assert len(oad) == len(test_dict)
    for k, v in test_dict.items():
        assert oad[k] == v
    print(oad)
    print("Passed low load OpenAddressHashDict")


def test_open_addressed_dict_del():
    """test_open_addressed_dict_del."""
    oad = OpenAddressHashDict()
    test_dict = dict()
    for key in (randrange(-100, 100) for _ in range(1000)):
        value = randrange(-100, 100)
        oad[key] = value
        test_dict[key] = value
    num_deleted = 0
    deleted = dict()
    keys = [k for k in test_dict.keys()]
    for key in keys:
        deleted[key] = test_dict[key]
        del test_dict[key]
        del oad[key]
        num_deleted += 1
        if num_deleted >= 500:
            break
    assert len(oad) == len(test_dict)
    for k, v in test_dict.items():
        assert oad[k] == v
    for k, v in deleted.items():
        assert k not in oad
    for k, v in deleted.items():
        oad[k] = v
        test_dict[k] = v
    assert len(oad) == len(test_dict)
    for k, v in test_dict.items():
        assert oad[k] == v
    print(oad)
    print("Passed OpenAddressHashDict deletion.")


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
    """Main test function.

    Emulates nosetests. Searches the global dictionary for functions that
    start with "test" and executes them.
    """
    tests = [
        f for name, f in sorted(globals().items()) if
        isinstance(f, FunctionType) and
        name.startswith("test")
        ]
    for test in tests:
        test()


if __name__ == '__main__':
    main()
