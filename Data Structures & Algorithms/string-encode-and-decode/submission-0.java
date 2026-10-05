class Solution {

    static final char DLM = '#';
    
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();


        for(String s : strs) {
            sb.append(s.length())
                .append(DLM)
                .append(s)
                .append(DLM);
        }

        return sb.toString();

    }

    public List<String> decode(String str) {
        int n = str.length();
        int i = 0;
        List<String> res = new ArrayList<>();

        while(i < n) {
            if(str.charAt(i) == DLM) {
                int l = ++i;
                while(i < n && str.charAt(i) != DLM) ++i;
                String word = str.substring(l, i);
                res.add(word);
            }
            ++i;
        }

        return res;

    }
}
