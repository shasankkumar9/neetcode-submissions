class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        return !Arrays.stream(nums).allMatch(seen::add);
    }
}