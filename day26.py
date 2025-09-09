def has_cycle(V, edges):
    from collections import defaultdict

    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * V

    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:  # visited and not parent → cycle
                return True
        return False

    # Run DFS for each connected component
    for v in range(V):
        if not visited[v]:
            if dfs(v, -1):
                return True
    return False


print(has_cycle(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]))  # True
print(has_cycle(3, [[0, 1], [1, 2]]))                          # False
print(has_cycle(4, [[0, 1], [1, 2], [2, 0]]))                  # True
print(has_cycle(5, []))                                        # False (no edges)
print(has_cycle(3, [[0, 1], [0, 1]]))                          # True (parallel edges)
