package day_5;

// https://www.acmicpc.net/problem/2751

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

// 수 정렬하기, 입력된 수를 정렬하여 출력하면된다.
public class Boj_2751 {
    public static void main(String[] args) throws IOException {
//        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        ArrayList<Integer> nums = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            nums.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(nums);

        StringBuilder sb = new StringBuilder();

        for (int num :
                nums) {
            sb.append(num).append("\n");
        }

        System.out.println(sb);
        br.close();

    }
}
