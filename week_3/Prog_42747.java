
// https://programmers.co.kr/learn/courses/30/lessons/42747

import java.util.Arrays;

// 주어진 숫자(인용횟수 h) 배열을 이용하여, H-Index를 출력한다.
// H-Index는 주어진 h 중
// h 보다 큰 숫자가 h개 이상이고,
// h 보다 작은 숫자가 h개 이하인 수들 중 가장 큰 수를 출력한다.
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
            //[0, 1, 3, 5, 6]
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
