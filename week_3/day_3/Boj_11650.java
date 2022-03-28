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
            // 나름 쉽게 이해하는 로직을 생각해보았다.
            // 오름차순 정렬을 비교하기 위해선 i1 기준으로 i2에 비해
            // 1. 작다  2. 같다  3. 크다
            // 3가지가 필요하다. 실질적으로 두 항목에 대해선
            // 작거나 같으면 이동은 없지만, 전체 항목을 비교할때는 작은 경우를 알아야한다.
            // 이전에는 단순히 "리턴이 1이면 두 항목을 교체한다" 정도만 생각했는데,
            // 작을 경우도 고려를 해야한다는걸 깨달았다.

            // 그래서 생각해낸 로직은 단순하다.
            // 우선순위에 맞게 순차적으로,
            // 같으면 뒷 순위 수를 (앞 항목 빼기 뒤 항목) 를 리턴한다.
            // 가지 않으면 현재 순위 항목을 뺀다.
            // 밑의 코드는 우선순위가 2가지 이지만,
            // 3가지 이상이더라도 동일하게 순서대로 같다는 조건을 달아주면 된다. (앞 순위의 "같다"는 조건 밑으로..)
            if (i1[0] == i2[0]) {
                return i1[1] - i2[1];
            }else{
                return i1[0] - i2[0];
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
