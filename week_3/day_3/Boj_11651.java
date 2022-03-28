package day_3;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

// https://www.acmicpc.net/problem/11651

// 이 문제는 아래 링크에서 정렬의 우선순위만 다를 뿐이니 주석은 생략하겠다.
// https://www.acmicpc.net/problem/11650
public class Boj_11651 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        int[][] coordinates = new int[n][2];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            coordinates[i][0] = Integer.parseInt(st.nextToken());
            coordinates[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(coordinates,(i1, i2) -> {
            if (i1[1] == i2[1]) {
                return i1[0] - i2[0];
            }else{
                return i1[1] - i2[1];
            }
        });

        for (int[] coordinate : coordinates) {
            bw.write(coordinate[0] + " " + coordinate[1] + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
