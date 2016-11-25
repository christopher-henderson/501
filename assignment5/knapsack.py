from time import time


def knapsack(max_size, items):
    known = [None for _ in range(max_size + 1)]
    known[0] = 0

    def knapsack_closure(size):
        known[size] = known[size] if known[size] is not None else max(
            item[1] + knapsack_closure(size - item[0]) if
            size - item[0] >= 0 else 0
            for item in items)
        return known[size]
    return knapsack_closure(max_size)

    # def knapsack_closure(size):
    #     known[size] = known[size] if known[size] is not None else max(
    #         item[1] + knapsack_closure(size - item[0]) if
    #         size - item[0] >= 0 else 0
    #         for item in items)
    #     return known[size]
    # return knapsack_closure(max_size)

# items = ((12, 4), (2, 2), (1, 2), (1, 1), (4, 10))
# print (knapsack(8, items))

# items = ((2, 3), (3, 4), (4, 5), (5, 8), (9, 10))
# start = time()
# print(knapsack(20, items))
# print(time() - start)

# items = ((10, 60), (20, 100), (30, 120))
# print(knapsack(50, items))
# items = (
#     (1, 8),
#     (2, 4),
#     (3, 0),
#     (2, 5),
#     (2, 3),
#     )


items = (
    (12, 14),
    (7, 13),
    (11, 23),
    (8, 15),
    (9, 16)
    )
print(knapsack(26, items))
