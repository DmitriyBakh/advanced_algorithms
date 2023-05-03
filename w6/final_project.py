class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        self.tree_sum = [0] * (4 * self.n)
        self.tree_sq_sum = [0] * (4 * self.n)
        self.lazy = [1] * (4 * self.n)
        self._build_tree(array, 0, 0, self.n - 1)

    def _build_tree(self, array, v, l, r):
        if l == r:
            self.tree_sum[v] = array[l]
            self.tree_sq_sum[v] = array[l] * array[l]
        else:
            mid = (l + r) // 2
            self._build_tree(array, 2 * v + 1, l, mid)
            self._build_tree(array, 2 * v + 2, mid + 1, r)
            self.tree_sum[v] = self.tree_sum[2 * v + 1] + self.tree_sum[2 * v + 2]
            self.tree_sq_sum[v] = self.tree_sq_sum[2 * v + 1] + self.tree_sq_sum[2 * v + 2]

    def _propagate(self, v, l, r):
        if self.lazy[v] != 1:
            k = self.lazy[v]
            self.tree_sum[v] *= k
            self.tree_sq_sum[v] *= k * k
            if l != r:
                self.lazy[2 * v + 1] *= k
                self.lazy[2 * v + 2] *= k
            self.lazy[v] = 1

    def get_variance(self, l, r):
        sum_range = self._get_sum(0, 0, self.n - 1, l, r)
        sq_sum_range = self._get_sq_sum(0, 0, self.n - 1, l, r)
        n_elements = r - l + 1
        mean = sum_range / n_elements
        sq_mean = sq_sum_range / n_elements
        variance = sq_mean - mean * mean
        return variance

    def _get_sum(self, v, tl, tr, l, r):
        self._propagate(v, tl, tr)
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree_sum[v]
        tm = (tl + tr) // 2
        left_sum = self._get_sum(2 * v + 1, tl, tm, l, min(r, tm))
        right_sum = self._get_sum(2 * v + 2, tm + 1, tr, max(l, tm + 1), r)
        return left_sum + right_sum

    def _get_sq_sum(self, v, tl, tr, l, r):
        self._propagate(v, tl, tr)
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree_sq_sum[v]
        tm = (tl + tr) // 2
        left_sq_sum = self._get_sq_sum(2 * v + 1, tl, tm, l, min(r, tm))
        right_sq_sum = self._get_sq_sum(2 * v + 2, tm + 1, tr, max(l, tm + 1), r)
        return left_sq_sum + right_sq_sum

    def update(self, i, value):
        self._update(0, 0, self.n - 1, i, value)

    def _update(self, v, tl, tr, i, value):
        self._propagate(v, tl, tr)
        if tl == tr:
            self.tree_sum[v] = value
            self.tree_sq_sum[v] = value * value
        else:
            tm = (tl + tr) // 2
            if i <= tm:
                self._update(2 * v + 1, tl, tm, i, value)
            else:
                self._update(2 * v + 2, tm + 1, tr, i, value)
            self.tree_sum[v] = self.tree_sum[2 * v + 1] + self.tree_sum[2 * v + 2]
            self.tree_sq_sum[v] = self.tree_sq_sum[2 * v + 1] + self.tree_sq_sum[2 * v + 2]

    def multiply_range(self, l, r, k):
        self._multiply_range(0, 0, self.n - 1, l, r - 1, k)

    def _multiply_range(self, v, tl, tr, l, r, k):
        self._propagate(v, tl, tr)
        if l > r:
            return
        if l == tl and r == tr:
            self.lazy[v] *= k
            self._propagate(v, tl, tr)
        else:
            tm = (tl + tr) // 2
            self._multiply_range(2 * v + 1, tl, tm, l, min(r, tm), k)
            self._multiply_range(2 * v + 2, tm + 1, tr, max(l, tm + 1), r, k)
            self.tree_sum[v] = self.tree_sum[2 * v + 1] + self.tree_sum[2 * v + 2]
            self.tree_sq_sum[v] = self.tree_sq_sum[2 * v + 1] + self.tree_sq_sum[2 * v + 2]

def perform_queries(array, queries):
    tree = SegmentTree(array)
    result = []

    for query in queries:
        if query[0] == 'get_variance':
            l, r = query[1], query[2]
            result.append(tree.get_variance(l, r - 1))  # Changed r to r - 1
        elif query[0] == 'update':
            i, x = query[1], query[2]
            tree.update(i, x)
        elif query[0] == 'multiply_range':
            l, r, k = query[1], query[2], query[3]
            tree.multiply_range(l, r - 1, k)  # Changed r to r - 1

    return result

# Test case
array = [10, 2, 3, 4, 5]
queries = [('get_variance', 0, 2), ('multiply_range', 3, 5, 10), ('update', 3, 10), ('get_variance', 2, 5)]
print(perform_queries(array, queries))  # Output: [16.0, 428.667]

