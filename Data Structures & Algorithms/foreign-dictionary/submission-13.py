import string

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c:set() for w in words for c in w}
        inDegrees = [0] * 26

        self._buildGraph(graph, words, inDegrees)
        return self._topology(graph, inDegrees)
    
    def _buildGraph(self, graph, words, inDegrees):

        for fir, sec in zip(words, words[1:]):
            l = min(len(fir), len(sec))
            for j in range(l):
                u = fir[j]
                v = sec[j]
                if u != v:
                    if v not in graph[u]:
                        graph[u].add(v)
                        inDegrees[string.ascii_lowercase.index(v)] += 1
                    break
                if j == l-1 and len(fir) > len(sec):
                    graph.clear()
                    return
    
    def _topology(self, graph, inDegrees):
        s = ''
        q = deque([c for c in graph if inDegrees[string.ascii_lowercase.index(c)] == 0])

        while q:
            u = q.pop()
            s += u
            for v in graph[u]:
                inDegrees[string.ascii_lowercase.index(v)] -= 1
                if inDegrees[string.ascii_lowercase.index(v)] == 0:
                    q.append(v)
        
        return s if len(s) == len(graph) else ''