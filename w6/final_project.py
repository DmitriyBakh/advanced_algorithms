class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        # Initialize the segment tree data structures for sum and squared sum
        self.tree_sum = [0] * (4 * self.n)
        self.tree_sq_sum = [0] * (4 * self.n)
        # Initialize the lazy propagation array
        self.lazy = [1] * (4 * self.n)
        # Build the segment tree
        self._build_tree(array, 0, 0, self.n - 1)

    def _build_tree(self, array, v, l, r):
        # Base case: leaf node
        if l == r:
            self.tree_sum[v] = array[l]
            self.tree_sq_sum[v] = array[l] * array[l]
        # Recursive case: internal node
        else:
            mid = (l + r) // 2
            self._build_tree(array, 2 * v + 1, l, mid)
            self._build_tree(array, 2 * v + 2, mid + 1, r)
            # Combine the results of the left and right children
            self.tree_sum[v] = self.tree_sum[2 * v + 1] + self.tree_sum[2 * v + 2]
            self.tree_sq_sum[v] = self.tree_sq_sum[2 * v + 1] + self.tree_sq_sum[2 * v + 2]

    def _propagate(self, v, l, r):
        # Apply the lazy value to the current node and propagate it to the children
        if self.lazy[v] != 1:
            k = self.lazy[v]
            self.tree_sum[v] *= k
            self.tree_sq_sum[v] *= k * k
            if l != r:
                self.lazy[2 * v + 1] *= k
                self.lazy[2 * v + 2] *= k
            # Reset the lazy value of the current node
            self.lazy[v] = 1

    def get_variance(self, l, r):
        # Calculate the sum and squared sum in the given range
        sum_range = self._get_sum(0, 0, self.n - 1, l, r)
        sq_sum_range = self._get_sq_sum(0, 0, self.n - 1, l, r)
        n_elements = r - l + 1
        # Calculate the mean and squared mean
        mean = sum_range / n_elements
        sq_mean = sq_sum_range / n_elements
        # Calculate the variance
        variance = sq_mean - mean * mean
        return variance

    def _get_sum(self, v, tl, tr, l, r):
        # Apply lazy propagation before querying the sum
        self._propagate(v, tl, tr)
        # If the query range is empty, return 0
        if l > r:
            return 0
        # If the query range matches the node range, return the sum of the node
        if l == tl and r == tr:
            return self.tree_sum[v]
        # Otherwise, split the query range and query the left and right children
        tm = (tl + tr) // 2
        left_sum = self._get_sum(2 * v + 1, tl, tm, l, min(r, tm))
        right_sum = self._get_sum(2 * v + 2, tm + 1, tr, max(l, tm + 1), r)
        # Combine the results of the left and right children
        return left_sum + right_sum

    def _get_sq_sum(self, v, tl, tr, l, r):
        # Apply lazy propagation before querying the squared sum
        self._propagate(v, tl, tr)
        # If the query range is empty, return 0
        if l > r:
            return 0
        # If the query range matches the node range, return the squared sum of the node
        if l == tl and r == tr:
            return self.tree_sq_sum[v]
        # Otherwise, split the query range and query the left and right children
        tm = (tl + tr) // 2
        left_sq_sum = self._get_sq_sum(2 * v + 1, tl, tm, l, min(r, tm))
        right_sq_sum = self._get_sq_sum(2 * v + 2, tm + 1, tr, max(l, tm + 1), r)
        # Combine the results of the left and right children
        return left_sq_sum + right_sq_sum

    def update(self, i, value):
        # Update the value at position i
        self._update(0, 0, self.n - 1, i, value)

    def _update(self, v, tl, tr, i, value):
        # Apply lazy propagation before updating the value
        self._propagate(v, tl, tr)
        # Base case: leaf node
        if tl == tr:
            self.tree_sum[v] = value
            self.tree_sq_sum[v] = value * value
        # Recursive case: internal node
        else:
            tm = (tl + tr) // 2
            if i <= tm:
                self._update(2 * v + 1, tl, tm, i, value)
                self._propagate(2 * v + 2, tm + 1, tr)
            else:
                self._propagate(2 * v + 1, tl, tm)
                self._update(2 * v + 2, tm + 1, tr, i, value)
            # Combine the results of the left and right children
            self.tree_sum[v] = self.tree_sum[2 * v + 1] + self.tree_sum[2 * v + 2]
            self.tree_sq_sum[v] = self.tree_sq_sum[2 * v + 1] + self.tree_sq_sum[2 * v + 2]
            self.lazy[2 * v + 1] = 1
            self.lazy[2 * v + 2] = 1

    def multiply_range(self, l, r, k):
        # Multiply all elements in the range [l, r] by k
        self._multiply_range(0, 0, self.n - 1, l, r, k)

    def _multiply_range(self, v, tl, tr, l, r, k):
        # Apply lazy propagation before multiplying the range
        self._propagate(v, tl, tr)
        # If the query range is empty, do nothing
        if l > r:
            return
        # If the query range matches the node range, apply the multiplication
        if l == tl and r == tr:
            self.lazy[v] *= k
            self._propagate(v, tl, tr)
        # Otherwise, split the query range and multiply the left and right children
        else:
            tm = (tl + tr) // 2
            self._multiply_range(2 * v + 1, tl, tm, l, min(r, tm), k)
            self._multiply_range(2 * v + 2, tm + 1, tr, max(l, tm + 1), r, k)
            self.tree_sum[v] = self.tree_sum[2 * v + 1] + self.tree_sum[2 * v + 2]
            self.tree_sq_sum[v] = self.tree_sq_sum[2 * v + 1] + self.tree_sq_sum[2 * v + 2]

def perform_queries(array, queries):
    # Initialize the segment tree with the input array
    tree = SegmentTree(array)
    result = []
    # Process each query
    for query in queries:
        if query[0] == 'get_variance':
            l, r = query[1], query[2]
            result.append(tree.get_variance(l, r - 1))
        elif query[0] == 'update':
            i, x = query[1], query[2]
            tree.update(i, x)
        elif query[0] == 'multiply_range':
            l, r, k = query[1], query[2], query[3]
            tree.multiply_range(l, r - 1, k)

    return result

# Test cases
array = [10, 2, 3, 4, 5]
queries = [('get_variance', 0, 2), ('multiply_range', 3, 5, 10), ('update', 3, 10), ('get_variance', 2, 5)] #Output: [16.0, 428.667]
# queries = [('get_variance', 0, 2), ('update', 3, 10), ('get_variance', 2, 5)] #Output: [16.0, 8,666666667]
# queries = [('get_variance', 0, 2), ('multiply_range', 3, 5, 10), ('get_variance', 2, 5)] #Output: [16.0, 408,6666667]
# queries = [('get_variance', 0, 2), ('multiply_range', 2, 5, 10), ('update', 3, 10), ('get_variance', 2, 5)] #Output: [16.0, 266,6666667]
# queries = [('get_variance', 0, 2), ('multiply_range', 2, 5, 10), ('update', 3, 10), ('update', 0, 5), ('get_variance', 0, 4)] #Output: [16.0, 119,1875]
print(perform_queries(array, queries))
