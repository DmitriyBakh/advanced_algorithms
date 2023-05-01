class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.tree = [0] * (2 * self.n)
        self.build(array)

    def build(self, array):
        for i, x in enumerate(array):
            self.tree[self.n + i] = x
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, i, value):
        i += self.n
        self.tree[i] = value
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def get_sum(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                res += self.tree[r]
            l //= 2
            r //= 2
        return res

def perform_queries(array, queries):
    tree = SegmentTree(array)
    results = []
    for query in queries:
        if query[0] == 'get_sum':
            results.append(tree.get_sum(query[1], query[2]))
        elif query[0] == 'update':
            tree.update(query[1], query[2])
    return results

array = [10, 2, 3, 4, 5]
queries = [('get_sum', 0, 2), ('update', 3, 10), ('get_sum', 2, 5)]
print(perform_queries(array, queries))  # Output: [12, 18]