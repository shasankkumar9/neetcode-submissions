class UnionFind:
    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.rank = [0] * n
    
    def union(self, u, v):
        i = self._find(u)
        j = self._find(v)
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            self.id[i] = j
        elif self.rank[i] > self.rank[j]:
            self.id[j] = i
        else:
            self.id[j] = i
            self.rank[j] += 1
        self.count -= 1
    
    def _find(self, u):
        if self.id[u] != u:
            self.id[u] = self._find(self.id[u])
        return self.id[u]

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)
        
        return uf.count == 1
        
        # graph = [[] for _ in range(n)]
        # seen = set()
        # q = deque([0])

        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # def dfs(u, prev):
        #     if u in seen:
        #         return False
            
        #     seen.add(u)
        #     for v in graph[u]:
        #         if v == prev:
        #             continue
        #         if not dfs(v, u):
        #             return False
        #     return True
        
        # return dfs(0,-1) and len(seen) == n
        # while q:
        #     u = q.popleft()
        #     for v in graph[u]:
        #         if v not in seen:
        #             seen.add(v)
        #             q.append(v)
        
        # return len(seen) == n