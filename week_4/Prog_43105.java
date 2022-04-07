
// https://programmers.co.kr/learn/courses/30/lessons/43105
public class Prog_43105 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] triangle = {{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}};
        System.out.println(sol.solution(triangle));
    }

    static class Solution {
        public int solution(int[][] triangle) {
            int sum = triangle[0][0];

            int j = 0;
            for (int i = 1; i < triangle.length; i++) {
                System.out.println(j);
                if (triangle[i][j] > triangle[i][j + 1]) {
                    sum += triangle[i][j];
                }else{
                    sum += triangle[i][j+1];
                    j = j + 1;
                }
            }

            return sum;
        }
    }
}
