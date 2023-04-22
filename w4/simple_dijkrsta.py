""" Have some practice with Dijkstra algorithm, get the shortest path between two vertices in weighted undirected graph without negative edges.

Implement function

def solve(

    adj_node_weight_lists: 'List[List[Tuple[int, float]]]',
    src_node: int,
    dst_node: int,

) -> float

returning the shortest path from src_node to dst_node. You can iterate the adjacency lists like this

for node, adj_node_weight_list in enumerate(adj_node_weight_lists):
    for adj_node, weight in adj_node_weight_list:
where 0 <= adj_node < len(adj_node_weight_lists).

Example (a triangle):

adj_node_weight_lists = [[(1, 10), (2, 40)], [(0, 10), (2, 20)], [(0, 40), (1, 20)]]
src_node = 0
dst_node = 2

the best path is 0-1-2 with total distance 10+20=30 so the answer is 30 """

def solve(adj_node_weight_lists, src_node, dst_node):
    # Dijkstra algorithm
    # initialize
    n = len(adj_node_weight_lists)
    dist = [float('inf')] * n
    dist[src_node] = 0
    visited = [False] * n
    # loop
    for _ in range(n):
        # find the nearest node
        min_dist = float('inf')
        min_node = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_node = i
        # update dist
        for adj_node, weight in adj_node_weight_lists[min_node]:
            if not visited[adj_node] and dist[min_node] + weight < dist[adj_node]:
                dist[adj_node] = dist[min_node] + weight
        # mark as visited
        visited[min_node] = True
    return dist[dst_node]
    
print(solve([[(1, 10), (2, 40)], [(0, 10), (2, 20)], [(0, 40), (1, 20)]], 0, 2))
