class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> memo = new HashMap<>();

        for(int i = 0; i < nums.length; ++i) {
            if(memo.containsKey(target - nums[i])) {
                return new int[] {memo.get(target - nums[i]), i};
            }
            memo.put(nums[i], i);
        }
        throw new IllegalArgumentException();
    }
}
