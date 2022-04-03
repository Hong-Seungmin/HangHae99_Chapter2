package day_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/1654
public class Boj_1654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[] array = new int[k];
        for (int i = 0; i < k; i++) {
            array[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(array);

        long left = 1;
        long right = array[k - 1];
        long result = 0;
        while (left <= right) {
            long mid = (left + right) / 2;
            long count = 0;

            for (int i :
                    array) {
                count += i / mid;
            }

            if (count >= n) {
                result = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(result);
    }
}
