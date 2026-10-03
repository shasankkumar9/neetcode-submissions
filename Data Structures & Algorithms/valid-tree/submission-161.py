class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        count = n
        id = list(range(n))
        rank = [0] * n

        def find(u):
            if id[u] != u:
                id[u] = find(id[u])
            return id[u]

        for u, v in edges:
            i = find(u)
            j = find(v)
            if i == j:
                continue
            if rank[i] < rank[j]:
                id[i] = j
            elif rank[i] > rank[j]:
                id[j] = i
            else:
                id[i] = j
                rank[j] += 1
            count -= 1
        
        return count == 1
        
        # graph = [[] for _ in range(n)]
        # seen = set() # {0}
        # q = deque([0])

        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # while q:
        #     u = q.popleft()
        #     for v in graph[u]:
        #         if v not in seen:
        #             seen.add(v)
        #             q.append(v)
        
        # return len(seen) == n

        # def dfs(u, prev):
        #     if u in seen:
        #         return
        #     seen.add(u)
        #     for v in graph[u]:
        #         if v == prev:
        #             continue
        #         if not dfs(v, u):
        #             return False
            
        #     return True
        
        # return dfs(0, -1) and len(seen) == n