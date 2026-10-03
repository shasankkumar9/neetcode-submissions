class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = [[] for _ in range(n)]
        seen = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(i):
            q = deque([i])
            seen.add(i)

            while q:
                u = q.pop()
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
        
        for i in range(n):
            if i not in seen:
                bfs(i)
                res += 1
        return res