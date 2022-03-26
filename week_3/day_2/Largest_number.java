package day_2;

import sun.jvm.hotspot.utilities.IntArray;

import java.util.Arrays;
import java.util.stream.IntStream;

public class Largest_number {
    public static void main(String[] args) {
        Solution sol = new Solution();

    }
}

// 주어진 정수 배열을 이용하여,
// 만들 수 있는 가장 큰 숫자의 문자열을 반환하라.
class Solution {

    // 숫자 배열을 정렬한 다음, 문자열로 만들면 가장 큰 숫자가 구성될것이다.
    // 단, 숫자의 가장 앞자리부터 기준으로 9에 가까운것이 앞으로 정렬해야한다.
    public String largestNumber(int[] nums) {
        int i = 1;

        while (i < nums.length) {
            int j = i;
            while ( j > 0 && toSwap(nums[j-1], nums[j])){
                int tmp = nums[j];
                nums[j] = nums[j-1];
                nums[j-1] = tmp;
                j -= 1;
            }
            i += 1;
        }
        if (nums[0] == 0) return "0";

        StringBuilder sb = new StringBuilder();
        for(int num:nums){
            sb.append(num);
        }

        return sb.toString();
    }

    public boolean toSwap(int n1, int n2) {
        String s1 = String.valueOf(n1);
        String s2 = String.valueOf(n2);

        return (s1+s2).compareTo(s2+s1) < 0 ;
    }
}