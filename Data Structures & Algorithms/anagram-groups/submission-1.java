class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        return new ArrayList<>(
            Arrays.stream(strs)
                  .collect(Collectors.groupingBy(this::key))
                  .values()
        );
    }

    private String key(String s) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) count[c - 'a']++;
        return Arrays.toString(count);
    }
}
