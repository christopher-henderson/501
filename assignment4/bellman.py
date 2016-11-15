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

    def __str__(self):
        return "({U}, {V}, {W})".format(U=self.u.value, V=self.v.value, W=self.weight)

    def __repr__(self):
        return self.__str__()

    def __unicode__(self):
        return self.__str__()

s = V('s', 0)
t = V('t')
y = V('y')
x = V('x')
z = V('z')

s.vertices = [
    Edge(s, t, 6),
    Edge(s, y, 7),
    ]

t.vertices = [
    Edge(t, y, 8),
    Edge(t, x, 5),
    Edge(t, z, -4),
    ]

y.vertices = [
    Edge(y, x, -3),
    Edge(y, z, 9),
    ]

x.vertices = [
    Edge(x, t, -2),
    ]

z.vertices = [
    Edge(z, x, 7),
    Edge(z, s, 2),
    ]

G = {
    'V': [s, t, y, x, z],
    'E': [Edge(t, x, 5),
          Edge(t, y, 8),
          Edge(t, z, -4),

          Edge(x, t, -2),

          Edge(y, x, -3),
          Edge(y, z, 9),

          Edge(z, x, 7),
          Edge(z, s, 2),

          Edge(s, t, 6),
          Edge(s, y, 7),

          ]
    }


def bell(G, s):
    for _ in range(1, len(G['V'])):
        for edge in G['E']:
            relax(edge)
        print(G['V'])
    # E = [Edge(x.parent, x, x.weight) for x in G['V'] if x.parent is not None]
    for edge in G['E']:
        # print (edge.v.weight, edge.u.weight, edge.weight)
        if edge.v.weight > edge.u.weight + edge.weight:
            return False
    return True

# def bell(G, s):
#     S = set()
#     Q = G
#     heapify(Q['V'])
#     while len(Q['V']) is not 0:
#         # print(S)
#         u = heappop(Q['V'])
#         S = S.union(set([u]))
#         for e in u.vertices:
#             relax(e)
#         heapify(Q['V'])
#     # print (S)
#     for edge in G['E']:
#         if edge.v.weight > edge.u.weight + edge.weight:
#             return False
#     return True

def relax(edge):
    # print(edge.u.weight, edge.v.weight, edge.weight,)
    if edge.u.weight + edge.weight < edge.v.weight:
        edge.v.weight = edge.u.weight + edge.weight
        edge.v.parent = edge.u
        return True
    return False


print(bell(G, s))
print(G['V'])
