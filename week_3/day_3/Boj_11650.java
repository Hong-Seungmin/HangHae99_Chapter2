package day_3;

import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

// 주어진 좌표 x,y를 정렬한다.
// x를 우선 정렬하고,
// x가 같다면, y를 정렬한다.
// 정렬은 오른차순으로 한다.

// 입력은 첫째 줄에 좌표의 개수 n을 입력하고,
// 둘째 줄부터 각 좌표를 "x y"로 한줄씩 입력한다.
public class Boj_11650 {
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
            // 헤깔리지말자. 리턴이 양수이면 두 객체를 바꾼다.
            if (i1[0] > i2[0]) {
                return 1;
            } else if (i1[0] == i2[0]) {
                if (i1[1] > i2[1]) {
                   return 1;
                }else if( i1[1] == i2[1]){
                    return 0;
                }
            }
            return -1;
        });

        for (int[] coordinate : coordinates) {
            bw.write(String.valueOf(coordinate[0]) + " " + String.valueOf(coordinate[1]) + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
