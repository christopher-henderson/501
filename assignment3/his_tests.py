from sys import exit
from bst import BinarySearchTreeDict
from chained_hash_dict import ChainedHashDict
from linked_list import SinglyLinkedList
from openaddresshash import OpenAddressHashDict

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


def testFunc():
    i = 1

    print ("For SinglyLinkedList ----------------")
    SLL = SinglyLinkedList()

    # 1
    if not SLL.__len__()==0:
        print ("failed test case ",i)
    else:
        print ("passed test case ",i)
    i += 1

    # 2
    if SLL.remove(12):
        print ("failed test case ",i)
    else:
        print ("passed test case ",i)
    i += 1

    # 3
    if SLL.prepend(12):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 4
    if SLL.remove(12):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 5
    if not SLL.__contains__(12):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 6
    if not SLL.__len__()==0:
        print ("failed test case ",i)
    else:
        print ("passed test case ",i)
    i += 1

    SLL.prepend(1)
    SLL.prepend(23)
    SLL.prepend(65)

    # 7
    if SLL.__repr__() == "List:65->23->1":
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 8
    strSLL = [s for s in SLL]
    if strSLL == [65, 23, 1]:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    print ("For BinarySearchTreeDict ----------------")
    BSTH = BinarySearchTreeDict()

    # 9
    if BSTH.__len__()==0 and BSTH.height==-1:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 10
    if not BSTH.__delitem__(12):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 11
    if BSTH.__setitem__(10,"X"):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 12
    if not BSTH.__setitem__(None, "qwerty"):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    BSTH.__setitem__(5,"V")
    BSTH.__setitem__(3,"III")
    BSTH.__setitem__(8,"VIII")
    BSTH.__setitem__(1,"I")
    BSTH.__setitem__(4,"VI")
    BSTH.__setitem__(16,"XVI")
    BSTH.__setitem__(13,"XIII")
    BSTH.__setitem__(21,"XXI")
    BSTH.__setitem__(17,"XVII")
    BSTH.__setitem__(26,"XXVI")
    BSTH.__setitem__(18,"XVIII")
    BSTH.__setitem__(19,"XIX")

    # 13
    print(BSTH.height)
    if BSTH.height == 5 and BSTH.length == 13:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 14
    temp = [t for t in BSTH.inorder_keys()]
    if temp == [1, 3, 4, 5, 8, 10, 13, 16, 17, 18, 19, 21, 26]:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 15
    if BSTH.__contains__(8):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 16
    if not BSTH.__contains__(2):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 17
    if not BSTH.__delitem__(None):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 18
    if BSTH.__delitem__(17) and BSTH.height == 4:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 19
    temp = [t for t in BSTH.preorder_keys()]
    if temp == [10, 5, 3, 1, 4, 8, 16, 13, 21, 18, 19, 26]:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 20
    if not BSTH.__delitem__(17):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 21
    if BSTH.__delitem__(10) and BSTH.height == 4:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 22
    temp = [t for t in BSTH.postorder_keys()]
    if temp == [1, 4, 3, 8, 5, 19, 18, 26, 21, 16, 13]:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 23
    temp = [t for t in BSTH._items()]
    if temp == [[1, 'I'], [3, 'III'], [4, 'VI'], [5, 'V'], [8, 'VIII'], [13, 'XIII'], [16, 'XVI'], [18, 'XVIII'], [19, 'XIX'], [21, 'XXI'], [26, 'XXVI']]:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 24
    if BSTH.display()==['Inorder:1->3->4->5->8->13->16->18->19->21->26', 'Preorder:13->5->3->1->4->8->16->21->18->19->26']:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    print ("For ChainedHashDict ----------------")
    CHD = ChainedHashDict(10,0.7)

    # 25
    if CHD.load_factor == 0 and CHD.bin_count == 10 and CHD.len==0:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 26
    if CHD.__setitem__(11,"XI"):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 27
    if not CHD.__setitem__(None,"XXII"):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    CHD.__setitem__(1,"I")

    # 28
    temp = CHD.display()
    eqs = "0List:\n1List:[1, 'I']->[11, 'XI']\n2List:\n3List:\n4List:\n5List:\n6List:\n7List:\n8List:\n9List:"
    if temp == eqs:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    CHD.__setitem__(10,"X")
    CHD.__setitem__(22,"XXII")
    CHD.__setitem__(143,"CXLIII")
    CHD.__setitem__(12,"XII")
    CHD.__setitem__(21,"XXI")
    CHD.__setitem__(20,"XX")
    CHD.__setitem__(32,"XXXII")
    CHD.__setitem__(31,"XXXI")

    # 29
    if CHD.load_factor == 0.5:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 30
    if CHD.__getitem__(10) == "X":
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 31
    if CHD.__getitem__(100) == None:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 32
    if CHD.__getitem__(None) == None:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 33
    CHD.rebuild(30)
    if CHD.load_factor == 1.0/3:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 34
    CHD.__setitem__(10,"ten")
    if(CHD.__getitem__(10)=="ten") and CHD.__len__()==10:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 35
    if CHD.__delitem__(10) and CHD.__len__()==9 and not CHD.__delitem__(10) and not CHD.__delitem__(None):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 36
    if not CHD.__contains__(10):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 37
    badCHD = ChainedHashDict(5,0.8, terrible_hash(5))
    badCHD.__setitem__(1,"I")
    badCHD.__setitem__(12,"XII")
    badCHD.__setitem__(134,"CXXXIV")
    temp = badCHD.display()
    eqs = "0List:[134, 'CXXXIV']->[12, 'XII']->[1, 'I']\n1List:\n2List:\n3List:\n4List:"
    if temp == eqs:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    CHD = None
    print ("For OpenAddressHashDict ----------------")
    OAHD = OpenAddressHashDict(10,0.7)

    # 38
    if OAHD.load_factor == 0 and OAHD.bin_count == 10 and OAHD.len==0:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 39
    if OAHD.__setitem__(11,"XI"):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 40
    if not OAHD.__setitem__(None,"XXII"):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    OAHD.__setitem__(1,"I")

    # 41
    temp = OAHD.display()
    eqs = "bin 0: [None, None]\nbin 1: [11, 'XI']\nbin 2: [1, 'I']\nbin 3: [None, None]\nbin 4:" \
          " [None, None]\nbin 5: [None, None]\nbin 6: [None, None]\nbin 7: [None, None]\nbin 8: " \
          "[None, None]\nbin 9: [None, None]"
    if temp == eqs:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    OAHD.__setitem__(10,"X")
    OAHD.__setitem__(22,"XXII")
    OAHD.__setitem__(143,"CXLIII")
    OAHD.__setitem__(12,"XII")
    OAHD.__setitem__(21,"XXI")
    OAHD.__setitem__(20,"XX")
    OAHD.__setitem__(32,"XXXII")
    OAHD.__setitem__(31,"XXXI")

    # 42
    if OAHD.load_factor == 0.5:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 43
    if OAHD.__getitem__(10) == "X":
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 44
    if OAHD.__getitem__(100) == None:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 45
    if OAHD.__getitem__(None) == None:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 46
    OAHD.rebuild(30)
    if OAHD.load_factor == 1.0/3:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 47
    OAHD.__setitem__(10,"ten")
    if(OAHD.__getitem__(10)=="ten") and OAHD.__len__()==10:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 48
    if OAHD.__delitem__(10) and OAHD.__len__()==9 and not OAHD.__delitem__(10) and not OAHD.__delitem__(None):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 49
    if not OAHD.__contains__(10):
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1

    # 50
    badOAHD = OpenAddressHashDict(5,0.8, terrible_hash(5))
    badOAHD.__setitem__(1,"I")
    badOAHD.__setitem__(12,"XII")
    badOAHD.__setitem__(134,"CXXXIV")
    temp = badOAHD.display()
    eqs = "bin 0: [1, 'I']\nbin 1: [12, 'XII']\nbin 2: [134, 'CXXXIV']\nbin 3: [None, None]\nbin 4: [None, None]"
    if temp == eqs:
        print ("passed test case ",i)
    else:
        print ("failed test case ",i)
    i += 1
    print(temp)

testFunc()
