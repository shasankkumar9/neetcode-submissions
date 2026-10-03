class Solution {
    public String foreignDictionary(String[] words) {
        Map<Character, Set<Character>> graph = new HashMap<>();
        Map<Character, Integer> inDegrees = new HashMap<>();

        buildGraph(graph, words, inDegrees);
        return topology(graph, inDegrees);
    }

    private void buildGraph(Map<Character, Set<Character>> graph, 
                            String[] words, 
                            Map<Character, Integer> inDegrees) {

        for (final String word : words) 
            for (final char c : word.toCharArray()) {
                graph.putIfAbsent(c, new HashSet<>());
                inDegrees.putIfAbsent(c, 0);
            }


        for(int i = 0; i < words.length - 1; ++i) {
            String fir = words[i];
            String sec = words[i+1];

            int l = Math.min(fir.length(), sec.length());
            for(int j = 0; j < l; ++j) {
                char u = fir.charAt(j);
                char v = sec.charAt(j);
                if(u != v) {
                    if(!graph.get(u).contains(v)) {
                        graph.get(u).add(v);
                        inDegrees.merge(v,1,Integer::sum);
                    }
                    break;
                }
                if(j == l-1 && fir.length() > sec.length()) {
                    graph.clear();
                    return;
                }
            }

        }

    }

    private String topology(Map<Character, Set<Character>> graph,
                            Map<Character, Integer> inDegrees) {
        
        StringBuilder sb = new StringBuilder();
        Queue<Character> q = graph.keySet()
                             .stream()
                             .filter(c -> inDegrees.get(c) == 0)
                             .collect(Collectors.toCollection(ArrayDeque::new));
        // for(char c: graph.keySet())
        //     if (inDegrees.get(c) == 0)
        //         q.offer(c);


        while(!q.isEmpty()) {
            char u = q.poll();
            sb.append(u);
            for(char v : graph.get(u)) {
                inDegrees.merge(v, -1, Integer::sum);
                if(inDegrees.get(v) == 0)
                    q.offer(v);
            }
        }

        return sb.length() == graph.keySet().size() ? sb.toString() : "";

    }
}
