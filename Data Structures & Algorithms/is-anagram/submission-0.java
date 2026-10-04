class Solution {
    public boolean isAnagram(String s, String t) {
        int[] seen = new int[26];
        for(char c: s.toCharArray()) {
            seen[c - 'a'] += 1;
        }

        for(char c : t.toCharArray()) {
            if(seen[c - 'a'] <= 0) {
                return false;
            }
            seen[c - 'a'] -= 1;
        }

        return !Arrays.stream(seen).anyMatch(v -> v != 0);
    }
}
