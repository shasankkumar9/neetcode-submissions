class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = [[] for _ in range(n)]
        seen = set()
        # q = deque([0])

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u, prev):
            if u in seen:
                return False
            
            seen.add(u)
            for v in graph[u]:
                if v == prev:
                    continue
                if not dfs(v, u):
                    return False
            return True
        
        return dfs(0,-1) and len(seen) == n
        # while q:
        #     u = q.popleft()
        #     for v in graph[u]:
        #         if v not in seen:
        #             seen.add(v)
        #             q.append(v)
        
        # return len(seen) == n