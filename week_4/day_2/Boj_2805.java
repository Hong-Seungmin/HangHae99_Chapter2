package day_2;
// https://www.acmicpc.net/problem/2805

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 절단기를 이용해 자른 나무의 총 길이(M)를 기준으로
// 최대한 높은 H를 구해야한다.
public class Boj_2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] array = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(array);

        int left = 0;
        int right = array[n - 1];
        int result = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            long sum = 0;

            for (int i :
                    array) {
                sum += Math.max(i - mid, 0);
            }

            if (sum >= m) {
                left = mid + 1;
                result = mid;
            } else {
                right = mid - 1;
            }
        }
        System.out.println(result);
    }
}
