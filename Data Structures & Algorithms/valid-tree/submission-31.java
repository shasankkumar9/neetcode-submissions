class Solution {

    private class UnionFind {
        private int count;
        private int[] id;
        private int[] rank;

        public UnionFind(int n) {
            this.count = n;
            this.id = IntStream.range(0,n).toArray();
            this.rank = new int[n];
        }

        public void unionByRank(int u, int v) {
            int i = find(u);
            int j = find(v);
            if(i == j) return;
            if(rank[i] < rank[j]) {
                id[i] = j;
            } else if(rank[i] > rank[j]) {
                id[j] = i;
            } else {
                id[i] = j;
                ++rank[j];
            }
            --count;
        }

        private int find(int u) {
            if(id[u] != u)
                id[u] = find(id[u]);
            return id[u];
        }

        public int getCount() {
            return count;
        }

    }

    public boolean validTree(int n, int[][] edges) {
        if(edges.length != n-1) return false;

        UnionFind uf = new UnionFind(n);

        for(int[] edge: edges) {
            uf.unionByRank(edge[0], edge[1]);
        }

        return uf.getCount() == 1;

    }
}
