class Solution {
    public int evalRPN(String[] tokens) {
        Set<String> operators = new HashSet<>(Arrays.asList("+", "-", "*", "/"));
        Stack<Integer> s = new Stack<>();

        for (String t : tokens) {
            if (!operators.contains(t)) {
                s.push(Integer.valueOf(t));
            }
            else {
                int res = 0;
                if (t.equals("+")) {
                    res = s.pop() + s.pop();
                }
                else if (t.equals("-")) {
                    res += -(s.pop());
                    res += s.pop();
                }
                else if (t.equals("*")) {   
                    res = s.pop() * s.pop();
                }
                else {
                    int op;
                    op = s.pop();
                    res = s.pop() / op;
                }
                s.push(res);
            }
        }

        return s.pop();
    }
}