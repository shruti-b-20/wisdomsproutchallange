from collections import deque, defaultdict

def shortest_path_unweighted(V, edges, start, end):
    # Edge case: start and end are same
    if start == end:
        return 0
    
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # undirected graph
    
    # BFS setup
    visited = [False] * V
    distance = [-1] * V
    queue = deque([start])
    
    visited[start] = True
    distance[start] = 0
    
    # BFS loop
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
                
                if neighbor == end:
                    return distance[neighbor]
    
    # If end not reachable
    return -1
print(shortest_path_unweighted(5, [[0,1],[0,2],[1,3],[2,3],[3,4]], 0, 4))  # Output: 3
print(shortest_path_unweighted(3, [[0,1],[1,2]], 0, 2))                     # Output: 2
print(shortest_path_unweighted(4, [[0,1],[1,2]], 2, 3))                     # Output: -1
print(shortest_path_unweighted(1, [], 0, 0))                                # Output: 0
