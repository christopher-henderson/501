import sys
from heapq import heapify, heappop


class V(object):

    def __init__(self, value, weight=sys.maxsize, parent=None):
        self.value = value
        self.weight = weight
        self.parent = parent
        self.vertices = []

    def __str__(self):
        return "({V}, {W}, {P})".format(V=self.value, W=self.weight, P=self.parent.value if self.parent else "None")

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __ge__(self, other):
        return self.weight >= other.weight


class Edge(object):

    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

s = V('s', 0)
t = V('t')
y = V('y')
x = V('x')
z = V('z')

s.vertices = [
    Edge(s, t, 3),
    Edge(s, y, 5),
    ]

t.vertices = [
    Edge(t, y, 2),
    Edge(t, x, 6),
    ]

y.vertices = [
    Edge(y, t, 1),
    Edge(y, x, 4),
    Edge(y, z, 6),
    ]

x.vertices = [
    Edge(x, z, 2),
    ]

z.vertices = [
    Edge(z, x, 7),
    Edge(z, s, 3),
    ]

G = [s, t, y, x, z]


def dijkstra(G, s):
    S = set()
    Q = [v for v in G]
    heapify(Q)
    while len(Q) is not 0:
        u = heappop(Q)
        S = S.union(set([u]))
        for e in u.vertices:
            relax(e)
        heapify(Q)
        print(S)
    return S


def relax(edge):
    if edge.u.weight + edge.weight < edge.v.weight:
        edge.v.weight = edge.u.weight + edge.weight
        edge.v.parent = edge.u
    # if w + u.weight < v.weight:
    #     v.weight = w
    #     v.parent = u


dijkstra(G, s)
