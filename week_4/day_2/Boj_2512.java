package day_2;
// https://www.acmicpc.net/problem/2512

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 각 지방의 요청 예산을 지급하되, 총예산을 초과한 경우,
// 총예산을 넘지 않는 한, 요청한 예산액에 대해 최대한 많은 예산을 지급할 수 있도록 조절한다.
public class Boj_2512 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] array = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            array[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());

        Arrays.sort(array);

//        System.out.println(m / n);
//        System.out.println(Arrays.toString(array));

        int left = 0;
        int right = array[n - 1];
        int result = 0;
        while (left <= right) {
            int mid = (left + right) / 2;

            int sum = 0;
            for (int i :
                    array) {
                sum += Math.min(i, mid);
            }

            if (sum <= m) {
                left = mid + 1;
                result = mid;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(result);
    }
}
