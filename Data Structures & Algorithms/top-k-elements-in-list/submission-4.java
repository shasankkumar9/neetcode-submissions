class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = Arrays.stream(nums).boxed()
                .collect(Collectors.groupingBy(x -> x,
                    Collectors.collectingAndThen(Collectors.counting(), Long::intValue)));
        
        Queue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for(Map.Entry<Integer, Integer> entry : count.entrySet()) {
            heap.offer(new int[] {entry.getValue(), entry.getKey()});
            if(heap.size() > k) heap.poll();
        }

        return heap.stream().mapToInt(v -> v[1]).toArray();

    }
}