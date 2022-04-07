// https://programmers.co.kr/learn/courses/30/lessons/43105
public class Prog_43105 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] triangle = {{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}};
        System.out.println(sol.solution(triangle));
    }

    static class Solution {
        public int solution(int[][] triangle) {
            int answer = 0;

            for (int i = triangle.length - 1; i > 0; i--) {
                for (int j = 0; j < triangle[i].length - 1; j++) {
                    int max = Math.max(triangle[i][j], triangle[i][j + 1]);
                    triangle[i - 1][j] += max;
                }
            }
            answer = triangle[0][0];

            return answer;
        }
    }
}
