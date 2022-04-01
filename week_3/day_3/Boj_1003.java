package day_3;

// https://www.acmicpc.net/problem/1003

import java.io.*;

// 피보나치 수열에서 0과 1이 리턴되는 횟수를 출력한다.
public class Boj_1003 {
    public static int[] fibonaccis = new int[41];
    public static int[] zero = new int[41];
    public static int[] one = new int[41];
//    public static int zero, one = 0;

    public static void main(String[] arg) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter((new OutputStreamWriter(System.out)));

        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];

        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < n; i++) {
            fibonacci(nums[i]);
            System.out.println(zero[nums[i]] + " " + one[nums[i]]);
        }


    }

    public static int fibonacci(int n) {
        if (n == 0) {
            zero[n] = 1;
            return 0;
        } else if (n == 1) {
            one[n] = 1;
            return 1;
        }
        if (fibonaccis[n] == 0) {
            fibonaccis[n] = fibonacci(n - 1) + fibonacci(n - 2);
            zero[n] = zero[n-1] + zero[n-2];
            one[n] = one[n-1] + one[n-2];
        }

        return fibonaccis[n];
    }
}
