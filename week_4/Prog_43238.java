import java.util.Arrays;

// https://programmers.co.kr/learn/courses/30/lessons/43238
public class Prog_43238 {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int n = 10;
        int[] times = {6, 8, 10};
        System.out.println(sol.solution(n, times));
    }

    static class Solution {
        public long solution(int n, int[] times) {
            Arrays.sort(times);
            long left = 0;
            long right = (long) n * times[times.length - 1];
            long sum = 0;
            while (left < right) {
                long mid = (left + right) / 2;

                sum = 0;
                for (int time :
                        times) {
                    sum += mid / time;
                }

                if (sum < n)
                    left = mid + 1;
                else
                    right = mid;
            }

            return right;
        }
    }
}

