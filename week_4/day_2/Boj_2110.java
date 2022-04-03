package day_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/2110
public class Boj_2110 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int[] home = new int[N];

        for (int i = 0; i < N; i++) {
            home[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(home);

        int result = bs(home, C, 1, home[N - 1] - home[0] + 1);

        System.out.println(result);
        br.close();
    }

    public static int bs(int[] home, int target, int start, int end) {
        int result = 1;
        while (start < end) {
            int mid = (start + end) / 2;

            int tmp_home = home[0];
            int count = 1;
            for (int i = 1; i < home.length; i++) {
                if (home[i] - tmp_home >= mid) {
                    count += 1;
                    tmp_home = home[i];
                }
            }

            if (count < target) {
                end = mid;
            } else {
                start = mid + 1;
            }

            result = start - 1;
        }
        return result;
    }
}
