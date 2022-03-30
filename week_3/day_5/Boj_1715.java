package day_5;
// https://www.acmicpc.net/problem/1715

import java.io.*;
import java.util.PriorityQueue;

// 주어진 카드 묶음을 가장 최소 비교하여 최종 비교 수를 출력하라.
public class Boj_1715 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            queue.add(Integer.parseInt(br.readLine()));
        }

        int sum = 0;

        while (queue.size() > 1) {
            int n1 = queue.poll();

            if(!queue.isEmpty()) {
                sum += n1 + queue.peek();
                queue.add(n1 + queue.poll());
            }
        }

        bw.write(String.valueOf(sum));

        bw.flush();
        bw.close();
        br.close();
    }
}
