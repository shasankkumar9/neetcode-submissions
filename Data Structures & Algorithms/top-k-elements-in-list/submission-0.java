class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();

        for(int i : nums) {
            count.merge(i, 1, Integer::sum);
        }
        return count.entrySet().stream()
            .sorted(Comparator.comparingInt((Map.Entry<Integer, Integer> e) -> e.getValue()).reversed())
            .limit(k)
            .mapToInt(Map.Entry::getKey)
            .toArray();
        
    }
}
