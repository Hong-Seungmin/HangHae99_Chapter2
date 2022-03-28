package day_3;

// https://www.acmicpc.net/problem/18310

import java.io.*;
import java.util.Arrays;

// 입력 : 첫째 줄에 집의 개수 N을 입력한다.
// 입력 : 둘째 줄에 N 만큼 집의 위치를 1~200,000범위 내에서 공백으로 구분하여 입력한다.
// 출력 : 가장 합리적인 위치를 출력한다. 중복될경우 가장 작은 값을 출력한다.
public class Boj_18310 {
    // 1. 각 위치별로 모든 위치의 상대적거리의 합을 구한다.
    // 2. 합산거리의 가장 작은 값을 가진 위치를 출력한다.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] locations = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();


        // 주어진 수의 중앙값이 합산거리가 가장 작은 값이다.
        Arrays.sort(locations);
        bw.write(Integer.toString(locations[(n - 1) / 2]));

        bw.flush();

        bw.close();
        br.close();
    }
}
