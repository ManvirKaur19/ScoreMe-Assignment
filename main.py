def longest_path(graph: list) -> int:
    n = len(graph)

    # Topological sorting of the graph
    topo_order = topological_sort(graph)

    # Calculating longest path using topological order
    return calculate_longest_path(graph, topo_order)


def topological_sort(graph):
    n = len(graph)
    visited = [False] * n
    stack = []

    def dfs(node):
        visited[node] = True
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    stack.reverse()
    return stack


def calculate_longest_path(graph, topo_order):
    n = len(graph)
    dist = [-float('inf')] * n

    # Initializing the distance for all nodes in topological order to 0
    for node in topo_order:
        if dist[node] == -float('inf'):
            dist[node] = 0

    for u in topo_order:
        if dist[u] != -float('inf'):
            for v, weight in graph[u]:
                if dist[u] + weight > dist[v]:
                    dist[v] = dist[u] + weight

    # The longest path would be the maximum value in dist array
    return max(dist)
