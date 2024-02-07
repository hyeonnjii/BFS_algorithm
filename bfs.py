### BFS(Breadth-First Search)

from collections import deque


def bfs(graph, start_v):
    
    q = deque()
    visited = {}

    q.append(start_v)
    visited[start_v] = 0  # value를 distance로 표현

    while q:
        cur_v = q.popleft()
        print(f"Vertex: {cur_v}, Distance: {visited[cur_v]}")

        for next_v in graph[cur_v]:
            if next_v not in visited:
                q.append(next_v)
                visited[next_v] = visited[cur_v] + 1



# Examples
graph = {
    0: [1, 3, 6],
    1: [0, 3],
    2: [3],
    3: [0, 1, 2, 7],
    4: [5],
    5: [4, 6, 7],
    6: [0, 5],
    7: [3, 5],
}

bfs(graph, 0)
