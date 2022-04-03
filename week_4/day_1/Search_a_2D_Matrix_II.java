package day_1;

// https://leetcode.com/problems/search-a-2d-matrix-ii/

// 주어진 2차 배열(matrix)에 담긴 정수들 중 target 정수가 포함되어있는지 확안한다.

public class Search_a_2D_Matrix_II {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] matrix = new int[][] {{1,4,7,11,15},{2,5,8,12,19},{3,6,9,16,22},{10,13,14,17,24},{18,21,23,26,30}};
        System.out.println(sol.searchMatrix(matrix,20));
    }
}
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int r = matrix.length;
        int c = matrix[0].length;

        for (int[] col : matrix) {
            int start = 0;
            int end = c - 1;
            while (start <= end) {
                int mid = (start + end) / 2;

                if (col[mid] < target) {
                    start = mid + 1;
                } else if (col[mid] > target) {
                    end = mid - 1;
                } else {
                    return true;
                }
            }
        }
        return false;
    }
}