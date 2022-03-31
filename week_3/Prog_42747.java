
// https://programmers.co.kr/learn/courses/30/lessons/42747

import java.util.Arrays;

public class Prog_42747 {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] citations = new int[] {3,0,6,1,5};
//        int[] citations = new int[]{10, 9, 7, 6, 2, 1};
        System.out.println(sol.solution(citations));
    }

    static class Solution {
        public int solution(int[] citations) {

            Arrays.sort(citations);
            System.out.println(Arrays.toString(citations));
            int size = citations.length;
            int h = 0;
            for (int i = 0; i < size; i++) {
                if (citations[i] >= size - i) {
                    h = size - i;
                    break;
                }
            }
            return h;
        }
    }
}
