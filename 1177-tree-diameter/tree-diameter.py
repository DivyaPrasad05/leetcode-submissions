from collections import deque
from typing import List

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        # Size by the max node label actually present
        n = max(max(u, v) for u, v in edges) + 1

        # Build adjacency
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        def bfs(start: int):
            q = deque([start])
            visited = [False] * n
            visited[start] = True
            dist = -1
            last = start

            while q:
                nxt = deque()
                while q:
                    u = q.popleft()
                    for w in adj[u]:
                        if not visited[w]:
                            visited[w] = True
                            nxt.append(w)
                            last = w
                dist += 1
                q = nxt
            return last, dist

        # Start from a known node that exists in the graph
        a, _ = bfs(edges[0][0])
        _, diameter = bfs(a)
        return diameter
