class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.tree = [0] * (4 * self.n)
        self.build(array, 1, 0, self.n)

    def build(self, array, x, lx, rx):
        if rx - lx == 1:
            if lx < len(array):
                self.tree[x] = array[lx]
            return
        m = (lx + rx) // 2
        self.build(array, x * 2, lx, m)
        self.build(array, x * 2 + 1, m, rx)
        self.tree[x] = self.tree[x * 2] + self.tree[x * 2 + 1]

    def _get_sum(self, l, r, x, lx, rx):
        if l >= rx or r <= lx:
            return 0
        if l <= lx and r >= rx:
            return self.tree[x]
        m = (lx + rx) // 2
        left_sum = self._get_sum(l, r, x * 2, lx, m)
        right_sum = self._get_sum(l, r, x * 2 + 1, m, rx)
        return left_sum + right_sum

    def get_sum(self, l, r):
        return self._get_sum(l, r, 1, 0, self.n)

    def _update(self, i, value, x, lx, rx):
        if lx > i or rx <= i:
            return
        if rx - lx == 1:
            self.tree[x] = value
            return
        m = (lx + rx) // 2
        self._update(i, value, x * 2, lx, m)
        self._update(i, value, x * 2 + 1, m, rx)
        self.tree[x] = self.tree[x * 2] + self.tree[x * 2 + 1]

    def update(self, i, value):
        self._update(i, value, 1, 0, self.n)

    def _multiply_range(self, l, r, value, x, lx, rx):
        if l >= rx or r <= lx:
            return
        if rx - lx == 1:
            self.tree[x] *= value
            return
        m = (lx + rx) // 2
        self._multiply_range(l, r, value, x * 2, lx, m)
        self._multiply_range(l, r, value, x * 2 + 1, m, rx)
        self.tree[x] = self.tree[x * 2] + self.tree[x * 2 + 1]

    def multiply_range(self, l, r, value):
        self._multiply_range(l, r, value, 1, 0, self.n)

def perform_queries(array, queries):
    tree = SegmentTree(array)
    results = []

    for query in queries:
        if query[0] == 'get_sum':
            results.append(tree.get_sum(query[1], query[2]))
        elif query[0] == 'update':
            tree.update(query[1], query[2])
        elif query[0] == 'multiply_range':
            tree.multiply_range(query[1], query[2], query[3])
    return results

array = [10, 2, 3, 4, 5]
queries = [('get_sum', 0, 2), ('multiply_range', 3, 5, 10), ('update', 3, 10), ('get_sum', 2, 5)]
print(perform_queries(array, queries)) # Result: [12, 63]
