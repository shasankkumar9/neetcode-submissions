class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> res = Arrays.stream(strs).collect(Collectors.groupingBy(s -> {
            char[] st = s.toCharArray();
            Arrays.sort(st);
            return Arrays.toString(st);
        }));

        return new ArrayList<>(res.values());
    }
}
