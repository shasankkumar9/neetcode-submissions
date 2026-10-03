class UnionFind:
    def __init__(self, n):
        self.count = n
        self.id = list(range(n))
        self.rank = [0] * n

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        if self.rank[i] < self.rank[j]:
            self.id[i] = j
        elif self.rank[i] > self.rank[j]:
            self.id[j] = i
        else:
            self.id[i] = j
            self.rank[j] += 1
        self.count -= 1
    
    def find(self,u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # graph = [[] for _ in range(n)]
        # seen = set()

        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # def bfs(i):
        #     q = deque([i])
        #     seen.add(i)
        #     while q:
        #         u = q.popleft()
        #         for v in graph[u]:
        #             if v not in seen:
        #                 seen.add(v)
        #                 q.append(v)

        # def dfs(i):
        #     for v in graph[i]:
        #         if v not in seen:
        #             seen.add(v)
        #             dfs(v)
        
        # res = 0

        # for i in range(n):
        #     if i not in seen:
        #         seen.add(i)
        #         dfs(i)
        #         res += 1
        
        # return res

        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u,v)

        return uf.count