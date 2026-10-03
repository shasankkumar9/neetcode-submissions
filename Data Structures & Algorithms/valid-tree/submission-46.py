class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = [[] for _ in range(n)]
        seen = {0}
        q = deque([0])

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        while q:
            u = q.popleft()

            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
            
        return len(seen) == n