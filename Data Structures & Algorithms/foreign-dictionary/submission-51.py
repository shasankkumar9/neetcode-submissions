class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c:set() for w in words for c in w}
        inDegrees = {c:0 for c in graph}

        self.buildGraph(graph,words,inDegrees)
        return self.topology(graph,inDegrees)

    def buildGraph(self, graph, words, inDegrees):

        for fir, sec in zip(words, words[1:]):
            l = min(len(fir), len(sec))
            for j in range(l):
                u = fir[j]
                v = sec[j]
                if u != v:
                    if v not in graph[u]:
                        graph[u].add(v)
                        inDegrees[v] += 1
                    break
                if j == l-1 and len(fir) > len(sec):
                    graph.clear()
                    return
    
    def topology(self, graph, inDegrees):
        s = ''
        q = deque([c for c in graph if inDegrees[c] == 0])

        while q:
            u = q.pop()
            s += u
            for v in graph[u]:
                inDegrees[v] -= 1
                if inDegrees[v] == 0:
                    q.append(v)
        return s if len(graph) == len(s) else ''