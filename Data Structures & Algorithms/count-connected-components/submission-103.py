class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

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
        
        return count
        
        # graph = [[] for _ in range(n)]
        # seen = set()

        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # def bfs(i):
        #     q = deque([i])
        #     while q:
        #         u = q.popleft()
        #         for v in graph[u]:
        #             if v not in seen:
        #                 seen.add(v)
        #                 q.append(v)

        # def dfs(u):
        #     for v in graph[u]:
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