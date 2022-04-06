package day_5;

//  https://leetcode.com/problems/maximum-subarray/
public class Maximum_subarray {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};

        System.out.println(sol.maxSubArray(nums));
    }

    static class Solution {
        public int maxSubArray(int[] nums) {
            int max = Integer.MIN_VALUE;
            int sum = 0;

            for (int num : nums) {
                sum += num;
                if (sum < 0) {
                    max = Math.max(max, num);
                    sum = 0;
                } else {
                    max = Math.max(max, sum);
                }
            }

            return max;
        }
    }
}
